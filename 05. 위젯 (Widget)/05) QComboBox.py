import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Option1", self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem("Option1")
        cb.addItem("Option2")
        cb.addItem("Option3")
        cb.addItem("Option4")
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle("QComboBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# ComboBox에 title이 "title"에 저장된 게 아니라 str에 저장되어 있는 듯하다
