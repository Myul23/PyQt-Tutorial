# ? echoMode : 문자열 입력 표시 종류에 따른 모드 분류
# QLineEdit.Normal = 0 : default value
# QLineEdit.NoEcho = 1 : 입력 표시 거부
# QLineEdit.Password = 2 : 입력 별표로 표시
# QLineEdit.PasswordEchoOnEdit  = 3 : 입력 시에만 표시, 수정 중에는 다른 문자로 표시 ?

# ? string validation check method
# maxLength() : set max string's length
# setValidator() : set some string's type
# setText(), insert()
# text() : return current text
# If it is different between input(ing) string and display(ing) string, it uses 'displayText()' that return display(ing) string
# setSelection(), selectAll() : select and choose text
# cut(), copy(), paste()
# setAlignment() : align text
# textChanged(), cursorPositionChanged()
# editingFinished() : cursor movement interrupt
# returnPressed() : Return and Enter Button interrupt


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.move(50, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle("QLineEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# 현재 텍스트를 반환, 그러니까 text()를 통해 바뀐 걸 확인하고 현재 텍스트를 넘김
