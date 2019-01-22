from django.conf import settings
import pymysql
import logging
from common.function import success_msg,error_msg,json_response
from common.error_code import E000
import datetime

logger = logging.getLogger(__name__)

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
            result.append(dev2vul)
        return json_response(success_msg(result))

    except Exception as e:
        logger.error("get dev2vul error :%s"%e)
        return json_response(error_msg(E000.code,E000.msg))


def getInstance():
    pass



def getInstancport():
    pass

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

