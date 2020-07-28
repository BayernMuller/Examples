# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'farm_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 480)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TitleBar = QtWidgets.QLabel(Form)
        self.TitleBar.setGeometry(QtCore.QRect(0, 430, 800, 50))
        self.TitleBar.setStyleSheet("background-color: rgb(0, 135, 68);\n"
"font: 81 25pt \"나눔스퀘어 ExtraBold\";\n"
"color: white\n"
"")
        self.TitleBar.setObjectName("TitleBar")
        self.MainBtn = QtWidgets.QPushButton(Form)
        self.MainBtn.setGeometry(QtCore.QRect(320, 438, 110, 34))
        self.MainBtn.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    font: 75 15pt \"나눔스퀘어 ExtraBold\";\n"
"    color: rgb(0, 135, 68);  \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:focus:checked\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}")
        self.MainBtn.setCheckable(True)
        self.MainBtn.setChecked(True)
        self.MainBtn.setAutoRepeat(False)
        self.MainBtn.setAutoExclusive(False)
        self.MainBtn.setAutoDefault(False)
        self.MainBtn.setObjectName("MainBtn")
        self.GraphBtn = QtWidgets.QPushButton(Form)
        self.GraphBtn.setGeometry(QtCore.QRect(440, 438, 110, 34))
        self.GraphBtn.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    font: 75 15pt \"나눔스퀘어 ExtraBold\";\n"
"    color: rgb(0, 135, 68);  \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:focus:checked\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}")
        self.GraphBtn.setCheckable(True)
        self.GraphBtn.setObjectName("GraphBtn")
        self.SetBtn = QtWidgets.QPushButton(Form)
        self.SetBtn.setGeometry(QtCore.QRect(680, 438, 110, 34))
        self.SetBtn.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    font: 75 15pt \"나눔스퀘어 ExtraBold\";\n"
