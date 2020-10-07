from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from threading import Thread
import serial

temperature = []
humidity = []

def readThread(ui):
    ser = serial.Serial(port='COM3',timeout=1)
    while True:
        data = ser.readline()
        if data:
            try:
                temperature.append(int(data[0:3]))
                humidity.append(int(data[3:6]))
                if len(temperature) > 20:
                    temperature.pop(0)
                if len(humidity) > 20:
                    humidity.pop(0)
                print(data)
                ui.uiUpdateDelegate.emit()
            except:
                pass
                
            

class GraphUi(QWidget):
    uiUpdateDelegate = pyqtSignal()  
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.uiUpdateDelegate.connect(self.uiUpdater) 
        pg.setConfigOption('background', 'w')
        self.Graph = PlotWidget(self)
        self.Graph.setGeometry(QRect(0, 0, 600, 500))
        self.Graph.setFrameShape(QFrame.NoFrame)
        self.Graph.setObjectName("Graph") 
        self.Graph.showGrid(x=True, y=True)

    def uiUpdater(self):  
        self.Graph.clear()
        self.Graph.plot(temperature, pen=pg.mkPen('r', width=2))
        self.Graph.plot(humidity, pen=pg.mkPen('b', width=2))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = GraphUi()
    ui.show()

    th = Thread(target=readThread, args=(ui,))
    th.daemon = True
    th.start()

    sys.exit(app.exec_())
