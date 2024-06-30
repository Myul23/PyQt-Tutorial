import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Reimplementing event handler")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()
        else:
            print("Doesn't have response")

    def mouseDoubleClickEvent(self, a0):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# ? Event Handler
# keyPressEvent: key press-in
# keyReleaseEvent: key press-out
# mouseDoubliClickEvent
# mouseMoveEvent
# mousePressEvent: mouse press-in
# mouseReleaseEvent: mouse press-out
# moveEvent: widget move event
# resizeEvent: widget resize event
