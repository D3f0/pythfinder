# encoding: utf-8

from PyQt4 import QtCore, QtGui, uic
from os import path

from networkoptions import NetworkOptionsDialog

class PythfinderMainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(PythfinderMainWindow, self).__init__()
        # Cargar la interfase gráfica
        self.setupUi()
        self.connectSignals()
        
    def connectSignals(self):
        self.actionNetwork_Options.triggered.connect(self.networkOptionsDialog.exec_)
        
        
    def setupUi(self):
        uifile = path.join(path.dirname(__file__), 'ui_files', 'mainwindow.ui')
        uic.loadUi(uifile, self)
        self.networkOptionsDialog = NetworkOptionsDialog()