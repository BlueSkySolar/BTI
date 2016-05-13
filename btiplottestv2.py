# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'btiplottestv2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(671, 531)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 611, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.array_plot = PlotWidget(self.centralwidget)
        self.array_plot.setGeometry(QtCore.QRect(30, 60, 291, 261))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.array_plot.sizePolicy().hasHeightForWidth())
        self.array_plot.setSizePolicy(sizePolicy)
        self.array_plot.setObjectName(_fromUtf8("array_plot"))
        self.battery_plot = PlotWidget(self.centralwidget)
        self.battery_plot.setGeometry(QtCore.QRect(350, 60, 291, 261))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery_plot.sizePolicy().hasHeightForWidth())
        self.battery_plot.setSizePolicy(sizePolicy)
        self.battery_plot.setObjectName(_fromUtf8("battery_plot"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 40, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.array_text = QtGui.QTextBrowser(self.centralwidget)
        self.array_text.setGeometry(QtCore.QRect(30, 340, 291, 141))
        self.array_text.setObjectName(_fromUtf8("array_text"))
        self.battery_text = QtGui.QTextBrowser(self.centralwidget)
        self.battery_text.setGeometry(QtCore.QRect(350, 340, 291, 141))
        self.battery_text.setObjectName(_fromUtf8("battery_text"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BTI Plot Test", None))
        self.pushButton.setText(_translate("MainWindow", "Start Listening (settings in bti.py)", None))
        self.label.setText(_translate("MainWindow", "Batteries I-V Plot", None))
        self.label_2.setText(_translate("MainWindow", "Array I-V Plot", None))

from pyqtgraph import PlotWidget
