'''
The GUI

Currently in the progress of testing plotting with PyQtGraph
'''

import sys
from PyQt4 import QtGui, QtCore
from btiplottest_ui import Ui_MainWindow
import bti
import pyqtgraph as pg
import numpy as np
from collections import deque
import datetime #for text data outputs

def makeUI():
    app = QtGui.QApplication(sys.argv)

    win = QtGui.QMainWindow()
    win.setWindowTitle('pyqtgraph example: ScatterPlotSpeedTest')
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()

    p = ui.plot
    p.setLabel('left', 'Avg Module Voltage', units='V')
    p.setLabel('bottom', 'Time', units='s')

    x = np.arange(1000)
    y = np.random.normal(size=(3, 1000))
    for i in range(3):
        p.plot(x, y[i], pen=(i, 3))

    time = QtCore.QTime()
    time.start()

    QtGui.QApplication.instance().exec_()

def update():
    dict = getlatestDict()
    #addnewpointstoplot()

def fileOutput(inputDict):
    '''
    Prints the input dictionary out to a text file.
    Current format is
    YYYY-MM-DD HH:MM:SS || Key: Value | Key: Value ...
    '''
    outputFile = open("output.txt", "a")
    outputFile.write("%s|| "%datetime.datetime.now())
    for key in inputDict.keys():
        outputFile.write("%s: %s | " %(key,inputDict[key]))
    outputFile.write("\n")

if __name__ == '__main__':
    makeUI()
