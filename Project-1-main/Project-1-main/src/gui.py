import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from . import process


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Program")
        self.setGeometry(100, 100, 200, 350)

        self.label = QLabel("Wafer : ", self)
        self.label.move(20, 20)
        self.label.resize(150, 20)

        self.label2 = QLabel("Coordinate : ", self)
        self.label2.move(20, 20)
        self.label2.resize(150, 80)

        self.waferEdit = QLineEdit("All", self)
        self.waferEdit.move(100, 20)
        self.waferEdit.resize(80, 20)

        self.columnEdit = QLineEdit("All", self)
        self.columnEdit.move(100, 50)
        self.columnEdit.resize(80, 20)

        self.showEdit = QCheckBox("Show", self)
        self.showEdit.move(30, 90)
        self.showEdit.toggle()

        self.saveEdit = QCheckBox("Save Figure", self)
        self.saveEdit.move(30, 120)
        self.saveEdit.toggle()

        self.csvEdit = QCheckBox("Save CSV", self)
        self.csvEdit.move(30, 150)
        self.csvEdit.toggle()

        self.label3 = QLabel('', self)
        self.label3.move(50, 170)

        self.btnOpenFolder = QPushButton("Set Data Folder", self)
        self.btnOpenFolder.resize(130, 30)
        self.btnOpenFolder.move(35, 200)
        self.btnOpenFolder.clicked.connect(self.find_folder)

        self.btnOpenSave = QPushButton("Open Result Folder", self)
        self.btnOpenSave.resize(130, 30)
        self.btnOpenSave.move(35, 250)
        self.btnOpenSave.clicked.connect(self.open_folder)

        self.btnSave = QPushButton("OK", self)
        self.btnSave.resize(130, 30)
        self.btnSave.move(35, 300)
        self.btnSave.clicked.connect(self.btnInput_clicked)


        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def find_folder(self):
        FileFolder = QFileDialog.getExistingDirectory(self, 'Find Folder')
        self.label3.setText(FileFolder)

    def open_folder(self):
        process.open()

    def btnInput_clicked(self):
        wafer = self.waferEdit.text()
        column = self.columnEdit.text()
        save = self.saveEdit.isChecked()
        show = self.showEdit.isChecked()
        csv = self.csvEdit.isChecked()
        data = self.label3.text()
        try:
            if wafer == '' or column == '':
                raise ValueError('There is blank')
            else:
                process.work(wafer, column, save, show, csv, data)
                QMessageBox.information(self, 'Message', str('Done!'))
        except ValueError as e:
            QMessageBox.information(self, 'Error', str(e))
        except:
            QMessageBox.information(self, 'Error', 'Error Unknown')
