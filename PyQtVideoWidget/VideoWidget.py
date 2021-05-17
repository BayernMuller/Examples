from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from threading import Thread
import cv2

class VideoWidget(QLabel):
    __refreshSignal = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__refreshSignal.connect(self.__onRefresh)
        self.__threadFlag = False
        
    
    def play(self, path: str, delay=30):
        if self.__threadFlag:
            self.__threadFlag = False
            self.th.join()

        self.th = Thread(target=self.__threadFunction, args=(path, delay))
        self.th.daemon = True
        self.__threadFlag = True
        self.th.start()

    def __onRefresh(self, pixmap: QPixmap):
        self.setPixmap(pixmap)

    def __threadFunction(self, path: str, delay: int):
        cap = cv2.VideoCapture(path)  
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        while cap.isOpened() and self.__threadFlag:
            ret, img = cap.read()
            if not ret:
                break
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            size = self.size()
            img = cv2.resize(img, (size.width(), size.height())) 

            h,w,c = img.shape
            qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        
            pixmap = QPixmap.fromImage(qImg)
            self.__refreshSignal.emit(pixmap)
            

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = VideoWidget()
    w.resize(1280, 720)
    w.show()
    w.play('video.mp4')
    sys.exit(app.exec_())