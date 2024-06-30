import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QMessageBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# QMessageBox.question: 창 적용 범위, exit 창 이름, exit 창 설명, 선택지, default value
# setText(), setInformativeText(), setDetailedText()
# 하나는 exit 창 이름이고, 하나는 exit 창 설명인 것까진 알겠는데 나머지 하난 뭐냐
