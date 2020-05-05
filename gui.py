# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 824)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuDatei = QtWidgets.QMenu(self.menuBar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuDatei.addAction(self.actionNew)
        self.menuDatei.addAction(self.actionOpen)
        self.menuDatei.addAction(self.actionSave)
        self.menuDatei.addAction(self.actionClose)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionDelete)
        self.menuBar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionNew.setText(_translate("MainWindow", "Neue Datei"))
        self.actionDelete.setText(_translate("MainWindow", "Datei löschen"))
        self.actionOpen.setText(_translate("MainWindow", "Datei öffnen"))
        self.actionClose.setText(_translate("MainWindow", "Datei schließen"))
        self.actionSave.setText(_translate("MainWindow", "Datei speichern"))
