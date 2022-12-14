import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(400, 150, 1200,800)   #x좌표, y좌표, 가로길이, 세로길이
        self.setWindowTitle('QPushbutton')
        self.show()

    def addControls(self) -> None:
        btn1 = QPushButton('Click', self)
        btn1.setGeometry(500, 380, 120, 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
    