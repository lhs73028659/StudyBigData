import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


#클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
        #화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(0, 0, 1500,800)   #x좌표, y좌표, 가로길이, 세로길이
        self.setWindowTitle('QLabel')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/image/lion.png')) # 윈도우아이콘 지정
        label1 = QLabel('Label1', self)
        label2 = QLabel('Label2', self)
        label1.setStyleSheet(
            ('border-width: 3px;'
            'border-style: solid;'
            'border-color: blue;'
            'image: url(./pyqt01/image/image1.png)')
        )

        label2.setStyleSheet(
        ('border-width: 3px;'
        'border-style: dot-dot-dash;'
        'border-color: purple;'
        'image: url(./pyqt01/image/image2.png)')
        )





        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
    