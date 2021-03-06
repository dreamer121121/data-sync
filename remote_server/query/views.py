from django.conf import settings
import pymysql
import logging
from common.function import success_msg,error_msg,json_response
from common.error_code import E000
import datetime
from common.decorators import http_method_required

logger = logging.getLogger(__name__)

TABLES = {'cve':'cve','vulnerability':'knowledgeBase_vulnerability','dev2vul':'knowledgeBase_dev2vul',
          'instance':'knowledgeBase_instance','instanceport':'knowledgeBase_instanceport','conpot_log':'conpot_log'}

def Connect(DATABASE):
    conn = pymysql.connect(host = DATABASE['HOST'],user= DATABASE['USER'],password=DATABASE['PASSWORD'],db=DATABASE['NAME'])
    cursor = conn.cursor()
    return  cursor

def process_request(request):

    start_date = request.GET.get('from')
    end_date = request.GET.get('to')
    if not end_date:  # 若没有截止日期则默认为从上一次开始到当前数据库中最新
        end_date = str(datetime.datetime.now())
        end_date = end_date[0:10]
    return start_date,end_date

def verify(user,password):
    print("---verify--")
    DATABASE = settings.DATABASES['data_sync']
    cursor = Connect(DATABASE)
    sql = 'select * from verify where user = '+'\''+str(user)+'\''
    cursor.execute(sql)
    rows = cursor.fetchall()[0]
    print("--rows---",rows)
    if rows:
        if rows[0] == user and rows[1] == password:
            return True
    else:
        return False




def getCve(request):
    DATABASE = settings.DATABASES['default']
    try:
        start_date,end_date = process_request(request)
        sql = 'select * from cve where update_time >='+'\''+start_date+'\''+' and update_time <= '+'\''+end_date+'\''
        cursor = Connect(DATABASE)
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("count cve vulnerability of this time: "+str(len(rows)))
        print('----sql-----',len(rows))

        result = []
        for row in rows:
            cves = {}
            cves["id"] = row[0]
            cves["num"] = row[1]
            cves["score"] = row[2]
            cves["secrecy"] = row[3]
            cves["integrity"] = row[4]
            cves["usability"] = row[5]
            cves["complexity"] = row[6]
            cves["vectorofattack"] = row[7]
            cves["identify"] = row[8]
            cves["kind"] = row[9]
            cves["cpe"] = row[10]
            cves["finddate"] = row[11]
            cves["summary"] = row[12]
            cves["update_time"] = row[13]
            result.append(cves)

        return json_response(success_msg(result))

    except Exception as e:

        logger.error("get cve error :%s"%e)
        return json_response(error_msg(E000.code,E000.msg))


def getCnvd(request):
    DATABASE = settings.DATABASES['ics_scan']
    try:
        start_date, end_date = process_request(request)
        sql = 'select * from knowledgeBase_vulnerability where update_time >='+'\''+start_date+'\''+' and update_time <= '+'\''+end_date+'\''
        cursor = Connect(DATABASE)
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("count cnvd vulnerability of this time: "+str(len(rows)))
        print('----sql-----',len(rows))

        result = []
        for row in rows:
            cnvd = {}
            cnvd["name"] = row[0]
            cnvd["vendor"] = row[1]
            cnvd["level"] = row[2]
            cnvd["description"] = row[3]
            cnvd["url"] = row[4]
            cnvd["mitigation"] = row[5]
            cnvd["provider"] = row[6]
            cnvd["date"] = row[7]
            cnvd["update_time"] = row[8]
            result.append(cnvd)

        return json_response(success_msg(result))

    except Exception as e:
        logger.error("get cnvd error :%s"%e)
        return json_response(error_msg(E000.code,E000.msg))

def getDev2vul(request):
    DATABASE = settings.DATABASES['ics_scan']
    try:
        start_date, end_date = process_request(request)
        sql = 'select * from knowledgeBase_dev2vul where update_time >='+'\''+start_date+'\''+' and update_time <= '+'\''+end_date+'\''
        cursor = Connect(DATABASE)
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("count dev2vul of this time: "+str(len(rows)))
        print('----sql-----',len(rows))

        result = []
        for row in rows:
            dev2vul = {}
            dev2vul["name"] = row[0]
            dev2vul["device"] = row[1]
            dev2vul["vulnerability"] = row[2]
            dev2vul["update_time"] = row[3]
            result.append(dev2vul)
        return json_response(success_msg(result))

    except Exception as e:
        logger.error("get dev2vul error :%s"%e)
        return json_response(error_msg(E000.code,E000.msg))


