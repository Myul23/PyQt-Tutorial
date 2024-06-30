# * QSlider
# setTickInterval(), setTickPosition()
# ? setTickPosition method's argument's value
# QSlider.NoTicks = 0
# QSlider.TickAbove = 1 : up?
# QSlider.TickBelow = 2 : bottom?
# QSlider.TicksBothSides = 3 : left and right
# QSlider.TickLeft = TicksAbove : Left
# QSlider.TickRight = TicksBelow : Right

# * QDial
# setNotchesVisible() : default value is False that doesn't show dial ticks

# * QSlider and QDial's popular signals
# valueChanged()
# sliderPressed() : move-start
# sliderMoved() : move-start and move-finish
# sliderReleased() : move-finish


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)
        # self.dial.setNotchesVisible(True)

        btn = QPushButton("Default", self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle("QSlider and QDial")
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# setGeometry는 길이까지 설정 가능한 거였지, 맞다
