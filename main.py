'''
The GUI

Currently in the progress of testing plotting with PyQtGraph
'''

import sys
from PyQt4 import QtGui, QtCore
from btiplottest_ui import Ui_MainWindow
import bti



def main():

    app = QtGui.QApplication(sys.argv)

    win = QtGui.QMainWindow()
    # win.setWindowTitle('pyqtgraph example: ScatterPlotSpeedTest')
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()

    p = ui.plot
    p.setLabel('left', 'Avg Module Voltage', units='V')
    p.setLabel('bottom', 'Time', units='s')

    QtGui.QApplication.instance().exec_()


#def update():



if __name__ == '__main__':
    main()
