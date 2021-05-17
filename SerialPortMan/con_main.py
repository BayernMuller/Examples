from con_gui import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import serial
import asyncio
import serial_asyncio
from threading import Thread

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

class connectObject(Ui_Form):
	is_connect = False
	connect_port=[]
	def __init__(self, Form):
		self.setupUi(Form)

	def setupUi(self, Form):
		Ui_Form.setupUi(self, Form)
		self.signals()

	def signals(self):
		self.serverCheck.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 0))
		self.clientCheck.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 0))
		self.serialCheck.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 1))
		self.serialCheck.clicked.connect(self.get_com)
		self.connectBtn.clicked.connect(self.on_connect)

	def info(self):
		if self.is_connect:
			if self.stackedWidget.currentIndex():
				seri = self.serialCombo.currentText()
				rate = int(self.speedCombo.currentText())
				return (2, seri, rate)
			ip = self.IPedit.text()
			port = int(self.PortEdit.text())
			return (0 if not self.get_checked() else 1, ip, port)
		return None

	def get_checked(self):
		ls = [self.serverCheck, self.clientCheck, self.serialCheck]
		for i, check in enumerate(ls):
			if check.isChecked():
				return i

	def on_connect(self):
		self.is_connect = True

	def get_com(self):
		self.serialCombo.clear()
		self.connect_port.clear()
		if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
 			self.isLinux = True
		else:
			self.isLinux = False

		COM_Ports = self.serial_ports()  
		for port in COM_Ports:
			if port.find('COM') > -1:
				self.connect_port.append(port)

		print(self.connect_port)   

		for comport in self.connect_port:
			self.serialCombo.addItem(comport)

	def serial_ports(self):  
		if sys.platform.startswith('win'):   
			ports = ['COM%s' % (i + 1) for i in range(256)]   
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):   
			# this excludes your current terminal "/dev/tty"   
			ports = glob.glob('/dev/tty[A-Za-z]*')   
		elif sys.platform.startswith('darwin'):   
			ports = glob.glob('/dev/tty.*')   
		else:   
			raise EnvironmentError('Unsupported platform')   
		result = []   
		for port in ports:   
			try:   
				s = serial.Serial(port)   
				s.close()   
				result.append(port)   
			except (OSError, serial.SerialException):  
				pass
		return result

'''
class UartProtocol(asyncio.Protocol):
    def __init__(self, port):  
        self.port = port

    def run(self, loop):
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        print("Closed Uart thread!")

    def connect_serial(self, text):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        com_no = port
        print (com_no)

        if self.isLinux:
            self.coro = serial_asyncio.create_serial_connection(self.loop, lambda: UartProtocol(), self.mcuPort, baudrate=115200)
            print('Connected mcu port = ' + self.mcuPort)
        else:
            print('com connect')
            self.coro = serial_asyncio.create_serial_connection(self.loop, lambda: UartProtocol(), com_no, baudrate=115200)
        self.loop.run_until_complete(self.coro)

        t = Thread(target=self.run, args=(self.loop,))
        t.start()

    def printLog(self, msg):
        print('<{!r}> {!r}'.format(self.getTimeStamp(), msg))

    def sendUart(self, text):
        if self.uart != None:            
            self.uart.write(text.encode())        
            print ('Finished Send')
        else: 
            print ('Not Connected')

    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        transport.serial.rts = False

    def data_received(self, data):
        message = data.decode() # repr(data)
        print('data received', message)
        # app.textEdit.append(message)

    def connection_lost(self, exc):
        print('port closed')
        self.transport.loop.stop()
'''
