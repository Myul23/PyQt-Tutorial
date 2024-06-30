# ? popular method
# text() : 현재 텍스트 반환
# setText() : 텍스트 설정
# setChecked() : 버튼의 선택 여부 설정?
# isChecked() : 버튼의 선택 여부 반환
# toggle() : 상태 변경

# ? popular signal
# pressed() : click-in interrupt
# released() : click-out interrupt
# clicked() : click-in and click-out interrupt
# toggled() : toggle interrupt


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton("First Button", self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText("Second Button")

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QRadioButton")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# setCheck()는 default를 True로 설정하는 것이었다
