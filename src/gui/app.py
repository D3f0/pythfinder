from PyQt4 import QtGui, QtCore

class PythFinderApp(QtGui.QApplication):
    def __init__(self, args):
        super(PythFinderApp, self).__init__(args)
        self.setupGui()
        self.mainWindow.show()
        
    def setupGui(self):
        from mainwindow import PythfinderMainWindow
        self.mainWindow = PythfinderMainWindow()
        
    def getTemplatePath(self):
        import os
        path = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(path, '..', 'templates'))
        
    
    
    