"    color: rgb(0, 135, 68);  \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:focus:checked\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}")
        self.SetBtn.setCheckable(True)
        self.SetBtn.setObjectName("SetBtn")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -1, 800, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.TempLabel = QtWidgets.QLabel(self.MainPage)
        self.TempLabel.setGeometry(QtCore.QRect(30, 80, 177, 30))
        self.TempLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: white;")
        self.TempLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.TempLabel.setObjectName("TempLabel")
        self.Temp = QtWidgets.QLabel(self.MainPage)
        self.Temp.setGeometry(QtCore.QRect(60, 70, 200, 120))
        self.Temp.setStyleSheet("font: 81 60pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF;\n"
"background-color: rgb(0, 135, 68);\n"
"border-radius: 30px;")
        self.Temp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Temp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Temp.setLineWidth(1)
        self.Temp.setMidLineWidth(0)
        self.Temp.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Temp.setObjectName("Temp")
        self.Humi = QtWidgets.QLabel(self.MainPage)
        self.Humi.setGeometry(QtCore.QRect(300, 70, 200, 120))
        self.Humi.setStyleSheet("font: 81 60pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF;\n"
"background-color: rgb(0, 135, 68);\n"
"border-radius: 30px;")
        self.Humi.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Humi.setObjectName("Humi")
        self.HumiLabel = QtWidgets.QLabel(self.MainPage)
        self.HumiLabel.setGeometry(QtCore.QRect(320, 80, 71, 30))
        self.HumiLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: white;")
        self.HumiLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.HumiLabel.setObjectName("HumiLabel")
        self.PhLabel = QtWidgets.QLabel(self.MainPage)
        self.PhLabel.setGeometry(QtCore.QRect(550, 80, 51, 30))
        self.PhLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: white;")
        self.PhLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.PhLabel.setObjectName("PhLabel")
        self.Ph = QtWidgets.QLabel(self.MainPage)
        self.Ph.setGeometry(QtCore.QRect(540, 70, 200, 120))
        self.Ph.setStyleSheet("font: 81 60pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF;\n"
"background-color: rgb(0, 135, 68);\n"
"border-radius: 30px;")
        self.Ph.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Ph.setObjectName("Ph")
        self.CdsLabel = QtWidgets.QLabel(self.MainPage)
        self.CdsLabel.setGeometry(QtCore.QRect(40, 250, 150, 30))
        self.CdsLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: white;")
        self.CdsLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.CdsLabel.setObjectName("CdsLabel")
        self.Cds = QtWidgets.QLabel(self.MainPage)
        self.Cds.setGeometry(QtCore.QRect(60, 240, 200, 120))
        self.Cds.setStyleSheet("font: 81 60pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF;\n"
"background-color: rgb(0, 135, 68);\n"
"border-radius: 30px;")
        self.Cds.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Cds.setObjectName("Cds")
        self.DoLabel = QtWidgets.QLabel(self.MainPage)
        self.DoLabel.setGeometry(QtCore.QRect(523, 250, 131, 31))
        self.DoLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: white;")
        self.DoLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.DoLabel.setObjectName("DoLabel")
        self.Do = QtWidgets.QLabel(self.MainPage)
        self.Do.setGeometry(QtCore.QRect(540, 240, 200, 120))
        self.Do.setStyleSheet("font: 81 60pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF;\n"
"background-color: rgb(0, 135, 68);\n"
"border-radius: 30px;")
        self.Do.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Do.setObjectName("Do")
        self.Tds = QtWidgets.QLabel(self.MainPage)
        self.Tds.setGeometry(QtCore.QRect(300, 240, 200, 120))
        self.Tds.setStyleSheet("font: 81 60pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF;\n"
"background-color: rgb(0, 135, 68);\n"
"border-radius: 30px;")
        self.Tds.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Tds.setObjectName("Tds")
        self.TdsLabel = QtWidgets.QLabel(self.MainPage)
        self.TdsLabel.setGeometry(QtCore.QRect(280, 250, 151, 30))
        self.TdsLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: white;")
        self.TdsLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.TdsLabel.setObjectName("TdsLabel")
        self.Ph.raise_()
        self.PhLabel.raise_()
        self.Temp.raise_()
        self.Cds.raise_()
        self.TempLabel.raise_()
        self.Humi.raise_()
        self.HumiLabel.raise_()
        self.CdsLabel.raise_()
        self.Do.raise_()
        self.Tds.raise_()
        self.TdsLabel.raise_()
        self.DoLabel.raise_()
        self.stackedWidget.addWidget(self.MainPage)
        self.GraphPage = QtWidgets.QWidget()
        self.GraphPage.setObjectName("GraphPage")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.GraphPage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 761, 36))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TempCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.TempCheck.setStyleSheet("font: 13pt \"나눔스퀘어\";\n"
"color: #FF0000")
        self.TempCheck.setChecked(True)
        self.TempCheck.setObjectName("TempCheck")
        self.horizontalLayout_2.addWidget(self.TempCheck)
        self.HumiCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.HumiCheck.setStyleSheet("font: 13pt \"나눔스퀘어\";\n"
"color: #0000FF")
        self.HumiCheck.setChecked(True)
        self.HumiCheck.setObjectName("HumiCheck")
        self.horizontalLayout_2.addWidget(self.HumiCheck)
        self.CdsCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.CdsCheck.setStyleSheet("font: 13pt \"나눔스퀘어\"; color: #00FF00")
        self.CdsCheck.setChecked(True)
        self.CdsCheck.setObjectName("CdsCheck")
        self.horizontalLayout_2.addWidget(self.CdsCheck)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.MonthRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.MonthRadio.setStyleSheet("font: 13pt \"나눔스퀘어\";")
        self.MonthRadio.setObjectName("MonthRadio")
        self.horizontalLayout_2.addWidget(self.MonthRadio)
        self.WeekRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.WeekRadio.setStyleSheet("font: 13pt \"나눔스퀘어\";")
        self.WeekRadio.setObjectName("WeekRadio")
        self.horizontalLayout_2.addWidget(self.WeekRadio)
        self.DayRadio = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.DayRadio.setStyleSheet("font: 13pt \"나눔스퀘어\";")
        self.DayRadio.setObjectName("DayRadio")
        self.horizontalLayout_2.addWidget(self.DayRadio)
        self.Graph = PlotWidget(self.GraphPage)
        self.Graph.setGeometry(QtCore.QRect(-1, 36, 802, 395))
        self.Graph.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Graph.setObjectName("Graph")
        self.stackedWidget.addWidget(self.GraphPage)
        self.ActuatorPage = QtWidgets.QWidget()
        self.ActuatorPage.setObjectName("ActuatorPage")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.ActuatorPage)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 80, 721, 271))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Fan = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.Fan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fan.setObjectName("Fan")
        self.label = QtWidgets.QLabel(self.Fan)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 181))
        self.label.setStyleSheet("background-color: rgb(0, 135, 68);\n"
"border-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Fan)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 191, 111))
        self.label_2.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 35px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Fan)
        self.label_3.setGeometry(QtCore.QRect(0, 130, 191, 51))
        self.label_3.setStyleSheet("background-color: rgb(0, 135, 68);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.FanAuto = QtWidgets.QCheckBox(self.Fan)
        self.FanAuto.setGeometry(QtCore.QRect(45, 205, 91, 31))
        self.FanAuto.setStyleSheet("font: 81 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: #008744")
        self.FanAuto.setObjectName("FanAuto")
        self.label_10 = QtWidgets.QLabel(self.Fan)
        self.label_10.setGeometry(QtCore.QRect(40, 30, 111, 121))
        self.label_10.setStyleSheet("border-image: url(:/image/fan.jpg);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.Fan)
        self.Light = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.Light.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Light.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Light.setObjectName("Light")
        self.label_4 = QtWidgets.QLabel(self.Light)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 191, 181))
        self.label_4.setStyleSheet("background-color: rgb(0, 135, 68);\n"
"border-radius: 50px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Light)
        self.label_5.setGeometry(QtCore.QRect(0, 150, 191, 111))
        self.label_5.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 35px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Light)
        self.label_6.setGeometry(QtCore.QRect(0, 130, 191, 51))
        self.label_6.setStyleSheet("background-color: rgb(0, 135, 68);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.LedAuto = QtWidgets.QCheckBox(self.Light)
        self.LedAuto.setGeometry(QtCore.QRect(45, 205, 91, 31))
        self.LedAuto.setStyleSheet("font: 81 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: #008744")
        self.LedAuto.setObjectName("LedAuto")
        self.label_11 = QtWidgets.QLabel(self.Light)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 111, 121))
        self.label_11.setStyleSheet("border-image: url(:/image/bulb.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.Light)
        self.Water = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.Water.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Water.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Water.setObjectName("Water")
        self.label_7 = QtWidgets.QLabel(self.Water)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 191, 181))
        self.label_7.setStyleSheet("background-color: rgb(0, 135, 68);\n"
"border-radius: 50px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Water)
        self.label_8.setGeometry(QtCore.QRect(0, 150, 191, 111))
        self.label_8.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 35px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Water)
        self.label_9.setGeometry(QtCore.QRect(0, 130, 191, 51))
        self.label_9.setStyleSheet("background-color: rgb(0, 135, 68);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.WaterAuto = QtWidgets.QCheckBox(self.Water)
        self.WaterAuto.setGeometry(QtCore.QRect(45, 205, 91, 31))
        self.WaterAuto.setStyleSheet("font: 81 20pt \"나눔스퀘어 ExtraBold\";\n"
"color: #008744")
        self.WaterAuto.setObjectName("WaterAuto")
        self.label_12 = QtWidgets.QLabel(self.Water)
        self.label_12.setGeometry(QtCore.QRect(40, 30, 111, 121))
        self.label_12.setStyleSheet("border-image: url(:/image/water.jpg);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.Water)
        self.stackedWidget.addWidget(self.ActuatorPage)
        self.SettingPage = QtWidgets.QWidget()
        self.SettingPage.setObjectName("SettingPage")
        self.label_13 = QtWidgets.QLabel(self.SettingPage)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 391, 180))
        self.label_13.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 30px;\n"
