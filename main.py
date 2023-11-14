import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import uic


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.flag =True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            #  круг должен быть желтым
            color = QColor(*[randint(0, 255) for _ in range(3)])
            qp.setPen(color)
            qp.setBrush(color)
            r = randint(10, 100)
            x, y = randint(0, 500 - r), randint(0, 500 - r)
            qp.drawEllipse(x, y, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())
