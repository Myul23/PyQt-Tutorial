import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # SansSerif, 궁서
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle("Tooltips")
        self.setGeometry(300, 300, 300, 200)
        self.show()


# self.setToolTip의 경우, ToolTip이라는 hold 시 생기는 설명에 대해 전반적으로 setting 하는 것으로 보인다. 추가적으로 다 만들고 show를 통해 화면을 생성하는 방식이라 중간에 값을 바꾸면 나중에 바뀐 값으로 전체가 바뀐다.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
