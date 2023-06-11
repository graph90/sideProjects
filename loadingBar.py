import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import QBasicTimer

class LoadingBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Loading Bar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.close()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadingBar()
    sys.exit(app.exec_())