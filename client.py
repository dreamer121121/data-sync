import requests
import urllib.parse
import datetime
import time
from config import TIME,DATABASES,FIRST_TIME
import logging
import re


# 记录拉取历史

def _write_in_history(now):

    f = open('history.txt', 'a+')
    f.write("本次拉取时间："+str(now))
    f.close()

def get_lasttime():
    f = open('history.txt','r')
    lastime = f.readlines()
    if not lastime:
        lastime = FIRST_TIME #第一次爬取
    else:
        lastime = lastime[-1]
        lastime = re.search('(\d+.*) ' ,lastime).group(0)
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
    urls = DATABASES
    now = datetime.datetime.now()
    lastime = get_lasttime()
    params = _create_params(lastime,now)

    for url in urls:
        url = _create_url(url,params)
        print('----url----',url)
        content = requests.get(url).text #调API
        f1 = open('results.txt','w',encoding='utf-8')
        f1.write(content)
        f1.close()

    _write_in_history(now) #写入历史记录
    print('----完成一次拉取-----')
    time.sleep(TIME)  # //完成一次拉取开始休眠

def insert_data():
    pass

if __name__ == '__main__':
    while True:
        pull_data()
