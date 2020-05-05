import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from tkinter import Tk
from tkinter import filedialog


class Editor:
    def newF(self):
        Tk().withdraw()
        filename = filedialog.asksaveasfilename(title='Speicherort auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            if not filename.endswith('.txt'):
                filename += '.txt'
            open(filename, "w")

    def openF(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename(title='Speicherort auswaehlen', filetypes=[('Text', '*.txt')])
        if filename:
            print(filename)

    def deleteF(self):
        print("close")

    def closeF(self):
        print("close")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    editor = Editor()
    ui.actionOpen.triggered.connect(editor.openF)
    ui.actionNew.triggered.connect(editor.newF)
    ui.actionDelete.triggered.connect(editor.deleteF)
    ui.actionClose.triggered.connect(editor.closeF)

    main_window.show()
    sys.exit(app.exec_())
