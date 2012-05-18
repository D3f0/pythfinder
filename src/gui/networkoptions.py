from PyQt4 import QtGui, QtCore 
from PyQt4 import uic
from os import path


class NetworkOptionsDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        super(NetworkOptionsDialog, self).__init__(parent = parent)
        self.setupUi()
        self.loadConfig()
        QtGui.QApplication.instance().aboutToQuit.connect(self.saveConfig)
        
    def setupUi(self):
        uifile = path.join(path.dirname(__file__), 'ui_files', 'networkconfig.ui')
        uic.loadUi(uifile, self)
    
    def loadConfig(self):
        pass
    
    def saveConfig(self):
        pass