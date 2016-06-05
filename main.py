'''
Main BTI GUI code will be in this file
'''

import sys
from PyQt4 import QtGui, QtCore, uic

window_class = uic.loadUiType("main.ui")[0]

class MainWindow(QtGui.QMainWindow, window_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # set up plots and list views by looping through widget items
        # button event handlers wil go here
        
    def start_listening():
        pass
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MainWindow(None)
    myWindow.show()
    app.exec_()
