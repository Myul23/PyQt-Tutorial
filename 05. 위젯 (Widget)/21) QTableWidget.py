import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i + j)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle("QTableWidget")
        self.setGeometry(300, 100, 600, 400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# ? QTableWidget().setEditTriggers()'s arguments
# QAbstractItemView.NoEditTriggers: No Edit
# QAbstractItemView.DoubleClicked: Double Click -> Edit
# QAbstractItemView.AllEditTriggers: Click, Double Click -> Edit


# ? QTableWidget().horizontalHeader().setSectionResizeMode()'s arguments
# QHeaderView.Stretch: 창 맞춤 정도?
# QHeaderView.ResizeToContents: 값 너비 맞춤


# folder action? 중에 첫 character 찾기 기능이 있는데 그거 되더라.
