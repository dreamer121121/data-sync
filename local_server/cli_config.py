import pymysql
from http.server import HTTPServer, BaseHTTPRequestHandler
import json,urllib.parse


"""配置数据库"""
conn = pymysql.connect(user='root',database='ics',password='123456')

"""配置本地服务器"""
data = {'result': 'this is a test'}
host = ('localhost', 8888)

"""配置数据同步默认参数"""

# 配置拉取数据的时间
TIME = 60
#配置远程服务器地址
REMOTE_ADDRS = 'http://192.168.1.40:8000/api/get/'
# 配置拉取的数据库
DATABASES = ['Cve']
#第一次拉取开始日期（给客户安装数据库的时间而定）
FIRST_TIME = '2016-01-01'

params = {'TIME':TIME,'REMOTE_ADDRS':REMOTE_ADDRS,'DATABASES':DATABASES,'FIRST_TIME':FIRST_TIME}


class Resquest(BaseHTTPRequestHandler):

    """
    用于接收客户端发送的请求
    更改数据同步的配置参数
    """
    def do_GET(self):

        try:
            if '?' in self.path:
                self.queryList = urllib.parse.unquote(self.path.split('?', 1)[1])
                self.queryList = self.queryList.split('&')
                for item in self.queryList:
                    key,value = item.split('=')
                    if key == 'DATABASES':
                        db_list = value.split('=')
                        params[key] = db_list
                    elif key == 'REMOTE_ADDRS':
                        params['REMOTE_ADDRS'] = 'http://'+value+"8000"+'/api/get/'
                    else:
                        if params[key] != value:
                            params[key] = value

                #写入文件
                f = open('config_params.txt','w')
                f.write(json.dumps(params))
                f.close()

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
        except:
            msg={'error':'config failed'}
            self.wfile.write(json.dumps(msg))

if __name__ == '__main__':

    """将默认数据同步参数写入文件"""
    f = open('config_params.txt', 'w')
    f.write(json.dumps(params))
    f.close()

    """启动本地服务器"""
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()