"font: 15pt \"나눔스퀘어 Bold\";\n"
"color: #008744")
        self.label_13.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.SettingPage)
        self.label_14.setGeometry(QtCore.QRect(20, 230, 391, 180))
        self.label_14.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 30px;\n"
"font: 15pt \"나눔스퀘어 Bold\";\n"
"color: #008744")
        self.label_14.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(self.SettingPage)
        self.comboBox.setGeometry(QtCore.QRect(155, 73, 121, 22))
        self.comboBox.setStyleSheet("border: 2px solid #008744")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.SettingPage)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 110, 101, 41))
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 2px solid #008744;\n"
"border-radius: 20px;\n"
"font: 25 12pt \"나눔스퀘어 Light\";\n"
"color: #008744;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.SettingPage)
        self.pushButton.setGeometry(QtCore.QRect(220, 110, 101, 41))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 2px solid #008744;\n"
"border-radius: 20px;\n"
"font: 25 12pt \"나눔스퀘어 Light\";\n"
"color: #008744;")
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(self.SettingPage)
        self.spinBox.setGeometry(QtCore.QRect(160, 170, 61, 21))
        self.spinBox.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")
        self.label_18 = QtWidgets.QLabel(self.SettingPage)
        self.label_18.setGeometry(QtCore.QRect(120, 170, 31, 16))
        self.label_18.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_18.setObjectName("label_18")
        self.pushButton_3 = QtWidgets.QPushButton(self.SettingPage)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 170, 71, 21))
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid #008744;\n"
"border-radius: 10px;\n"
"font: 25 12pt \"나눔스퀘어 Light\";\n"
"color: #008744;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.SettingPage)
        self.lineEdit.setGeometry(QtCore.QRect(140, 270, 181, 31))
        self.lineEdit.setStyleSheet("border: 2px solid #008744;\n"
"border-radius: 5px;\n"
"font: 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.SettingPage)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 310, 101, 31))
        self.lineEdit_2.setStyleSheet("border: 2px solid #008744;\n"
"border-radius: 5px;\n"
"font: 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_19 = QtWidgets.QLabel(self.SettingPage)
        self.label_19.setGeometry(QtCore.QRect(110, 278, 21, 16))
        self.label_19.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.SettingPage)
        self.label_20.setGeometry(QtCore.QRect(92, 317, 41, 16))
        self.label_20.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_20.setObjectName("label_20")
        self.pushButton_4 = QtWidgets.QPushButton(self.SettingPage)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 315, 71, 21))
        self.pushButton_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid #008744;\n"
