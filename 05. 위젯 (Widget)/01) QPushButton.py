# QPushButton
# ? popular method
# setCheckable() : 버튼 interrupt, 상태 유지
# toggle() : 토글
# setIcon() : 아이콘 set
# setEnabled() : 버튼이냐 그림의 떡이냐
# isChecked() : 버튼의 선택 여부? 뭔 소리지
# setText() : 텍스트 set
# text() : 현재 텍스트 반환

# ? popular signal
# clicked() : click interrupt
# pressed() : 눌렸을 때(clicking? click hover?) interrupt
# released() : click 탈락 시에 interrupt
# toggled() : toggle 전환 시 interrupt


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("&Button1", self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText("Button&2")

        btn3 = QPushButton("Button3", self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle("QPushButton")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# & + character는 Alt + character로 단축키 설정
