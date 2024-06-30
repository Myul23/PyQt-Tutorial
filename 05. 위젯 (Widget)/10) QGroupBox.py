# 위젯 박스라 전체 제목, 전체 제어 등 가능
# shortcut은 뭔 소릴까


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid)

        self.setWindowTitle("Box Layout")
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox("Exclusive Radio Buttons")

        radio1 = QRadioButton("Radio1")
        radio2 = QRadioButton("Radio2")
        radio3 = QRadioButton("Radio3")
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox("Exclusive Radio Buttons")
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton("Radio1")
        radio2 = QRadioButton("Radio2")
        radio3 = QRadioButton("Radio3")
        radio1.setChecked(True)
        checkbox = QCheckBox("Independent Checkbox")
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox("Non-Exclusive Checkboxes")
        groupbox.setFlat(True)

        checkbox1 = QCheckBox("Checkbox1")
        checkbox2 = QCheckBox("Checkbox2")
        checkbox2.setChecked(True)
        tristatebox = QCheckBox("Tri-state Button")
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox("Push Buttons")
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton("Normal Button")
        togglebutton = QPushButton("Toggle Button")
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        self.flatbutton = QPushButton("Flat Button")
        self.flatbutton.setFlat(True)
        self.flatbutton.clicked.connect(self.flatChanged)
        popupbutton = QPushButton("Popup Button")
        menu = QMenu(self)
        menu.addAction("First Item")
        menu.addAction("Second Item")
        menu.addAction("Third Item")
        menu.addAction("Fourth Item")
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(self.flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def flatChanged(self):
        if self.flatbutton.isFlat():
            self.flatbutton.setFlat(False)
        else:
            self.flatbutton.setFlat(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# checkable과 checked로 설문지의 필요없는 문항 건너뛰기 같은 걸 구현할 수 있군요
# tristate는 선택 가능한 value가 0, 1, 2인 듯
# 그냥 flat 변화를 주는 걸 보니까 click - flat change를 구현해보고 싶었다
