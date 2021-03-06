#!/usr/bin/env python2
# coding: utf-8
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
from PyQt4 import QtCore, QtGui
import sys
from gui.app import PythFinderApp

def main(argv = sys.argv):
    app = PythFinderApp(argv)
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())