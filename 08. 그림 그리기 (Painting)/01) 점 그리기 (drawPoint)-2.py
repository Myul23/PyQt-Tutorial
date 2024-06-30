import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
import numpy as np


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("drawPoint")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        colors = ["#D83C5F", "#3CD88F", "#AA5CE3", "#DF4A26", "#AE85F6", "#F7A82E", "#406CF3", "#E9F229", "#29ACF2"]

        pen = QPen()
        for _ in range(1000):
            pen.setWidth(np.random.randint(1, 15))
            pen.setColor(QColor(np.random.choice(colors)))
            qp.setPen(pen)

            rand_x = int(100 * np.random.randn())
            rand_y = int(100 * np.random.randn())
            qp.drawPoint(self.width() // 2 + rand_x, self.height() // 2 + rand_y)
            # 명심하자 자동 형 변환, 넓은 범위로 형 변환 시켜준다는 것 잊지 말자.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
