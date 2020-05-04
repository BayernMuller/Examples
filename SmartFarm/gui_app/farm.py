from farm_gui import *
from threading import Thread
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from functools import partial
from time import sleep
import pyqtgraph as pg
import PyQt5
import serial
import sqlite3

Now_temp = ''
Now_humi = ''
Now_cds = ''

temperature = []
humidity = []
cds = []

'''
ser = serial.Serial(port='COM6',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)
'''

def ReceiveData(self, ui):
	global Now_cds, Now_humi, Now_temp
	while True:
		rxdata = ser.readline().decode('utf-8')
		if rxdata:
			print(rxdata)
			con = sqlite3.connect("data.db")         #DB File 생성
			cur = con.cursor()
			cur.execute("CREATE TABLE if not exists datas(temp text, humi text, cds text);")

			Now_temp = rxdata[1:5]
			Now_humi = rxdata[7:11]
			Now_cds = format(int(rxdata[13:16]) / 10.23, '.1f')
			temperature.append(float(Now_temp))
			humidity.append(float(Now_humi))
			cds.append(float(Now_cds))

			cur.execute("INSERT INTO datas VALUES({}, {}, {});".format(Now_temp, Now_humi, Now_cds))
			con.commit()
			con.close()
			ui.uiUpdateDelegate.emit(1)
			sleep(2)

class EventThread(PyQt5.QtCore.QThread):
    def __init__(self, ui):
        self.btn_list = [ui.MainBtn,ui.GraphBtn,ui.ActBtn,ui.SetBtn]
        for i, mainButton in enumerate(self.btn_list):
            mainButton.clicked.connect(partial(ui.stackedWidget.setCurrentIndex, i))
            mainButton.clicked.connect(partial(mainButton.setChecked, True))

        self.checklist = [ ui.TempCheck, ui.HumiCheck, ui.CdsCheck ]
        for check in self.checklist:
        	check.clicked.connect(partial(ui.uiUpdateDelegate.emit, 1))
        

class GraphGui(QtWidgets.QMainWindow, Ui_Form):
    global Now_temp, Now_humi, Now_cds
    uiUpdateDelegate = pyqtSignal(int)   
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.uiUpdateDelegate.connect(self.uiUpdater)   
        pg.setConfigOption('background', 'w')
        # self.Graph.setRange(xRange=[2, 20])
        self.Graph.showGrid(x=True, y=True)

    def uiUpdater(self):  
        self.Graph.clear()
        if self.TempCheck.isChecked():
        	self.Graph.plot(temperature, pen= pg.mkPen('r', width=2))
        if self.HumiCheck.isChecked():
        	self.Graph.plot(humidity, pen=pg.mkPen('b', width=2))
        if self.CdsCheck.isChecked():
        	self.Graph.plot(cds, pen=pg.mkPen('g', width=2))
        self.Temp.setText(Now_temp)
        self.Humi.setText(Now_humi)
        self.Cds.setText(Now_cds)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GraphGui()
    ui.setupUi(Form)

    #dataThread = Thread(target=ReceiveData, args=(ser, ui))
    #dataThread.daemon = True
    #dataThread.start()

    eventThread = EventThread(ui)
    ui.uiUpdateDelegate.emit(1)
    Form.show()
    sys.exit(app.exec_())