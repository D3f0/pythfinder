# encoding: utf-8

from PyQt4 import QtCore, QtGui, uic, QtWebKit, QtNetwork
from os import path
from ui.mainwindow import Ui_MainWindow
from networkoptions import NetworkOptionsDialog
import os
from collections import OrderedDict
import PyQt4
class ChromUserAgentPage(QtWebKit.QWebPage):
    def userAgentForUrl(self, url):
        return "Chrome/1.0"
    

class PythfinderMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PythfinderMainWindow, self).__init__()
        # Cargar la interfase gráfica
        self.setupUi(self)
        self.connectSignals()
        self.setupBrowser()
        
        
        
    MAP_TYPES = OrderedDict(
        ROADMAP = 'ROADMAP',
        SATELLITE = 'SATELLITE',
        HYBRID = 'HYBRID',
        TERRAIN = 'TERRAIN',
    )
    
    def connectSignals(self):
        self.actionNetwork_Options.triggered.connect(self.networkOptionsDialog.exec_)
        self.networkOptionsDialog.accepted.connect(self.applyProxyParams)
        self.pushSnapshot.pressed.connect(self.takeSnapshot)
    
    def setupUi(self, instance):
        super(PythfinderMainWindow, self).setupUi(instance)
        for key, val in self.MAP_TYPES.items():
            self.comboMapType.addItem(key.title(), userData=val)
        # Dialgo de configración de red
        self.networkOptionsDialog = NetworkOptionsDialog()
        
    def setupBrowser(self):
        self.webView.setPage(ChromUserAgentPage())
        self.webView.setHtml(self.getInitialHTML())
        self.webView.loadStarted.connect(lambda : self.statusBar().showMessage("Cargando..."))
        self.webView.loadProgress[int].connect(lambda progress :self.statusBar().showMessage("Cargando %d" % progress))
        self.webView.loadFinished.connect(lambda :self.statusBar().showMessage("Carga completada."))
        
        
    def getInitialHTML(self):
        template = os.path.join(QtGui.qApp.instance().getTemplatePath(),
                                'initial.html')
        
        with open(template) as f:
            data = f.read()
        return data
    
    @PyQt4.QtCore.pyqtSignature('int')
    def on_comboMapType_activated(self, index):
        mapTypeStr = self.comboMapType.itemData(index)
        self.statusBar().showMessage("Estableciendo tipo %s" % mapTypeStr, 1000)
        self.setMapTypeId(mapTypeStr)
    
    def setMapTypeId(self, mapType):
        self.processJS('MAP.setMapTypeId(google.maps.MapTypeId.%s);' % mapType)
    
    def processJS(self, js):
        js = '''
        try {
            %(js)s
        } catch (e) {
            alert("No se puedo ejecutar %(js)s por "+e); 
        }
        ''' % {'js':js}
        self.webView.page().mainFrame().evaluateJavaScript(js)
    
    def refreshWebView(self):
        ''' Refrescar '''
        
        self.webView.setHtml(self.getInitialHTML())
        
    def applyProxyParams(self):
        dlg = self.networkOptionsDialog
        
        if dlg.radioManual.isChecked():
            #===================================================================
            # Proxy Manual
            #===================================================================
            proxy = QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.HttpProxy)
            proxy.setHostName(dlg.lineProxyHost.text())
            proxy.setPort(dlg.spinPort.value())
            if dlg.checkAuth.isChecked():
                proxy.setUser(dlg.lineUser.text())
                proxy.setPassword(dlg.linePass.text())
                
        elif dlg.radioSystemPreferences.isChecked():
            proxy = QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.DefaultProxy)
        else:
            proxy = QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.NoProxy)
        
        QtNetwork.QNetworkProxy.setApplicationProxy( proxy )
        
        self.refreshWebView()
    
    @QtCore.pyqtSignature('')
    def takeSnapshot(self):
        '''Tomar la captura de pantalla'''
        f = QtGui.QFileDialog.getOpenFileName(self, "Guardar imagen", "", 
                                          "Images (*.png *.jpg *.xpm)")
        
        if f:
            if os.path.splitext(f)[1] not in ('png', 'jpg', 'xpm'):
                f = f + '.png'
            snapshot = QtGui.QPixmap.grabWidget(self.webView)
            snapshot.save(f)
    
    def updateTitleWithSize(self):
        webview_size = self.webView.size()
        self.setWindowTitle(u"Tamaño %sx%s" % (webview_size.width(), webview_size.height()))
    
    def resizeEvent(self, event):
        self.updateTitleWithSize()
        super(PythfinderMainWindow, self).resizeEvent(event)
        
    def showEvent(self, event):
        super(PythfinderMainWindow, self).showEvent(event)
        self.updateTitleWithSize()