"border-radius: 10px;\n"
"font: 25 12pt \"나눔스퀘어 Light\";\n"
"color: #008744;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.SettingPage)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 360, 71, 21))
        self.pushButton_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid #008744;\n"
"border-radius: 10px;\n"
"font: 25 12pt \"나눔스퀘어 Light\";\n"
"color: #008744;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_21 = QtWidgets.QLabel(self.SettingPage)
        self.label_21.setGeometry(QtCore.QRect(130, 360, 31, 16))
        self.label_21.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_21.setObjectName("label_21")
        self.spinBox_2 = QtWidgets.QSpinBox(self.SettingPage)
        self.spinBox_2.setGeometry(QtCore.QRect(170, 360, 61, 21))
        self.spinBox_2.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(60)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.SettingPage)
        self.spinBox_3.setGeometry(QtCore.QRect(570, 60, 61, 21))
        self.spinBox_3.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744")
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(99)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_22 = QtWidgets.QLabel(self.SettingPage)
        self.label_22.setGeometry(QtCore.QRect(530, 60, 31, 16))
        self.label_22.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_22.setObjectName("label_22")
        self.label_16 = QtWidgets.QLabel(self.SettingPage)
        self.label_16.setGeometry(QtCore.QRect(420, 160, 359, 120))
        self.label_16.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 30px;\n"
"font: 15pt \"나눔스퀘어 Bold\";\n"
"color: #008744")
        self.label_16.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.SettingPage)
        self.label_17.setGeometry(QtCore.QRect(420, 290, 359, 120))
        self.label_17.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 30px;\n"
