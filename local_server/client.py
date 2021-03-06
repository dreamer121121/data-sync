import requests
import os.path
import urllib.parse
import datetime
import time
import logging.config
import re
import json
import pymysql
from cli_config import DATABASES


TIME = 0
TABLES = []
REMOTE_ADDRS = ''
FIRST_TIME = ''




logging_config = os.path.join(os.path.dirname(__file__), 'logging.conf')#logging.conf路径
logging.config.fileConfig(logging_config)
logger = logging.getLogger('root')


def get_config():

    """
    get config_params
    :return:
    """

    global TIME,TABLES,REMOTE_ADDRS,FIRST_TIME
    f = open('config_params.txt','r')
    CONFIG = json.loads(f.read())
    TIME = int(CONFIG['TIME'])
    TABLES = CONFIG['TABLES']
    REMOTE_ADDRS =  CONFIG['REMOTE_ADDRS']
    FIRST_TIME = CONFIG['FIRST_TIME'] #只在第一次同步时使用（客户不可更改）


def create_conn(db_name):
    conn = pymysql.connect(host=DATABASES[db_name]['HOST'],user=DATABASES[db_name]['USER'], database=DATABASES[db_name]['NAME'], password=DATABASES[db_name]['PASSWORD'])
    return conn

def _write_in_history(now):
    """
    write in success_history
    :param now:the date of success_sync
    :return:
    """
    f = open('success_history.txt', 'w')
    f.write("本次同步时间："+str(now))
    f.close()

def get_lasttime():
    """
    get lasttime history
    :return:
    """
    f = open('success_history.txt','r')
    lastime = f.readlines()
    f.close()
    if not lastime:
        lastime = FIRST_TIME #只用于第一次同步时使用这一参数（用户不可更改公司根据给客户安装的数据库的日期进行更改）
        lastime = re.search('(\d+.*) ' ,lastime).group(0)
    else:
        lastime = lastime[-1]
        lastime = re.search('(\d+.*) ' ,lastime).group(0)
    return lastime

def _create_params(lastime,now):
    """
    create requests params
    :param lastime:
    :param now:
    :return:
    """
    json = {}
    json['from'] = lastime
    json['to'] = now
    return json

def _create_url(url,json):
    """
    create url
    :param url:
    :param json:
    :return:
    """
    params = urllib.parse.urlencode(json)
    url += params
    return url

def pull_data():

    """
    pull data from remote DB
    :return:
    """
    error_db_info = ''
    base_urls = []
    for table in TABLES:
        root_url = ""
        root_url += REMOTE_ADDRS+table+"?"
        base_urls.append(root_url)

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    enddate = str(now)[0:10]
    lastime = get_lasttime()
    params = _create_params(lastime,enddate)

    try:
        for base_url in base_urls:
            table_name = re.search(r'get/(\w+)?',base_url).group(1)
            error_db_info = table_name
            url = _create_url(base_url,params)

            logger.info("**********"+lastime+" --- "+enddate+"**********")
            logger.info("INFO begin get data from: "+table_name)
            data = requests.get(url).json()
            logger.info("INFO get data from "+table_name+" total: "+str(len(data['detail'])))

            logger.info("INFO begin insert data to "+table_name)
            time.sleep(5)

            insert_data(data,table_name)
            logger.info("INFO finish data-sync for "+table_name)

        logger.info("INFO  finish data-sync all database")
        _write_in_history(now)  # 写入success_history

    except Exception as e:
        error_f = open('error_history.txt','w')
        error_f.write("最近一次错误：Error get "+error_db_info+':%s'%e)
        error_f.close()

        logger.error("Error get "+error_db_info+':%s'%e)
        logger.error("Error data-sync failed this time !!!")


