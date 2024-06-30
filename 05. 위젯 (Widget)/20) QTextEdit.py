import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel("Enter your sentence:")
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel("The number of words is 0")

        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QTextEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText("The number of words is " + str(len(text.split())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# QTextEdit().textChanged에는 속성, column or key가 없나 봐, single signal이라고 overload된 str이 없다고 그러네
# 일정 이상으로 커지면 sizePolicy에 따라서 addStretch가 추가한 box형 unit이 가장 큰? 반응하는? box형 unit이랑 크기를 맞춰서 움직이는 듯 보임.
