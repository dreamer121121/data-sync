# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 362)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(750, 362))
        MainWindow.setMaximumSize(QtCore.QSize(750, 362))
        MainWindow.setStyleSheet("#MainWindow {background-color: rgb(255, 255, 255);}")
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 361))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(35, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(35, 110, 91, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(35, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(35, 230, 91, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 110, 113, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 230, 131, 20))
        self.lineEdit_4.setCursorPosition(19)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(160, 160, 71, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 160, 71, 16))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(160, 190, 71, 16))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(270, 60, 31, 20))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(35, 20, 10, 15))
        self.line_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.line_2.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(250, 320, 60, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(220, 190, 101, 16))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setGeometry(QtCore.QRect(370, 0, 381, 361))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 60, 89, 16))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(35, 90, 81, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(35, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(140, 120, 135, 16))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(35, 20, 10, 15))
        self.line_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.line_4.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(120, 90, 135, 20))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(35, 150, 91, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(35, 180, 81, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(130, 150, 135, 16))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 320, 60, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(35, 240, 81, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(110, 250, 231, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(130, 60, 89, 16))
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 180, 231, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.line = QtWidgets.QFrame(MainWindow)
        self.line.setGeometry(QtCore.QRect(350, 10, 20, 291))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.config)
        self.pushButton_2.clicked.connect(MainWindow.get_config)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "data-sync-client"))
        self.label_3.setText(_translate("MainWindow", "数据同步时间间隔"))
        self.label_4.setText(_translate("MainWindow", "远程服务器地址"))
        self.label_5.setText(_translate("MainWindow", "同步的数据库"))
        self.label_6.setText(_translate("MainWindow", "首次同步日期"))
        self.lineEdit_4.setText(_translate("MainWindow", "2019-01-01 00:00:00"))
        self.checkBox.setText(_translate("MainWindow", "Cve"))
        self.checkBox_2.setText(_translate("MainWindow", "Cnvd"))
        self.checkBox_3.setText(_translate("MainWindow", "Attack"))
        self.label_7.setText(_translate("MainWindow", "小时"))
        self.label.setText(_translate("MainWindow", "数据同步参数配置"))
        self.pushButton.setText(_translate("MainWindow", "config"))
        self.checkBox_4.setText(_translate("MainWindow", "Instance_info"))
        self.radioButton_2.setText(_translate("MainWindow", "错误"))
        self.label_2.setText(_translate("MainWindow", "系统运行状态"))
        self.label_8.setText(_translate("MainWindow", "上次同步时间："))
        self.label_10.setText(_translate("MainWindow", "同步时间间隔(h)："))
        self.label_13.setText(_translate("MainWindow", "远程服务器地址："))
        self.label_14.setText(_translate("MainWindow", "同步数据表："))
        self.pushButton_2.setText(_translate("MainWindow", "status"))
        self.label_17.setText(_translate("MainWindow", "错误信息："))
        self.radioButton_3.setText(_translate("MainWindow", "正常"))

