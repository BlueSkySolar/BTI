'''
The GUI

Currently in the progress of testing plotting with PyQtGraph
'''

import sys
from PyQt4 import QtGui, QtCore
from btiplottest_ui import Ui_MainWindow
import bti
import pyqtgraph as pg
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

    time = QtCore.QTime
    time.start()
    data = deque()

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(0)

    QtGui.QApplication.instance().exec_()

#def update():
    #dict = getlatestDict()
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
