from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from Login import Ui_Login_MainWindow
from UI_mainwindow import Ui_main_MainWindow
from aip import AipSpeech
import sys
import requests
import os
from config import local_server
import datetime

# """ 语音播报信息"""
# APP_ID = '14442796'
# API_KEY = 'FraivQGZbx1HWSyFKoYMFA18'
# SECRET_KEY = 'EPf7caqa68hHDk2doE06Y643D2kuZGfl'
#
# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# speech_msg = '欢迎使用北京睿航至臻科技有限公司数据同步客户端'
# result  = client.synthesis(speech_msg, 'zh', 1, {
#     'vol': 5,'per':0
# })
# if not isinstance(result, dict):
#     with open('auido.mp3', 'wb') as f:
#         f.write(result)

class Main_Window(QMainWindow, Ui_main_MainWindow):

    def __init__(self):
        super(Main_Window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)
        # cmd = 'auido.mp3'
        # os.system(cmd)

    def config(self):
        TIME = self.lineEdit.text()
        REMOTE_ADDRS = self.lineEdit_2.text()
        FIRST_TIME = self.lineEdit_4.text()
        TABLES = ''
        if self.checkBox:
            TABLES += 'Cve,'
        if self.checkBox_2:
            TABLES += 'Vulnerability,Ddev2vul,'
        if self.checkBox_3:
            TABLES += 'Conpot_log'
        url = local_server+'TIME='+TIME+'&REMOTE_ADDRS='+REMOTE_ADDRS+'&TABLES='+TABLES+'&FIRST_TIME='+FIRST_TIME
        print('-----url----',url)
        content = requests.get(url).json()
        print('----47-----',content)
        if content['result'] == 'success':
            message = '参数配置成功'
            QMessageBox.information(self, "Message", message)

            # #显示系统状态信息
            # self.label_12.setText(content['lastime'])
            # time_span = self.lineEdit.text

            # currentTime = content['lasttime']
            # temp =  datetime.datetime.strptime(currentTime, '%Y-%m-%d %H:%M:%S')
            # print(temp)
            # print(currentTime)
            # self.label_11.setText(datetime.datetime.)

        elif content['result'] == 'failed':
            message = '配置失败'
            QMessageBox.information(self, "Message", message)


    def get_config(self):
        url = local_server.strip('?')
        params = requests.get(url).json()
        self.label_12.setText(params['lastime'])
        self.label_11.setText(str(params['TIME']))
        self.label_15.setText(params['REMOTE_ADDRS'][7:18])
        tables = ''
        for table in params['TABLES']:
            table = table.strip('\'')
            tables += table
            tables += ','
        self.label_16.setText(tables)


class Login_Window(QMainWindow, Ui_Login_MainWindow):
    def __init__(self):
        super(Login_Window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)

    def slot1(self):
        if self.lineEdit.text() == 'rhzz' and self.lineEdit_2.text() == '1234.com':
            self.hide()
            self.main = Main_Window()
            self.main.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login_Window()  # 初始化
    login_window.show()
    sys.exit(app.exec_())
