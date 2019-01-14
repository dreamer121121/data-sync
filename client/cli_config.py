import pymysql
# 配置拉取数据的时间
TIME = 60
#配置远程服务器地址
REMOTE_ADDRS = 'http://192.168.1.40:8000/api/get/'
# 配置拉取的数据库
DATABASES = ['Cve']
#第一次拉取开始日期（给客户安装数据库的时间而定）
FIRST_TIME = '2016-01-01'
#连接本地数据库
conn = pymysql.connect(user='root',database='ics',password='123456')
