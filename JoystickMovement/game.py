from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import serial

ser = serial.Serial(port='COM3',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 커스텀 위젯에서 스타일 시트를 사용하게 함.
        self.pt = [250,250]
        # 움직이는 사각형의 좌표
        self.setStyleSheet('background-color: white')
        # 스타일 시트 배경 색 변경

    def paintEvent(self, event):
        # 위젯이 그림을 그려야 할 때 호출되는 이벤트
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(self.pt[0], self.pt[1], 10,10, QColor('red'))
        qp.end()

def reading(ui):
    # 프로토콜
    # 0x02, X, Y, 0x03
    while True:
        data = ser.read(4)
        # 4바이트 받기. (타임아웃)
        data = data[1:3]
        print(data)
        ui.pt[0] += (data[0] - 48 - 1) * 10
        ui.pt[1] += (data[1] - 48 - 1) * 10
        ui.update()
        # Game 의 paintEvent를 호출 함

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Game()
    thread = threading.Thread(target=reading, args=(ui,))
    thread.daemon = True
    thread.start()
    ui.show()
    sys.exit(app.exec_())