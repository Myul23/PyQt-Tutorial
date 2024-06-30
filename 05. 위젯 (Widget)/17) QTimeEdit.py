import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QVBoxLayout
from PyQt5.QtCore import QTime


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel("QTimeEdit")

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat("hh::mm::ss")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(timeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QTimeEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# 이제 와 든 의문인데, python에서 __init__ 함수는 class가 선언될 때 불리는 거라서 생성자인데 왜 super()를 쓸 때 super().__init__()으로 굳이 지정을 해주는 거지? 어차피 같은 게 불릴 텐데?
# super()와 super().__init__()의 결과가 다르다.
