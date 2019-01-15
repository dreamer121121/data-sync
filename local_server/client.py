import requests
import os.path
import urllib.parse
import datetime
import time
from cli_config import TIME,DATABASES,FIRST_TIME,REMOTE_ADDRS,conn
import logging.config
import re
import json



logging_config = os.path.join(os.path.dirname(__file__), 'logging.conf')#logging.conf路径
logging.config.fileConfig(logging_config)
logger = logging.getLogger('root')


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
        lastime = FIRST_TIME
    else:
        lastime = lastime[-1]
        lastime = re.search('(\d+.*) ' ,lastime).group(0)
        print('----32----',lastime)
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
    for db in DATABASES:
        base_url = REMOTE_ADDRS+db+"?"
        base_urls.append(base_url)

    now = datetime.datetime.now()
    date = str(now)[0:10]
    lastime = get_lasttime()
    params = _create_params(lastime,date)

    try:
        for base_url in base_urls:
            error_db_info = base_url
            db_name = base_url[33:36]
            url = _create_url(base_url,params)
            logger.info("INFO begin get data from: "+db_name)
            data = requests.get(url).json()
            logger.info("INFO get data from "+db_name+" total: "+str(len(data['detail'])))
            time.sleep(5)
            logger.info("INFO begin insert data to "+db_name)
            insert_data(data,db_name)
            logger.info("INFO finish data-sync for "+db_name)

        logger.info("INFO  finish data-sync all database")
        _write_in_history(now)  # 写入success_history

    except Exception as e:
        logger.error("Error get "+error_db_info[25:36]+':%s'%e)
        logger.error("Error data-sync failed this time !!!")



def insert_data(content,db_name):

    """
    insert data into localDB
    :param content:
    :param db_name:
    :return:
    """

    if db_name == 'Cve':
        fields =['id', 'num', 'score', 'secrecy', 'integrity', 'usability', 'complexity', 'vectorofattack', 'identify',
                 'kind', 'cpe', 'finddate', 'summary', 'update_time']

        content = content['detail']
        if content:
            for data in content:
                values = []
                sql = 'replace into cve'+str(tuple(fields))#去重
                sql = sql.replace('\'','')
                sql_values = ' values'
                for field in fields:
                    values.append(data[field])
                values = str(tuple(values))
                values=values
                print(values)
                sql_values += values
                sql += sql_values
                cursor = conn.cursor()
                cursor.execute(sql)

    elif db_name == 'Cnvd':
        pass


if __name__ == '__main__':
    if not os.path.exists('success_history.txt'):
        f = open('success_history.txt', 'w')
        f.close()

    while True:
        pull_data()
        logger.info("INFO start sleep")
        time.sleep(TIME)  # //完成一次拉取开始休眠