def db2fields(table_name):

    DB2fields={}
    DB2fields['Cve'] = ['id', 'num', 'score', 'secrecy', 'integrity', 'usability', 'complexity', 'vectorofattack', 'identify',
                 'kind', 'cpe', 'finddate', 'summary', 'update_time']
    DB2fields['Vulnerability'] = ['name', 'vendor', 'level', 'description', 'url', 'mitigation', 'provider', 'update_time']
    DB2fields['Dev2vul'] = ['name', 'device', 'vulnerability','update_time']
    DB2fields['Conpot_log'] = ['date','time','function_id','protocol','request','destIP','sourcePort','DestPort','slaveID',
                               'sourceIP','response','country','subdivision','city','coordinate']
    DB2fields['Instance'] = ['name','vendor','ip','city','country','continent','asn','lat','lon',
                                           'hostname','service','os','app','extrainfo','version','timestamp']
    DB2fields['Instanceport'] = ['id','ip','port','nw_proto','protocol','banner','status','add_time','update_time','instance_id']


    return DB2fields[table_name]

def create_sql(data,fields,table_name):
    table_name = table_name.lower()
    if table_name == 'Vulnerability':
        table_name = 'knowledgeBase_vulnerability'
    elif table_name == 'Dev2vul':
        table_name = 'knowledgeBase_dev2vul'
    elif table_name == 'Instance':
        table_name = 'knowledgeBase_instance'
    elif table_name == 'Instanceport':
        table_name = 'knowledgeBase_instanceport'

    sql = 'replace into '+ table_name + str(tuple(fields))  # 去重
    values = []
    sql = sql.replace('\'', '')
    sql_values = ' values'
    for field in fields:
        values.append(data[field])
    values = str(tuple(values))
    sql_values += values
    sql += sql_values
    # sql = sql.replace('\'', '')
    return sql




def insert_data(content,table_name):

    """
    insert data into localDB
    :param content:
    :param table_name:
    :return:
    """
    if table_name == 'Cve':
        db_name = 'ics'
        fields =db2fields(table_name)
        content = content['detail']
        conn = create_conn(db_name)
        if content:
            for data in content:
                sql = create_sql(data,fields,table_name) #逐条插入
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
        else:
            pass


    elif table_name == 'Vulnerability':

        db_name = 'ics_scan'
        fields =db2fields(table_name)
        content = content['detail']
        conn = create_conn(db_name)
        
        if content:
            for data in content:
                sql = create_sql(data,fields,table_name) #逐条插入
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
        else:
            pass

    elif table_name == 'Ddev2vul':

        db_name = 'ics_scan'
        fields = db2fields(table_name)
        content = content['detail']
        conn = create_conn(db_name)
        if content:
            for data in content:
                sql = create_sql(data,fields,table_name) #逐条插入
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
        else:
            pass

    elif table_name == 'Conpot_log':

        db_name = 'ics'
        fields = db2fields(table_name)
        content = content['detail']
        conn = create_conn(db_name)
        if content:
            for data in content:
                sql = create_sql(data,fields,table_name) #逐条插入
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
        else:
            pass

    elif table_name == 'Instance':

        db_name = 'ics_scan'
        fields = db2fields(table_name)
        content = content['detail']
        conn = create_conn(db_name)
        if content:
            for data in content:
                sql = create_sql(data,fields,table_name) #逐条插入
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
        else:
            pass

    elif table_name == 'Instanceport':

        db_name = 'ics_scan'
        fields = db2fields(table_name)
        content = content['detail']
        conn = create_conn(db_name)
        if content:
            for data in content:
                sql = create_sql(data,fields,table_name) #逐条插入
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
        else:
            pass


if __name__ == '__main__':

    if not os.path.exists('success_history.txt'):
        f = open('success_history.txt', 'w')
        f.close()

    if not os.path.exists('error_history.txt'):
        f = open('error_history.txt', 'w')
        f.close()

    while True:
        get_config()    #每一个拉取循环都要重新获取配置参数
        SECOND = TIME*3600 #把小时转换为秒
        pull_data()
        logger.info("INFO start sleep")
        time.sleep(SECOND)  # //完成一次拉取开始休眠