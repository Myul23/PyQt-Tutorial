import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon("open.png"), "Open", self)
        openFile.setShortcut("Ctrl+0")
        openFile.setStatusTip("Open New File")
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu("$File")
        fileMenu.addAction(openFile)

        self.setWindowTitle("File Dialog")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "./")
        if fname[0]:
            f = open(fname[0], "r")

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# plain 하게 하는 TextEdit이랑 비교했을 때 이쪽은 box가 반응형인 듯?
