import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Points")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawPoint(self.width() // 2, self.height() // 2)
        # x, y 좌표라서 int만 받는다. 그냥 반올림하면 여기가 문제인 걸 모를까 봐 이렇게 하는 걸까.

        qp.setPen(QPen(Qt.green, 12))
        qp.drawPoint(self.width() // 4, 3 * self.height() // 4)

        qp.setPen(QPen(Qt.red, 16))
        qp.drawPoint(3 * self.width() // 4, self.height() // 4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
