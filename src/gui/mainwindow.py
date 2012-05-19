# encoding: utf-8

from PyQt4 import QtCore, QtGui, uic
from os import path
from ui.mainwindow import Ui_MainWindow
from networkoptions import NetworkOptionsDialog
import os

class PythfinderMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PythfinderMainWindow, self).__init__()
        # Cargar la interfase gráfica
        self.setupUi(self)
        self.setupBrowser()
    
    
    def setupBrowser(self):
        self.webView.setHtml(self.getInitialHTML())
        
    def getInitialHTML(self):
        template = os.path.join(QtGui.qApp.instance().getTemplatePath(),
                                'initial.html')
        
        with open(template) as f:
            data = f.read()
        return data