import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(lambda x: self.lbl.setText(x.toString()))  # self.showDate

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle("QCalendarWidget")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    # def showDate(self, date):
    #     self.lbl.setText(date.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# Calendar Widget의 완성도가 상당하다
# 당연한 말이지만, GUI 연결 함수(뭐라고 하더라)에 lambda가 가능하다.
