import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Centering")
        self.resize(500, 350)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        # 창의 위치와 크기 정보를 가져온다고 했는데 느낌상 Geometry 객체를 반환하는 것으로 보인다.
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.move(qr.topLeft())
        # 위치 정보를 왼쪽 상단으로 계산하는 객체가 있어서 필요한 듯 보이는데 없어도 중심으로 잘 나온다.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
