# encoding: utf-8

from PyQt4 import QtCore, QtGui, uic
from os import path

class PythfinderMainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(PythfinderMainWindow, self).__init__()
        # Cargar la interfase gráfica
        uic.loadUi(path.join(path.dirname(__file__), 'ui_files', 'mainwindow.ui'), self)
        
        self.connectSignals()
        
    def connectSignals(self):
        pass
