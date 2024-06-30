import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel("QDateEdit")

        dateedit = QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        dateedit.setDisplayFormat("dd.MM.yyyy")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QDateEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# 당연히 string format을 변경할 수 있다, 이러면 처음부터 default 설정도 건드리고 갈 수 있다면 좋을 텐데
# setMinimumDate's default: 1752-09-14, minimum: 100-01-01
# setMaximumDate's default: 9999-12-31
