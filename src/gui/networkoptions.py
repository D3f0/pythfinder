from PyQt4 import QtGui, QtCore 
from PyQt4 import uic
from os import path
from ui.config.networkconfig import Ui_NetworkConfigDialog 


class NetworkOptionsDialog(QtGui.QDialog, Ui_NetworkConfigDialog):
    def __init__(self, parent = None):
        super(NetworkOptionsDialog, self).__init__(parent = parent)
        self.setupUi(self)
        self.loadConfig()
        QtGui.QApplication.instance().aboutToQuit.connect(self.saveConfig)
        
    def loadConfig(self):
        pass
    
    def saveConfig(self):
        pass