def getInstance(request):
    DATABASE = settings.DATABASES['ics_scan']
    try:
        start_date, end_date = process_request(request)
        sql = 'select * from knowledgeBase_instance where update_time >='+'\''+start_date+'\''+' and update_time <= '+'\''+end_date+'\''
        cursor = Connect(DATABASE)
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("count instance of this time: "+str(len(rows)))

        result = []
        for row in rows:
            print(len(row))
            instance = {}
           # instance["name"] = row[0]
            instance["vendor"] = row[0]
            instance["ip"] = row[1]
            instance['city'] = row[2]
            instance['country'] = row[3]
            instance['continent'] = row[4]
            instance['asn'] = row[5]
            instance['lat'] = row[6]
            instance['lon'] = row[7]
            instance['hostname'] = row[8]
            instance['service'] = row[9]
            instance['os'] = row[10]
            instance['app'] = row[11]
            instance['extrainfo'] = row[12]
            instance['version'] = row[13]
            instance['timestamp'] = row[14]
            instance['type_index'] = row[15]
            instance['update_time'] = row[16]
            instance['from_scan'] = row[17]
            instance['from_spider'] = row[18]
            instance['isp'] = row[19]
            instance['organization'] = row[20]
            instance['from_web'] = row[21]
            result.append(instance)
        return json_response(success_msg(result))

    except Exception as e:
        logger.error("get instance error :%s"%e)
        return json_response(error_msg(E000.code,E000.msg))


def getInstanceport(request):

    DATABASE = settings.DATABASES['ics_scan']
    try:
        start_date, end_date = process_request(request)
        sql = 'select * from knowledgeBase_instanceport where update_time >=' + '\'' + start_date + '\'' + ' and update_time <= ' + '\'' + end_date + '\''
        cursor = Connect(DATABASE)
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("count instanceport of this time: " + str(len(rows)))

        result = []
        for row in rows:
            instanceport = {}
            instanceport["id"] = row[0]
            instanceport["ip"] = row[1]
            instanceport["port"] = row[2]
            instanceport['nw_proto'] = row[3]
            instanceport['protocol'] = row[4]
            instanceport['banner'] = row[5]
            instanceport['status'] = row[6]
            instanceport['add_time'] = row[7]
            instanceport['update_time'] = row[8]
           # instanceport['instance_id'] = row[9]

            result.append(instanceport)
        return json_response(success_msg(result))

    except Exception as e:
        logger.error("get instanceport error :%s" % e)
        return json_response(error_msg(E000.code, E000.msg))


def getAttack(request):
    DATABASE = settings.DATABASES['default']
    try:
        start_date, end_date = process_request(request)
        sql = 'select * from conpot_log where date >='+'\''+start_date+'\''+' and date <= '+'\''+end_date+'\''
        cursor = Connect(DATABASE)
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("count conpot_log of this time: "+str(len(rows)))
        print('----sql-----',len(rows))

        result = []
        for row in rows:
            row = list(row)
            for j in range(len(row)):
                if row[j] == None:
                    row[j] = "Null"
            conpot_log = {}
            conpot_log["date"] = str(row[0])
            conpot_log["time"] = str(row[1])
            conpot_log["function_id"] = row[2]
            conpot_log["protocol"] = row[3]
            conpot_log["request"] = row[4]
            conpot_log["destIP"] = row[5]
            conpot_log["sourcePort"] = row[6]
            conpot_log["DestPort"] = row[7]
            conpot_log["slaveID"] = row[8]
            conpot_log["sourceIP"] = row[9]
            conpot_log["response"] = row[10]
            conpot_log["country"] = row[11]
            conpot_log["subdivision"] = row[12]
            conpot_log["city"] = row[13]
            conpot_log["coordinate"] = row[14]
            result.append(conpot_log)
        return json_response(success_msg(result))

    except Exception as e:
        logger.error("get conpot_log error :%s"%e)
        return json_response(error_msg(E000.code,E000.msg))


@http_method_required('GET')
def getdata(request):

    try:

        user = request.GET.get('user')
        password = request.GET.get('password')
        key = request.GET.get('key')
        print("---key---",key)
        #验证用户名和密码
        if verify(user,password):
            if key in TABLES.keys():
                if key == 'cve':
                    print("---cve----")
                    return getCve(request)
                elif key == 'vulnerability':
                    return getCnvd(request)
                elif key == 'dev2vul':
                    return getDev2vul(request)
                elif key == 'instance':
                    return getInstance(request)
                elif key == 'instanceport':
                    return getInstanceport(request)
                elif key == 'conpot_log':
                    return getAttack(request)
        else:
            msg = "用户名或者密码错误"
            return json_response(error_msg(E000.code,msg))

    except Exception as e:
        return json_response(error_msg(E000.code, E000.msg))


