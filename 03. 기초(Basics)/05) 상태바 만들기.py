# 위 Menu, 아래 Status 영역이 있고, 그걸 제외한 영역이 Toolbar.
# 그리고 Toolbar의 중심에 Dockwidget 영역이, 그 안에 Centralwidget 영역이 있다.

# ? QStateBar: 상태 표시
# showMessage(): 텍스트 표시, 표시 시간 설정 가능
# clearMessage(): 현재 텍스트 제거
# currentMessage(): 현재 텍스트 반환
# messageChanged(): 상태 변화 interrupt


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")

        self.setWindowTitle("StatusBar")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
