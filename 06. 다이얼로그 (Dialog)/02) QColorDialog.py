import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton("Dialog", self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())
        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle("Color Dialog")
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())
            print(col.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# QColorDialog.getColor().name()이 정말 이름으로 넒길까? 굳이 그럴 필요가 없을 것 같은데, 어차피 hex style(?)로 변환해야 할 테니까. -> 맞네 그냥 색코드로 전달하네
