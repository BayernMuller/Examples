# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'con_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("central")
        Form.resize(380, 250)
        Form.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font:18pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serverCheck = QtWidgets.QRadioButton(Form)
        self.serverCheck.setStyleSheet("font: 13pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.serverCheck.setChecked(True)
        self.serverCheck.setObjectName("serverCheck")
        self.horizontalLayout.addWidget(self.serverCheck)
        self.clientCheck = QtWidgets.QRadioButton(Form)
        self.clientCheck.setStyleSheet("font: 13pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.clientCheck.setObjectName("clientCheck")
        self.horizontalLayout.addWidget(self.clientCheck)
        self.serialCheck = QtWidgets.QRadioButton(Form)
        self.serialCheck.setStyleSheet("font: 13pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.serialCheck.setObjectName("serialCheck")
        self.horizontalLayout.addWidget(self.serialCheck)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setMouseTracking(False)
        self.page.setObjectName("page")
        self.gridWidget = QtWidgets.QWidget(self.page)
        self.gridWidget.setGeometry(QtCore.QRect(0, 20, 341, 101))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridWidget)
        self.label_3.setStyleSheet("font: 17pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridWidget)
        self.label_2.setStyleSheet("font: 17pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.IPedit = QtWidgets.QLineEdit(self.gridWidget)
        self.IPedit.setStyleSheet("background-color: rgb(255, 255, 255); font: 20px \"Arial\";\n"
"border-radius: 3px;")
        self.IPedit.setAlignment(QtCore.Qt.AlignCenter)
        self.IPedit.setObjectName("IPedit")
        self.gridLayout_2.addWidget(self.IPedit, 0, 1, 1, 1)
        self.PortEdit = QtWidgets.QLineEdit(self.gridWidget)
        self.PortEdit.setStyleSheet("background-color: rgb(255, 255, 255); font: 20px \"Arial\";\n"
"border-radius: 3px;")
        self.PortEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.PortEdit.setObjectName("PortEdit")
        self.gridLayout_2.addWidget(self.PortEdit, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridWidget_2 = QtWidgets.QWidget(self.page_2)
        self.gridWidget_2.setGeometry(QtCore.QRect(0, 20, 341, 101))
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_5.setStyleSheet("font: 17pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_4.setStyleSheet("font: 17pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.serialCombo = QtWidgets.QComboBox(self.gridWidget_2)
        self.serialCombo.setStyleSheet("background-color: rgb(255, 255, 255); font: 20px \"Arial\";\n"
"border-radius: 3px;")
        self.serialCombo.setObjectName("serialCombo")
        self.gridLayout_3.addWidget(self.serialCombo, 0, 1, 1, 1)
        self.speedCombo = QtWidgets.QComboBox(self.gridWidget_2)
        self.speedCombo.setStyleSheet("background-color: rgb(255, 255, 255); font: 20px \"Arial\";\n"
"border-radius: 3px;")
        self.speedCombo.setObjectName("speedCombo")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.speedCombo.addItem("")
        self.gridLayout_3.addWidget(self.speedCombo, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.connectBtn = QtWidgets.QPushButton(Form)
        self.connectBtn.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"font: 75 13pt \"나눔스퀘어 Bold\";\n"
"border-radius: 5px;")
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_2.addWidget(self.connectBtn)
        self.cancelBtn = QtWidgets.QPushButton(Form)
        self.cancelBtn.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"font: 75 13pt \"나눔스퀘어 Bold\";\n"
"border-radius: 5px;")
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.retranslateUi(Form)
        self.connectBtn.clicked.connect(Form.close)
        self.cancelBtn.clicked.connect(Form.close)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Connect"))
        self.serverCheck.setText(_translate("Form", "Server"))
        self.clientCheck.setText(_translate("Form", "Client"))
        self.serialCheck.setText(_translate("Form", "Serial"))
        self.label_3.setText(_translate("Form", "IP"))
        self.label_2.setText(_translate("Form", "Port"))
        self.PortEdit.setText(_translate("Form", "7777"))
        self.label_5.setText(_translate("Form", "Baud Rate"))
        self.label_4.setText(_translate("Form", "Port"))
        self.speedCombo.setCurrentText(_translate("Form", "1200"))
        self.speedCombo.setItemText(0, _translate("Form", "1200"))
        self.speedCombo.setItemText(1, _translate("Form", "2400"))
        self.speedCombo.setItemText(2, _translate("Form", "4800"))
        self.speedCombo.setItemText(3, _translate("Form", "9600"))
        self.speedCombo.setItemText(4, _translate("Form", "19200"))
        self.speedCombo.setItemText(5, _translate("Form", "38400"))
        self.speedCombo.setItemText(6, _translate("Form", "57600"))
        self.speedCombo.setItemText(7, _translate("Form", "115200"))
        self.speedCombo.setItemText(8, _translate("Form", "230400"))
        self.speedCombo.setItemText(9, _translate("Form", "460800"))
        self.speedCombo.setItemText(10, _translate("Form", "921600"))
        self.connectBtn.setText(_translate("Form", " Connect "))
        self.cancelBtn.setText(_translate("Form", "  Cancel  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
