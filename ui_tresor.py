# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tresor.ui'
#
# Created: Tue Nov 18 23:39:42 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Tresor(object):
    def setupUi(self, Tresor):
        Tresor.setObjectName(_fromUtf8("Tresor"))
        Tresor.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Tresor)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Tresor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Tresor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Tresor.reject)
        QtCore.QMetaObject.connectSlotsByName(Tresor)

    def retranslateUi(self, Tresor):
        Tresor.setWindowTitle(QtGui.QApplication.translate("Tresor", "Tresor", None, QtGui.QApplication.UnicodeUTF8))

