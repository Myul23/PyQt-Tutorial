import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = y = 0

        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)

        self.setMouseTracking(True)

        self.setWindowTitle("Reimplementing event handler")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mouseMoveEvent(self, e):
        x, y = e.x(), e.y()
        # x, y = e.globalX(), e.globalY()

        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# 당연한 소리지만, 창 위 액션에 대해서만 추적한다.
