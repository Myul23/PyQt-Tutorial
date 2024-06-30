# QCheckBox
# ? popular method
# text() : 텍스트 반환
# setText() : 텍스트 set
# isChecked() : 상태 반환 (True, False)
# checkState() : 상태 상세 반환 (True, not changed, False)
# toggle() : 상태 변경

# ? popular signal
# clicked() : click interrupt (click-in, click-out)
# pressed() : click-in interrupt
# released() : click-out interrupt
# stateChanged() : toggle interrupt


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox("Show Title", self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setWindowTitle("QCheckBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle(" ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
