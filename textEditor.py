import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from tkinter import Tk
from tkinter import filedialog


class Editor:

    def __init__(self):
        self.currentFile = ""
        self.dict = {}

        ui.actionOpen.triggered.connect(self.openF)
        ui.actionNew.triggered.connect(self.newF)
        ui.actionSave.triggered.connect(self.saveF)
        ui.actionDelete.triggered.connect(self.deleteF)
        ui.actionClose.triggered.connect(self.closeF)

        ui.toolFett.setCheckable(True)
        ui.toolFett.setShortcut(QKeySequence.Bold)
        ui.toolFett.toggled.connect(lambda x: ui.textEdit.setFontWeight(QFont.Bold if x else QFont.Normal))

        ui.toolKursiv.setCheckable(True)
        ui.toolKursiv.setShortcut(QKeySequence.Italic)
        ui.toolKursiv.toggled.connect(ui.textEdit.setFontItalic)

        ui.textEdit.setAcceptRichText(True)

    def newF(self):
        Tk().withdraw()
        filename = filedialog.asksaveasfilename(title='Speicherort auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            self.disableNewDocumentTab()
            if not filename.endswith('.txt'):
                filename += '.txt'
            self.currentFile = filename
            open(filename, "w")

            self.addNewTab(filename)

    def changeCurrentTab(self, filename):
        with open(self.currentFile, "w") as file:
            file.write(ui.textEdit.toHtml())
        self.currentFile = filename
        with open(filename, "r") as file:
            ui.textEdit.setText(file.read())

    def addNewTab(self, filename):
        self.dict[filename] = QtWidgets.QPushButton(ui.centralwidget)
        self.dict[filename].setText(filename)
        self.dict[filename].clicked.connect(lambda: self.changeCurrentTab(filename))
        self.changeCurrentTab(filename)
        ui.layoutTabs.addWidget(self.dict[filename])

    def openF(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename(title='Datei auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            self.disableNewDocumentTab()
            self.currentFile = filename
            with open(filename, "r") as file:
                ui.textEdit.setText(file.read())
            self.addNewTab(filename)

    def saveF(self):
        if self.currentFile == "":
            self.currentFile = "Neues Dokument.txt"
        with open(self.currentFile, "w") as file:
            file.write(ui.textEdit.toHtml())

    def deleteF(self):
        self.closeF()
        os.remove(self.currentFile)

    def closeF(self):
        item = self.dict[self.currentFile]
        item.setParent(None)

    def disableNewDocumentTab(self):
        if self.currentFile == "":
            ui.newDocument.setParent(None)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    editor = Editor()

    main_window.show()
    sys.exit(app.exec_())