"font: 15pt \"나눔스퀘어 Bold\";\n"
"color: #008744")
        self.label_17.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.label_15 = QtWidgets.QLabel(self.SettingPage)
        self.label_15.setGeometry(QtCore.QRect(420, 30, 359, 120))
        self.label_15.setStyleSheet("border: 3px solid #008744;\n"
"border-radius: 30px;\n"
"font: 15pt \"나눔스퀘어 Bold\";\n"
"color: #008744")
        self.label_15.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.label_23 = QtWidgets.QLabel(self.SettingPage)
        self.label_23.setGeometry(QtCore.QRect(640, 60, 31, 16))
        self.label_23.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.SettingPage)
        self.label_24.setGeometry(QtCore.QRect(640, 90, 31, 16))
        self.label_24.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_24.setObjectName("label_24")
        self.spinBox_4 = QtWidgets.QSpinBox(self.SettingPage)
        self.spinBox_4.setGeometry(QtCore.QRect(570, 90, 61, 21))
        self.spinBox_4.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744")
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(99)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_25 = QtWidgets.QLabel(self.SettingPage)
        self.label_25.setGeometry(QtCore.QRect(530, 90, 31, 16))
        self.label_25.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.pushButton_6 = QtWidgets.QPushButton(self.SettingPage)
        self.pushButton_6.setGeometry(QtCore.QRect(565, 118, 71, 21))
        self.pushButton_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid #008744;\n"
"border-radius: 10px;\n"
"font: 25 12pt \"나눔스퀘어 Light\";\n"
"color: #008744;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_26 = QtWidgets.QLabel(self.SettingPage)
        self.label_26.setGeometry(QtCore.QRect(640, 220, 31, 16))
        self.label_26.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_26.setObjectName("label_26")
        self.spinBox_5 = QtWidgets.QSpinBox(self.SettingPage)
        self.spinBox_5.setGeometry(QtCore.QRect(570, 220, 61, 21))
        self.spinBox_5.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744")
        self.spinBox_5.setMinimum(0)
        self.spinBox_5.setMaximum(99)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.SettingPage)
        self.spinBox_6.setGeometry(QtCore.QRect(570, 190, 61, 21))
        self.spinBox_6.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744")
        self.spinBox_6.setMinimum(0)
        self.spinBox_6.setMaximum(99)
        self.spinBox_6.setObjectName("spinBox_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.SettingPage)
        self.pushButton_7.setGeometry(QtCore.QRect(565, 248, 71, 21))
        self.pushButton_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid #008744;\n"
"border-radius: 10px;\n"
"font: 25 12pt \"나눔스퀘어 Light\";\n"
"color: #008744;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_27 = QtWidgets.QLabel(self.SettingPage)
        self.label_27.setGeometry(QtCore.QRect(640, 190, 31, 16))
        self.label_27.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.SettingPage)
        self.label_28.setGeometry(QtCore.QRect(530, 220, 31, 16))
        self.label_28.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.SettingPage)
        self.label_29.setGeometry(QtCore.QRect(530, 190, 31, 16))
        self.label_29.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_29.setObjectName("label_29")
        self.timeEdit = QtWidgets.QTimeEdit(self.SettingPage)
        self.timeEdit.setGeometry(QtCore.QRect(540, 330, 118, 22))
        self.timeEdit.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744;\n"
