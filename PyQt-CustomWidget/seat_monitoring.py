from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from random import *

class SeatMonitoring(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 480)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # allow custom wigdet to use style sheet
        self.lists = [[randrange(0,3) for j in range(15 if i != 2 else 1)] for i in range(5)]
        self.setStyleSheet('background-color: white')
        self.colors = [QColor('gray'), QColor('green'), QColor('red')]
        print(self.lists)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        cenX = 400 - (7.5 * 40)
        cenY = 240 - (2.5 * 40)
        for i, col in enumerate(self.lists):
            for j, row in enumerate(col):
                rect = QRect(cenX + j * 40, cenY + i * 40, 40, 40)
                rect.adjust(7, 7, -7, -7)
                qp.fillRect(rect, self.colors[row])
        qp.end()
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = SeatMonitoring()
    ui.show()
    sys.exit(app.exec_())