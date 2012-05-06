from PyQt4 import QtGui

class PythFinderApp(QtGui.QApplication):
    def __init__(self, args):
        super(PythFinderApp, self).__init__(args)
        self.setupGui()
        
        
    def setupGui(self):
        pass
    
    
    