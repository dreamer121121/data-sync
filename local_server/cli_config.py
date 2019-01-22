import pymysql
from http.server import HTTPServer, BaseHTTPRequestHandler
import json,urllib.parse,os




"""配置数据库"""

DATABASES = {
    'ics': {
        'NAME': 'ics',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'ics_scan': {
        'NAME': 'ics_scan',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}


"""配置本地服务器"""
config_result = 'success'
host = ('localhost', 8888)

"""配置数据同步默认参数"""

# 配置拉取数据的时间
TIME = 60
#配置远程服务器地址
REMOTE_ADDRS = 'http://192.168.1.40:8000/api/get/'
# 配置拉取的数据库
TABLES = ['Cve','Vulnerability','Dev2vul','Conpot_log','Instance','Instanceport']
#第一次拉取开始日期（给客户安装数据库的时间而定）
FIRST_TIME = '2019-01-01 00:00:00'

params = {'TIME':TIME,'REMOTE_ADDRS':REMOTE_ADDRS,'TABLES':TABLES,'FIRST_TIME':FIRST_TIME}


def get_lasttime():
    """
    get lasttime history
    :return:
    """
    if not os.path.exists('success_history.txt'):
        f = open('success_history.txt', 'w')
        f.close()

    f = open('success_history.txt','r')
    lastime = f.readlines()
    f.close()
    if not lastime:
        lastime = FIRST_TIME #只用于第一次同步时使用这一参数（用户不可更改公司根据给客户安装的数据库的日期进行更改）
    else:
        lastime = lastime[-1]
        print('----32----',lastime)
    return lastime

class Resquest(BaseHTTPRequestHandler):

    """
    用于接收客户端发送的请求
    更改数据同步的配置参数
    """
    def do_GET(self):
        try:
            if '?' in self.path:#配置接口
                self.queryList = urllib.parse.unquote(self.path.split('?', 1)[1])
                self.queryList = self.queryList.split('&')
                for item in self.queryList:
                    key,value = item.split('=')
                    if key == 'TABLES':
                        db_list = value.split(',')
                        params[key] = db_list
                    elif key == 'REMOTE_ADDRS':
                        params['REMOTE_ADDRS'] = 'http://'+value+":8000"+'/api/get/'
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
                status = {}
                status['result'] = config_result
                print('-----97----',status)
                self.wfile.write(json.dumps(status).encode())

            else:#查询接口
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                print('-----查询接口-----')
                status_message = self.get_return_message()
                print('----103----',type(status_message))
                print(status_message)
                self.wfile.write(json.dumps(status_message).encode())


        except:
            msg={'error':'failed'}
            self.wfile.write(json.dumps(msg).encode())


    def get_return_message(self):
        status_message = {}
        self.lastime = get_lasttime()
        status_message['lastime'] = self.lastime
        f = open('config_params.txt')
        params = json.loads(f.read())
        status_message['TIME'] = params['TIME']
        status_message['REMOTE_ADDRS'] = params['REMOTE_ADDRS']
        status_message['TABLES'] = params['TABLES']
        print(status_message)
        return  status_message




if __name__ == '__main__':

    """将默认数据同步参数写入配置文件"""
    f = open('config_params.txt', 'w')
    f.write(json.dumps(params))
    f.close()

    """启动本地服务器"""
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()