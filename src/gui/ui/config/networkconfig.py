# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/config/networkconfig.ui'
#
# Created: Mon May 21 13:20:32 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NetworkConfigDialog(object):
    def setupUi(self, NetworkConfigDialog):
        NetworkConfigDialog.setObjectName(_fromUtf8("NetworkConfigDialog"))
        NetworkConfigDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(NetworkConfigDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioNoProxy = QtGui.QRadioButton(NetworkConfigDialog)
        self.radioNoProxy.setChecked(True)
        self.radioNoProxy.setObjectName(_fromUtf8("radioNoProxy"))
        self.verticalLayout.addWidget(self.radioNoProxy)
        self.radioSystemPreferences = QtGui.QRadioButton(NetworkConfigDialog)
        self.radioSystemPreferences.setObjectName(_fromUtf8("radioSystemPreferences"))
        self.verticalLayout.addWidget(self.radioSystemPreferences)
        self.radioManual = QtGui.QRadioButton(NetworkConfigDialog)
        self.radioManual.setObjectName(_fromUtf8("radioManual"))
        self.verticalLayout.addWidget(self.radioManual)
        self.widget = QtGui.QWidget(NetworkConfigDialog)
        self.widget.setEnabled(False)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineProxyHost = QtGui.QLineEdit(self.widget)
        self.lineProxyHost.setObjectName(_fromUtf8("lineProxyHost"))
        self.horizontalLayout.addWidget(self.lineProxyHost)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.spinPort = QtGui.QSpinBox(self.widget)
        self.spinPort.setMinimum(1)
        self.spinPort.setMaximum(65535)
        self.spinPort.setProperty("value", 3128)
        self.spinPort.setObjectName(_fromUtf8("spinPort"))
        self.horizontalLayout.addWidget(self.spinPort)
        self.verticalLayout.addWidget(self.widget)
        self.checkAuth = QtGui.QCheckBox(NetworkConfigDialog)
        self.checkAuth.setEnabled(False)
        self.checkAuth.setObjectName(_fromUtf8("checkAuth"))
        self.verticalLayout.addWidget(self.checkAuth)
        self.groupBox = QtGui.QGroupBox(NetworkConfigDialog)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineUser = QtGui.QLineEdit(self.groupBox)
        self.lineUser.setObjectName(_fromUtf8("lineUser"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineUser)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.linePass = QtGui.QLineEdit(self.groupBox)
        self.linePass.setEchoMode(QtGui.QLineEdit.Password)
        self.linePass.setObjectName(_fromUtf8("linePass"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.linePass)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(NetworkConfigDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NetworkConfigDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NetworkConfigDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NetworkConfigDialog.reject)
        QtCore.QObject.connect(self.checkAuth, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox.setEnabled)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.widget.setEnabled)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkAuth.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(NetworkConfigDialog)

    def retranslateUi(self, NetworkConfigDialog):
        NetworkConfigDialog.setWindowTitle(QtGui.QApplication.translate("NetworkConfigDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.radioNoProxy.setText(QtGui.QApplication.translate("NetworkConfigDialog", "No proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSystemPreferences.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Use system preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.radioManual.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Use Manual Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Proxy Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NetworkConfigDialog", "port", None, QtGui.QApplication.UnicodeUTF8))
        self.checkAuth.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Use authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NetworkConfigDialog", "Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))

