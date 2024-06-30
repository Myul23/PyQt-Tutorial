# # ? QDate
# from PyQt5.QtCore import QDate

# now = QDate.currentDate()
# # 이미 계산된 걸 객체 입력 시 넣는 것 같기도 한데, 흠 조금 신기함
# print(now.toString())
# # ddd M d yyyy

# from PyQt5.QtCore import QDate, Qt

# now = QDate.currentDate()
# print(now.toString("d.M.yy"))
# print(now.toString("dd.MM.yyyy"))
# print(now.toString("ddd.MMMM.yyyy"))
# print(now.toString(Qt.ISODate))
# print(now.toString(Qt.DefaultLocaleLongDate))
# # local 언어 분석해서 한국어로 display 해준다
# # 다행히 d, dd, ddd의 차이(최소 한 자리 표기, 두 자리 표기, 문자열 표기)를 기억하고 있다.
# # ISO 형식이 'yyyy-MM-dd', DefaultLocaleLongDate는 말 그대로 Long Date


# # ? QTime
# from PyQt5.QtCore import QTime

# time = QTime.currentTime()
# print(time.toString())
# # hh:mm:ss, 24시간 기준


# from PyQt5.QtCore import QTime, Qt

# time = QTime.currentTime()
# print(time.toString("h.m.s"))
# print(time.toString("hh.mm.ss"))
# print(time.toString("hh.mm.ss.zzz"))
# print(time.toString(Qt.DefaultLocaleLongDate))
# print(time.toString(Qt.DefaultLocaleShortDate))
# # h, hh은 d, dd 때와 같다. zzz는 생각한 것이 ms다.
# # Long Date는 AM/PM 표시부터 해준다, Short Date = Long Date - Second


# # ? QDateTime
# from PyQt5.QtCore import QDateTime

# datetime = QDateTime.currentDateTime()
# print(datetime.toString())
# # MMMM M d hh:mm:ss yyyy


# from PyQt5.QtCore import QDateTime, Qt

# datetime = QDateTime.currentDateTime()
# print(datetime.toString("d.M.yy hh:mm:ss"))
# print(datetime.toString("dd.MM.yyyy, hh:mm:ss"))
# print(datetime.toString(Qt.DefaultLocaleLongDate))
# print(datetime.toString(Qt.DefaultLocaleShortDate))
# # Long Date = yyyy년 M월 d일 MMMM요일 Long Date
# # Short Date = yyyy-mm-dd Short Date


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle("Date")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
