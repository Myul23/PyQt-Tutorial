import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Dialog", self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)

        self.setWindowTitle("Input dialog")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            self.le.setText(str(text))

        # text, ok = QInputDialog.getInt(self, "Input Dialog", "Enter your name:")
        # if ok:
        #     self.le.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# 입력값의 형태에 따라 getText(), getmultiLineText(), getInt(), getDouble(), getItem()의 활용 가능 유무가 정해진다. 그냥 입력 종류 제한하는 용도인 듯하다.
# QLineEdit의 width가 고정되어 있다, 당연한 소리지만, 입력이 된다.
