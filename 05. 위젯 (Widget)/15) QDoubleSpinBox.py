import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel("QDoubleSpinBox")
        self.lbl2 = QLabel("$ 0.0")

        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix("$ ")
        self.dspinbox.setDecimals(1)

        self.dspinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)

        self.setLayout(vbox)

        self.setWindowTitle("QDoubleSpinBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText("$ " + str(self.dspinbox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# double이래서 times 의미에서 double인 줄 알았는데 data type에서 double이었다.
# 아무래도 프로그래밍 기초에서 많이 떨어져 살았나 보다. 시간 상으론 얼마 안 됐지만.
