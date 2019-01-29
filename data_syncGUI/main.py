from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from PyQt5 import QtMultimedia,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from Login import Ui_Login_MainWindow
from UI_mainwindow import Ui_main_MainWindow
from aip import AipSpeech
import sys
import requests
import os,re
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

    def checkip(self):
        p = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if p.match(self.lineEdit_2.text()) and self.lineEdit_2.text() != '':
            return True
        else:
            return False


    def config(self):
        try:
            if self.lineEdit.text():
                TIME = self.lineEdit.text()
            else:
                TIME = '24'

            if self.checkip():
                REMOTE_ADDRS = self.lineEdit_2.text()
            else:
                REMOTE_ADDRS = '192.168.1.40'

            FIRST_TIME = self.lineEdit_4.text()
            TABLES = ''
            if self.checkBox:
                TABLES += 'Cve,'
            if self.checkBox_2:
                TABLES += 'Vulnerability,Dev2vul,'
            if self.checkBox_3:
                TABLES += 'Conpot_log,'
            if self.checkBox_4:
                TABLES += 'Instance,Instanceport'
            url = local_server+'TIME='+TIME+'&REMOTE_ADDRS='+REMOTE_ADDRS+'&TABLES='+TABLES+'&FIRST_TIME='+FIRST_TIME

            content = requests.get(url).json()
            if content['result'] == 'success':
                message = '参数配置成功'
                QMessageBox.information(self, "Message", message)

            elif content['result'] == 'failed':
                message = '配置失败'
                QMessageBox.information(self, "Message", message)

        except Exception as e:
            msg = str(e)
            QMessageBox.information(self,"Error",msg)

    def get_config(self):
        try:
            url = local_server.strip('?')
            params = requests.get(url,timeout=5).json()

            if params['IFERROR']:
                self.radioButton_2.setChecked(True)
                self.textBrowser.setText(params['IFERROR'])
            else:
                self.radioButton_3.setChecked(True)
            self.label_12.setText(params['lastime'])
            self.label_11.setText(str(params['TIME']))
            self.label_15.setText(params['REMOTE_ADDRS'][7:18])

            tables = ''
            for table in params['TABLES']:
                table = table.strip('\'')
                tables += table
                tables += ','
            self.textBrowser_2.setText(tables)
        except Exception as e:
            msg = str(e)
            QMessageBox.information(self,"Error",msg)



class Login_Window(QMainWindow, Ui_Login_MainWindow):

    def __init__(self):
        super(Login_Window, self).__init__()  # 通过这句话就可以调用其父类的属性和方法
        self.setupUi(self)
        self.lineEdit.setToolTip("请输入用户名，默认为rhzz")
        self.lineEdit_2.setToolTip("请输入密码，默认为1234.com")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))#设置鼠标图标变为手型
        self.pushButton.pressed.connect(self.pushButton_pressed)
        self.pushButton.released.connect(self.pushbutton_released)
        self.status = self.statusBar()
        self.status.showMessage('Copyright © 2018 - 现在 睿航至臻 版权所有')
        self.status.setStyleSheet("color: gray")


        """语音提示尚未成功"""
        # player = QtMultimedia.QMediaPlayer()
        #
        # player.setVolume(100)
        # playlist = QtMultimedia.QMediaPlaylist()
        # playlist.addMedia(
        #     QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(r"C:\Users\Tao xia\Desktop\data-sync\data_syncGUI\audio.mp3")))
        # playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.CurrentItemInLoop)
        # player.setPlaylist(playlist)
        # player.play()

    def slot1(self):

        if self.lineEdit.text() == 'rhzz' and self.lineEdit_2.text() == '1234.com':
            self.hide()
            self.main = Main_Window()
            self.main.show()
        else:
            QMessageBox.information(self,'Error','用户名或密码错误')
            self.lineEdit.clear()
            self.lineEdit_2.clear()


    def pushButton_pressed(self):

        self.pushButton.setStyleSheet("background-color: rgb(44, 171, 206);\n"
                                      "color: rgb(221, 46, 57);")


    def pushbutton_released(self):
        self.pushButton.setStyleSheet("background-color: rgb(44, 171, 206);\n"
                                      "color: rgb(255, 255, 255);")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login_Window()  # 初始化
    login_window.show()
    sys.exit(app.exec_())
