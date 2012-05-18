from PyQt4 import QtGui, QtCore

class PythFinderApp(QtGui.QApplication):
    def __init__(self, args):
        super(PythFinderApp, self).__init__(args)
        self.setupGui()
        self.mainWindow.show()
        self.mainWindow.webView.setUrl(QtCore.QUrl('http://maps.google.com'))
        
    def setupGui(self):
        from mainwindow import PythfinderMainWindow
        self.mainWindow = PythfinderMainWindow()
        
    
        
    
    
    