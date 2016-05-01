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

app = None;
ui = None;
win = None;
p = None;

def makeUI(): #this method is so jank it hurts my soul
    global app, ui, win, p

    app = QtGui.QApplication(sys.argv) #QtGui object

    #Setting up window stuff
    win = QtGui.QMainWindow()
    win.setWindowTitle('pyqtgraph example: ScatterPlotSpeedTest')
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()

    #setup actual plot
    p = ui.plot
    p.setLabel('left', 'Avg Module Voltage', units='V')
    p.setLabel('bottom', 'Time', units='s')

    #getting random crap from numpy
    #x = np.arange(1000)
    x = [1,2,3,4,5,6,7,8,9]
    #y = np.random.normal(size=(3, 1000))
    y = [[5,5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6,6],[8,8,8,8,8,8,8,8,8]]
    for i in range(3):
        p.plot(x, y[i], pen=(i, 3))

    '''
    time = QtCore.QTime
    time.start()
    data = deque()

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(0)
    '''
    QtGui.QApplication.instance().exec_()

def updateGraph(inputDict):
    '''
    Takes in the dictionary and adds it to
    '''

#def update():
    #dict = getlatestDict()
    #addnewpointstoplot()

def file_output(input_dict):
    '''
    Prints the input dictionary out to a text file.
    Current format is
    YYYY-MM-DD HH:MM:SS || Key: Value | Key: Value ...
    '''
    output_file = open("output.txt", "a")
    output_file.write("%s|| "%datetime.datetime.now())
    for key in input_dict.keys():
        output_file.write("%s: %s | " %(key,input_dict[key]))
    output_file.write("\n")

if __name__ == '__main__':
    makeUI()

