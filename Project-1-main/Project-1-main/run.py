import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src import gui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.MainWindow()
    window.show()
    app.exec_()
