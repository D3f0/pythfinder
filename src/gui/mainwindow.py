# encoding: utf-8

from PyQt4 import QtCore, QtGui, uic, QtWebKit
from os import path
from ui.mainwindow import Ui_MainWindow
from networkoptions import NetworkOptionsDialog
import os
from collections import OrderedDict
class ChromUserAgentPage(QtWebKit.QWebPage):
    def userAgentForUrl(self, url):
        return "Chrome/1.0"
    

class PythfinderMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PythfinderMainWindow, self).__init__()
        # Cargar la interfase gráfica
        self.setupUi(self)
        
        self.setupBrowser()
        
    MAP_TYPES = OrderedDict(
        HYBRID = 'HYBRID',
        ROADMAP = 'ROADMAP',
        SATELLITE = 'SATELLITE',
        TERRAIN = 'TERRAIN',
    )
    
    def setupUi(self, instance):
        super(PythfinderMainWindow, self).setupUi(instance)
        for key, val in self.MAP_TYPES.items():
            self.comboMapType.addItem(key.title(), userData=val)
    
    def setupBrowser(self):
        self.webView.setPage(ChromUserAgentPage())
        self.webView.setHtml(self.getInitialHTML())
        
    def getInitialHTML(self):
        template = os.path.join(QtGui.qApp.instance().getTemplatePath(),
                                'initial.html')
        
        with open(template) as f:
            data = f.read()
        return data
    

    def processJS(self, js):
        js = '''
        try {
            %(js)s
        } catch (e) {
            alert("No se puedo ejecutar %(js)s por "+e); 
        }
        ''' % {'js':js}
        self.webView.page().mainFrame().evaluateJavaScript(js) 