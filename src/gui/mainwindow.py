# encoding: utf-8

from PyQt4 import QtCore, QtGui, uic
from os import path
from ui.mainwindow import Ui_MainWindow
from networkoptions import NetworkOptionsDialog

class PythfinderMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PythfinderMainWindow, self).__init__()
        # Cargar la interfase gráfica
        self.setupUi(self)
        self.connectSignals()
    
    def connectSignals(self):
        pass
    
        
