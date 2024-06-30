# splitter는 경계를 drag해서 자식 위젯의 크기를 조절할 수 있도록 합니다?

import sys
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(0x0001)
        top.setObjectName("top")

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle("QSplitter")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# 중간 위젯의 크기가 최소 크기일 때 밀어내는 방향에 최소 크기가 아닌 위젯이 있다면 그 크기를 먼저 줄이더군요
# 그리고 기본 마진이 있어서 최소 크기 위젯의 크기를 0으로 만들어도 위젯 하나만 만들었을 때보다 크기가 작더군요

# ? setFrameShape argument value
# QFrame::NotFrame : 0
# QFrame::Box : 0x0001
# QFrame::Panel : 0x0002
# QFrame::WinPanel : 0x0003
# QFrame::HLine : 0x0004
# QFrame::VLine : 0x0005
# QFrame::StyledPanel : 0x0006
# Box Shape이자 Style

# ? setFrameShadow argument value
# QFrame::Plain : 0x0010
# QFrame::Raised : 0x0020
# QFrame::Sunked : 0x0030

# border-size?에 따라서 두꺼워지는 style도 있고 아닌 것도 있고

# 안쪽이 움직이는 건 splitter 특유의 그것이라고 할 수 있는데
# 그럼 바깥쪽이 움직이게 하려면 length를 건드리는 수밖에 없나?
# 일단 바깥 border에 대한 click interrupt가 있나?
# mousePressEvent(self, a0: QMouseEvent) -> None로 이것저것 확인해 봤는데 nearest object에 대한 정보는 제공하지 않는 듯하다. 하긴 tracking에는 많은 resource가 필요한 법이니까...
