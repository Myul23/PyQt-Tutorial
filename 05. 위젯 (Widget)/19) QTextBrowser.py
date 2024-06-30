import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)
        # self.le.textChanged[str].connect(self.add_text)
        # 내가 원하는 방법은 굳이 p이렇게 만들 필요가 없을 것 같음.

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setWindowTitle("QTextBrowser")
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def add_text(self, text):
        previous = self.tb.text()
        self.tb.setText(text + previous)

    def clear_text(self):
        self.tb.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# QTextBbrowser는 일단 showing만을 추구하는데 html 쪽으로 한 번 처리해서 Browser처럼 보여주는 용도인 듯하다. Online Text Editor를 위한 건가? 흠.
# QTextBrowser().setAcceptRichText() <- 기본이 True이기 때문에 False로 설정하고 싶을 때 쓰거나 True인 걸 강조할 때 쓰거나
