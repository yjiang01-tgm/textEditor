import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from tkinter import Tk
from tkinter import filedialog


class EditorComponent:
    def __init__(self, button: QtWidgets.QPushButton, button_text: str, text: str, editor):
        self.button = button
        self.button.setText(button_text)
        self.button.clicked.connect(lambda: editor.changeCurrentTab(button_text))
        self.button.setStyleSheet("""
                QPushButton{
                    color: rgb(255, 255, 255);
                    background-color: rgb(180, 180, 180);
                    border: none;
                    padding: 10px 10px;
                    font-size: 16px;
                    border-radius: 8px;
                }

                QPushButton:hover{
                    background-color: white;
                    border: 2px solid rgb(180, 180, 180);
                    color: rgb(0, 0, 0);
                }
                QPushButton:disabled{
                    background-color: rgba(0, 170, 255, 0.6);
                }
                """)
        self.text = text
        self.editor = editor

    def setText(self, text):
        self.text = text
        ui.textEdit.setText(text)

    def getText(self) -> str:
        return self.text

    def getButton(self) -> QtWidgets.QPushButton:
        return self.button

    def buttonStatus(self, status: bool):
        self.button.setEnabled(status)

class Editor:

    def __init__(self):
        self.currentFile = ""
        self.dict = {self.currentFile: EditorComponent(QtWidgets.QPushButton(), "Neues Dokument", "", self)}

        ui.actionOpen.triggered.connect(self.openF)
        ui.actionNew.triggered.connect(self.newF)
        ui.actionSave.triggered.connect(self.saveF)
        ui.actionDelete.triggered.connect(self.deleteF)
        ui.actionClose.triggered.connect(self.closeF)
        ui.textEdit.selectionChanged.connect(self.updateFormatting)

        ui.toolFett.setCheckable(True)
        ui.toolFett.setShortcut(QKeySequence.Bold)
        ui.toolFett.toggled.connect(lambda x: ui.textEdit.setFontWeight(QFont.Bold if x else QFont.Normal))

        ui.toolKursiv.setCheckable(True)
        ui.toolKursiv.setShortcut(QKeySequence.Italic)
        ui.toolKursiv.toggled.connect(ui.textEdit.setFontItalic)

        ui.toolUnter.setCheckable(True)
        ui.toolUnter.setShortcut(QKeySequence.Underline)
        ui.toolUnter.toggled.connect(ui.textEdit.setFontUnderline)

        ui.toolTitel.clicked.connect(self.fontTitle)
        ui.toolStandard.clicked.connect(self.fontStandard)
        ui.toolUeberschrift.clicked.connect(self.fontUeberschrift)

        ui.textEdit.setFontPointSize(12)
        ui.toolFontSize.valueChanged.connect(lambda: ui.textEdit.setFontPointSize(ui.toolFontSize.value()))

        ui.textEdit.setAcceptRichText(True)

    def fontTitle(self):
        ui.textEdit.setFontUnderline(True)
        ui.textEdit.setFontWeight(QFont.Bold)
        ui.textEdit.setFontPointSize(20)

    def fontStandard(self):
        ui.textEdit.setFontUnderline(False)
        ui.textEdit.setFontWeight(QFont.Normal)
        ui.textEdit.setFontPointSize(12)

    def fontUeberschrift(self):
        ui.textEdit.setFontUnderline(False)
        ui.textEdit.setFontWeight(QFont.Bold)
        ui.textEdit.setFontPointSize(16)

    def changeCurrentTab(self, filename):
        editor_comp: EditorComponent = self.dict[self.currentFile]
        editor_comp.setText(ui.textEdit.toHtml())
        editor_comp.buttonStatus(True)

        self.currentFile = filename

        editor_comp = self.dict[self.currentFile]
        with open(self.currentFile, "r") as file:
            editor_comp.setText(file.read())
        editor_comp.buttonStatus(False)

    def addNewTab(self, filename):
        if filename not in self.dict:
            self.dict[filename] = EditorComponent(QtWidgets.QPushButton(), filename, "", self)
            ui.layoutTabs.addWidget(self.dict[filename].getButton())
        self.changeCurrentTab(filename)

    def updateFormatting(self):
        ui.toolFett.blockSignals(True)  # Signale blockieren (.connect)
        ui.toolFett.setChecked(ui.textEdit.fontWeight() == QFont.Bold)
        ui.toolFett.blockSignals(False)
        ui.toolKursiv.blockSignals(True)
        ui.toolKursiv.setChecked(ui.textEdit.fontItalic())
        ui.toolKursiv.blockSignals(False)
        ui.toolUnter.blockSignals(True)
        ui.toolUnter.setChecked(ui.textEdit.fontUnderline())
        ui.toolUnter.blockSignals(False)
        ui.toolFontSize.blockSignals(True)
        ui.toolFontSize.setValue(int(ui.textEdit.fontPointSize()))
        ui.toolFontSize.blockSignals(False)
        ui.toolFont.blockSignals(True)
        ui.toolFont.setCurrentFont(ui.textEdit.currentFont())
        ui.toolFont.blockSignals(False)

    def newF(self):
        Tk().withdraw()
        filename = filedialog.asksaveasfilename(title='Speicherort auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            if not filename.endswith('.txt'):
                filename += '.txt'
            open(filename, "w")
            self.addNewTab(filename)

    def openF(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename(title='Datei auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            self.addNewTab(filename)
            with open(filename, "r") as file:
                self.dict[filename].setText(file.read())

    def saveF(self):
        with open(self.currentFile, "w") as file:
            file.write(ui.textEdit.toHtml())

    def deleteF(self):
        self.closeF()
        os.remove(self.currentFile)

    def closeF(self):
        editor_comp = self.dict[self.currentFile]
        button: QtWidgets.QPushButton = editor_comp.getButton()
        button.setParent(None)
        del self.dict[self.currentFile]
        if self.dict != {}:
            firstItem = next(iter(self.dict))
            self.currentFile = firstItem
            self.dict[firstItem].buttonStatus(False)
            with open(firstItem, "r") as file:
                self.dict[firstItem].setText(file.read())
        else:
            self.currentFile = ""
            ui.textEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    editor = Editor()

    main_window.show()
    sys.exit(app.exec_())
