from socket import *
from sock_gui import *
from threading import Thread
from time import sleep
import socketserver
import con_main
import serial
import sys

# Constants
NOCONNECTION = -1
SERVER = 0
CLIENT = 1
SERIAL = 2

# Global Variable
now_state = NOCONNECTION
is_connected = False
flag = False

def serial_thread(self, info):
    global is_connected, flag
    self.ser = serial.Serial(port = info[1],
                             baudrate = info[2],
                             parity = serial.PARITY_NONE,
                             stopbits = serial.STOPBITS_ONE,
                             bytesize = serial.EIGHTBITS,
                             timeout=1)
    self.add_text('Serial is conneted')
    while flag:
        try:
            rxdata = self.ser.readline().decode('utf-8')       
        except:
            self.add_text('Divice has been disconnected.')
            break
        if rxdata:
            self.add_text(rxdata)

    self.ser.close()
    self.ser = None
    flag = False
    is_connected = False
    self.connectBtn.setText('  Connect  ')


def client_thread(self, info):
    global is_connected, flag
    self.client = socket(AF_INET, SOCK_STREAM)
    self.add_text('Connecting ...')
    
    try:
        self.client.connect((info[1] if info[1] else 'localhost', info[2]))
    except:
        return
    
    self.add_text('Connected!')
    is_connected = True
    while flag:
        try:
            data = ''
            data = self.client.recv(1024)
        except:
            pass
        if data:
            self.recv_data(data)
        else:
            self.add_text('Connection Lost.')
            self.add_text('Client closed.')
            self.connectBtn.setText('  Connect  ')
            flag = False
            is_connected = False
            break

def server_thread(self, info):
    global is_connected
    self.server = socket()
    self.server.bind(info[1:3])
    self.server.listen(1)
    while flag:
        self.add_text('Listen..')
        try:
            self.client, addr = self.server.accept()
        except:
            break
        address = self.client.getpeername();
        strAddr = address[0] + ':' + str(address[1])
        self.add_text(strAddr + ' is conneted.')
        is_connected = True
        while flag:  
            try:
                data = ''
                data = self.client.recv(1024)
            except:
                pass

            if data:
                self.recv_data(data)
            else:
                self.add_text(strAddr +' is disconnected.')
                is_connected = False
                self.client = None
                break

    self.add_text('Server closed.')
    self.server.close()
    self.server = None
    


def recv_data(self, text):
    self.add_text(f'{text.decode()}')
  
def send_data(self):
    if now_state != NOCONNECTION:
        message = self.MsgEdit.text()
        if now_state == SERIAL:
            self.ser.write(message.encode())
            return

        self.client.send(message.encode())
        self.MsgEdit.setText('')

def add_text(self, text):
    self.receiveList.addItem(text)

def connect(self):
    global is_connected, flag, now_state
    if flag:
        flag = False
        if now_state == SERVER:
            if is_connected:
                self.client.close()
            else:
                self.server.close()
        elif now_state == CLIENT:
            self.add_text('Client closed.')
            self.client.close()
            self.client = None
        elif now_state == SERIAL:
            self.add_text('Serial is disconnected.')
            if self.ser != None:
                self.ser.close()
                self.ser = None

        self.thread.join()
        self.thread = None
        self.connectBtn.setText('  Connect  ')
        is_connected = False
        now_state = NOCONNECTION
        return


    Form = QtWidgets.QDialog()
    dialog = con_main.connectObject(Form)
    Form.exec_()
    info = dialog.info()
    if info:
        flag = True
        if info[0] == SERVER:
            now_state = SERVER
            self.thread = Thread(target = self.server_thread, args=(info,))
        elif info[0] == CLIENT:
            now_state = CLIENT
            self.thread = Thread(target = self.client_thread, args=(info,))
        else:#info[0] == SERIAL
            now_state = SERIAL
            self.thread = Thread(target = self.serial_thread, args=(info,))
        self.thread.daemon = True
        self.thread.start()
        self.connectBtn.setText('   Close   ')

def signals(self):
    self.SendBtn.clicked.connect(self.send_data)
    self.ClearBtn.clicked.connect(self.receiveList.clear)
    self.connectBtn.clicked.connect(self.connect)
  

Ui_Form.connect = connect
Ui_Form.signals = signals
Ui_Form.recv_data = recv_data
Ui_Form.send_data = send_data
Ui_Form.add_text = add_text
Ui_Form.server_thread = server_thread
Ui_Form.client_thread = client_thread
Ui_Form.serial_thread = serial_thread

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.signals()
    Form.show()
    sys.exit(app.exec_())

