#!/usr/bin/env python2
# coding: utf-8
from PyQt4 import QtCore, QtGui
import sys

def main(argv = sys.argv):
    app = QtGui.QApplication(argv)
    win = QtGui.QMainWindow()
    win.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())