"font: 9pt \"나눔스퀘어\";\n"
"color: #008744")
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.SettingPage)
        self.timeEdit_2.setGeometry(QtCore.QRect(540, 370, 118, 22))
        self.timeEdit_2.setStyleSheet("border-radius: 4px;\n"
"border: 1px solid #008744;\n"
"font: 9pt \"나눔스퀘어\";\n"
"color: #008744")
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_30 = QtWidgets.QLabel(self.SettingPage)
        self.label_30.setGeometry(QtCore.QRect(500, 372, 31, 16))
        self.label_30.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.SettingPage)
        self.label_31.setGeometry(QtCore.QRect(510, 332, 21, 16))
        self.label_31.setStyleSheet("font: 75 11pt \"나눔스퀘어\";\n"
"color: #008744")
        self.label_31.setObjectName("label_31")
        self.label_15.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.comboBox.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.spinBox.raise_()
        self.label_18.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_21.raise_()
        self.spinBox_2.raise_()
        self.spinBox_3.raise_()
        self.label_22.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.spinBox_4.raise_()
        self.label_25.raise_()
        self.pushButton_6.raise_()
        self.label_26.raise_()
        self.spinBox_5.raise_()
        self.spinBox_6.raise_()
        self.pushButton_7.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.timeEdit.raise_()
        self.timeEdit_2.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.stackedWidget.addWidget(self.SettingPage)
        self.ActBtn = QtWidgets.QPushButton(Form)
        self.ActBtn.setGeometry(QtCore.QRect(560, 438, 110, 34))
        self.ActBtn.setStyleSheet("QPushButton\n"
"{ \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    font: 75 15pt \"나눔스퀘어 ExtraBold\";\n"
"    color: rgb(0, 135, 68);  \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:focus:checked\n"
"{ \n"
"    background-color: rgb(0, 0, 0, 0%);\n"
"    border: 3px solid white;\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ActBtn.setCheckable(True)
        self.ActBtn.setAutoExclusive(True)
        self.ActBtn.setObjectName("ActBtn")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(3, 433, 45, 45))
        self.logo.setStyleSheet("border-image: url(:/image/leaf.jpg);")
        self.logo.setText("")
        self.logo.setObjectName("logo")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TitleBar.setText(_translate("Form", "      Smart Farm"))
        self.MainBtn.setText(_translate("Form", "Main"))
        self.GraphBtn.setText(_translate("Form", "Graph"))
        self.SetBtn.setText(_translate("Form", "Setting"))
        self.TempLabel.setText(_translate("Form", "Temp"))
        self.Temp.setText(_translate("Form", "00.0"))
        self.Humi.setText(_translate("Form", "00.0"))
        self.HumiLabel.setText(_translate("Form", "Humi"))
        self.PhLabel.setText(_translate("Form", "pH"))
        self.Ph.setText(_translate("Form", "00.0"))
        self.CdsLabel.setText(_translate("Form", "Cds"))
        self.Cds.setText(_translate("Form", "000"))
        self.DoLabel.setText(_translate("Form", "DO"))
        self.Do.setText(_translate("Form", "000"))
        self.Tds.setText(_translate("Form", "000"))
        self.TdsLabel.setText(_translate("Form", "TDS"))
        self.TempCheck.setText(_translate("Form", "Temperature"))
        self.HumiCheck.setText(_translate("Form", "Humidity"))
        self.CdsCheck.setText(_translate("Form", "Cds"))
        self.MonthRadio.setText(_translate("Form", "Month"))
        self.WeekRadio.setText(_translate("Form", "Week"))
        self.DayRadio.setText(_translate("Form", "Day"))
        self.FanAuto.setText(_translate("Form", "AUTO"))
        self.LedAuto.setText(_translate("Form", "AUTO"))
        self.WaterAuto.setText(_translate("Form", "AUTO"))
        self.label_13.setText(_translate("Form", "SENSOR"))
        self.label_14.setText(_translate("Form", "SERVER"))
        self.pushButton_2.setText(_translate("Form", "Connect"))
        self.pushButton.setText(_translate("Form", "Disconnect"))
        self.label_18.setText(_translate("Form", "Freq"))
        self.pushButton_3.setText(_translate("Form", "apply"))
        self.label_19.setText(_translate("Form", "IP"))
        self.label_20.setText(_translate("Form", "Port"))
        self.pushButton_4.setText(_translate("Form", "save"))
        self.pushButton_5.setText(_translate("Form", "apply"))
        self.label_21.setText(_translate("Form", "Freq"))
        self.label_22.setText(_translate("Form", "Freq"))
        self.label_16.setText(_translate("Form", "Culture Solution"))
        self.label_17.setText(_translate("Form", "LED"))
        self.label_15.setText(_translate("Form", "Fan"))
        self.label_23.setText(_translate("Form", "hour"))
        self.label_24.setText(_translate("Form", "min"))
        self.label_25.setText(_translate("Form", "Act"))
        self.pushButton_6.setText(_translate("Form", "save"))
        self.label_26.setText(_translate("Form", "min"))
        self.pushButton_7.setText(_translate("Form", "save"))
        self.label_27.setText(_translate("Form", "hour"))
        self.label_28.setText(_translate("Form", "Act"))
        self.label_29.setText(_translate("Form", "Freq"))
        self.label_30.setText(_translate("Form", "Off"))
        self.label_31.setText(_translate("Form", "On"))
        self.ActBtn.setText(_translate("Form", "Actuator"))

from pyqtgraph import PlotWidget
import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

