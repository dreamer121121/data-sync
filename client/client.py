import requests
import os.path
import urllib.parse
import datetime
import time
from cli_config import TIME,DATABASES,FIRST_TIME
import logging.config
import re



logging_config = os.path.join(os.path.dirname(__file__), 'logging.conf')#logging.conf路径
logging.config.fileConfig(logging_config)
logger = logging.getLogger('root')
# 记录拉取历史

def _write_in_history(now):

    f = open('history.txt', 'w')
    f.write("本次拉取时间："+str(now))
    f.close()

def get_lasttime():
    f = open('history.txt','r')
    lastime = f.readlines()
    f.close()
    if not lastime:
        lastime = FIRST_TIME #第一次拉取
    else:
        lastime = lastime[-1]
        lastime = re.search('(\d+.*) ' ,lastime).group(0)
        print('----32----',lastime)
    return lastime

def _create_params(lastime,now):
    json = {}
    json['from'] = lastime
    json['to'] = now
    return json

def _create_url(url,json):
    params = urllib.parse.urlencode(json)
    url += params
    return url

def pull_data():

    error_db_info = ''
    base_urls = DATABASES
    now = datetime.datetime.now()
    date = str(now)[0:10]
    lastime = get_lasttime()
    params = _create_params(lastime,date)

    try:
        for base_url in base_urls:
            error_db_info = base_url
            url = _create_url(base_url,params)
            logger.info("INFO begin pull data from: "+url[25:36])
            content = requests.get(url).json()#调API

            # f1=open("results.txt",'w')
            # f1.write(content[0:9])
            # f1.close()
            logger.info("INFO finish  "+base_url[25:36])

        logger.info("INFO  finish pull all database")
        _write_in_history(now)  # 写入历史记录

    except Exception as e:
        logger.error("Error get "+error_db_info[25:36]+':%s'%e)
        logger.error("Error pull data failed this time !!!")


def insert_data():
    pass

if __name__ == '__main__':

    if not os.path.exists('history.txt'):
        f = open('history.txt', 'w')
        f.close()

    while True:
        pull_data()
        logger.info("INFO start sleep")
        time.sleep(TIME)  # //完成一次拉取开始休眠
