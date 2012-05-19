# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/config/networkconfig.ui'
#
# Created: Fri May 18 20:58:24 2012
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
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtGui.QSpinBox(self.widget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(65535)
        self.spinBox.setProperty("value", 3128)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addWidget(self.widget)
        self.checkBox = QtGui.QCheckBox(NetworkConfigDialog)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.groupBox = QtGui.QGroupBox(NetworkConfigDialog)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(NetworkConfigDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NetworkConfigDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NetworkConfigDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NetworkConfigDialog.reject)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox.setEnabled)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.widget.setEnabled)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(NetworkConfigDialog)

    def retranslateUi(self, NetworkConfigDialog):
        NetworkConfigDialog.setWindowTitle(QtGui.QApplication.translate("NetworkConfigDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.radioNoProxy.setText(QtGui.QApplication.translate("NetworkConfigDialog", "No proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSystemPreferences.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Use system preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.radioManual.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Use Manual Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Proxy Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NetworkConfigDialog", "port", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Use authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NetworkConfigDialog", "Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NetworkConfigDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))

