from django.conf import settings
import pymysql
import logging
from common.function import success_msg,error_msg,json_response
from common.error_code import E000
import datetime

logger = logging.getLogger(__name__) #日志命名
DATABASE = settings.DATABASES['default']

def Connect():
    conn = pymysql.connect(host = DATABASE['HOST'],user= DATABASE['USER'],password=DATABASE['PASSWORD'],db=DATABASE['NAME'])
    cursur = conn.cursor()
    return  cursur


def getCve(request):
    try:
        start_date = request.GET.get('from')
        end_date = request.GET.get('to')
        if not end_date:#若没有截止日期则默认为从上一次开始到当前数据库中最新
            end_date = str(datetime.datetime.now())
            end_date = end_date[0:10]

        sql = 'select * from cve where update_time >='+'\''+start_date+'\''+' and update_time <= '+'\''+end_date+'\''
        cursor = Connect()
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("count cve vulnerability of this time: "+str(len(rows)))
        print('----31-----',len(rows))

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


def getCnvd():
    pass

def getinstance():
    pass

def getAttack():
    pass
