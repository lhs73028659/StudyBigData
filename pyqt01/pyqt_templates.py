import sys
from PyQt5.QtWidgets import QApplication, QWidget

#클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.setGeometry(0, 0, 800,800)   #x좌표, y좌표, 가로길이, 세로길이
        self.setWindowTitle('QTemplate!!!')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
    