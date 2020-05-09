import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from tkinter import Tk
from tkinter import filedialog


class Editor:

    def __init__(self):
        self.currentFile = ""
        self.dict = {}

    def newF(self):
        Tk().withdraw()
        filename = filedialog.asksaveasfilename(title='Speicherort auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            self.disableNewDocument()
            if not filename.endswith('.txt'):
                filename += '.txt'
            self.currentFile = filename
            open(filename, "w")

            self.dict[filename] = QtWidgets.QPushButton(ui.centralwidget)
            self.dict[filename].setText(filename)
            self.dict[filename].clicked.connect(lambda: self.changeCurrent(filename))
            ui.layoutTabs.addWidget(self.dict[filename])

    def changeCurrent(self, filename):
        self.currentFile = filename

    def openF(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename(title='Datei auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            self.disableNewDocument()
            self.currentFile = filename
            with open(filename, "r") as file:
                ui.textEdit.setPlainText(file.read())

    def saveF(self):
        if self.currentFile == "":
            self.currentFile = "Neues Dokument.txt"
        with open(self.currentFile, "w") as file:
            file.write(ui.textEdit.toPlainText())

    def deleteF(self):
        os.remove(self.currentFile)

    def closeF(self):
        print("close")

    def disableNewDocument(self):
        if self.currentFile == "":
            ui.newDocument.setParent(None)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    editor = Editor()
    ui.actionOpen.triggered.connect(editor.openF)
    ui.actionNew.triggered.connect(editor.newF)
    ui.actionSave.triggered.connect(editor.saveF)
    ui.actionDelete.triggered.connect(editor.deleteF)
    ui.actionClose.triggered.connect(editor.closeF)

    main_window.show()
    sys.exit(app.exec_())
