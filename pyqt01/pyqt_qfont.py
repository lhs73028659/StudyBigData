import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


#클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
        #화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.setGeometry(0, 0, 800,800)   #x좌표, y좌표, 가로길이, 세로길이
        self.setWindowTitle('QTemplate!!!')
        self.text = 'What a wonderful world~'
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    def drawText(self, event, paint):
        paint.setPen(QColor(0,0,200)) # RED, GREEN, BLUE
        paint.setFont(QFont('NanumGothic', 30))
        paint.drawText(105, 100, 'HELL WORLD~')
        paint.setPen(QColor(0,200,100))
        paint.setFont(QFont('Impact', 20))
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
    