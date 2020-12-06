# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sock_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_Form(QDialog):
    def setupUi(self, Form):
        Form.setObjectName("central")
        Form.resize(900, 693)
        Form.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.receiveList = QtWidgets.QListWidget(Form)
        self.receiveList.setStyleSheet("background-color: #FFFFFF;\n"
"font: 75 14pt \"Arial\";\n"
"border-radius: 10px;")
        self.receiveList.setObjectName("receiveList")
        self.verticalLayout_2.addWidget(self.receiveList)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MsgEdit = QtWidgets.QLineEdit(Form)
        self.MsgEdit.setStyleSheet("background-color: rgb(255, 255, 255); font: 20px \"Arial\";\n"
"border-radius: 3px;")
        self.MsgEdit.setObjectName("MsgEdit")
        self.horizontalLayout.addWidget(self.MsgEdit)
        self.SendBtn = QtWidgets.QPushButton(Form)
        self.SendBtn.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"font: 75 20pt \"나눔스퀘어 Bold\";\n"
"border-radius: 5px;")
        self.SendBtn.setObjectName("SendBtn")
        self.horizontalLayout.addWidget(self.SendBtn)
        self.ClearBtn = QtWidgets.QPushButton(Form)
        self.ClearBtn.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"font: 75 20pt \"나눔스퀘어 Bold\";\n"
"border-radius: 5px;")
        self.ClearBtn.setObjectName("ClearBtn")
        self.horizontalLayout.addWidget(self.ClearBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 3, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("font: 34.4pt \"나눔스퀘어 ExtraBold\";\n"
"color: #FFFFFF")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.connectBtn = QtWidgets.QPushButton(Form)
        self.connectBtn.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"font: 75 20pt \"나눔스퀘어 Bold\";\n"
"border-radius: 5px;")
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_5.addWidget(self.connectBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SendBtn.setText(_translate("Form", "    Send    "))
        self.ClearBtn.setText(_translate("Form", "    Clear    "))
        self.label_3.setText(_translate("Form", "Connection Program"))
        self.connectBtn.setText(_translate("Form", "  Connect  "))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
