'''
Main BTI GUI code will be in this file
'''

import sys
from PyQt4 import QtGui, QtCore, uic
import dicts
import bti
import pyqtgraph as pg
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


GRAPH_LIMIT = 100
FILE_NAME = "test"
time = None


window_class = uic.loadUiType("main.ui")[0]

class MainWindow(QtGui.QMainWindow, window_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.setupUi(self)
        self.radio = None
        self.filename = None
        self.times = []
        # button event handlers wil go here
        self.pushButton.clicked.connect(self.start_listening)

        # set up plots by looping through widget items
        self.plots = []
        # does not loop through all tabs properly yet
        tabs = [self.bmsA, self.bmsB]
        for tab in tabs:
            for child in tab.children():
                for next_child in child.children():
                    if type(next_child) == pg.widgets.PlotWidget.PlotWidget:
                        #initialize plots
                        names = next_child.accessibleName()
                        names = names.split(',')
                        units = next_child.accessibleDescription()
                        units = units.split(',')
                        plot_item = plot(next_child, len(names), names, units)
                        self.plots.append(plot_item)
                        #next_child.setLabel('bottom', 'Time', units='s')
                        #next_child.setLabel('left', units[0], units=units[1])
                        #next_child.setTitle(next_child.accessibleName())
        print(self.plots)
        
    def start_listening(self):
        # stop listening if button pressed while running
        global time
        if self.radio:
            self.radio.enabled = False
            self.radio.ser.close()
            time = None
            self.radio = None
            self.statusBar().showMessage("Not Connected")
            return
        
        # ask for filename
        self.filename = QtGui.QInputDialog.getText(self, 'Input', "Enter a filename for this session's saved data")
        print(self.filename)
        if not self.filename:
            return
            
        # start timer
        time = QtCore.QTime()
        time.start()
        
        # detect radio_port
        radio_port = bti.get_radio_port()
        if not radio_port:
            self.statusBar().showMessage("No Port Found")
            return
        else:
            self.statusBar().showMessage("Connected to " + radio_port)

        #connect to radio
        self.radio = bti.serial_device(radio_port)
        self.radio.open_port()
        self.radio.enabled = True
        
        try:
            while self.radio.enabled:
                self.update()
                QtCore.QCoreApplication.processEvents()
        except KeyboardInterrupt:
            self.radio.enabled = False
            self.radio.ser.close()
    
    def update(self):
        data = bti.get_value_dict(bti.get_radio_dict(self.radio))
        bti.csv_output(data, self.filename[0])
        
        if len(self.times) >= GRAPH_LIMIT:
            self.times = self.times[1:]
        self.times.append(time.elapsed())

        for plot in self.plots:
            for i in range(len(plot.names)):
                if plot.names[i] in data and data[plot.names[i]]:
                    if len(plot.data[i]) >= GRAPH_LIMIT:
                        plot.data[i] = plot.data[i][1:]
                    plot.data[i].append(data[plot.names[i]])
                    print(plot.data[i], self.times)
                    if len(plot.data[i]) == 1:
                        plot.plot.plot(self.times, plot.data[i], pen=(i, len(plot.names)), name=plot.names[i])
                    else:
                        plot.plot.plot(self.times, plot.data[i], pen=(i, len(plot.names)))
                else:
                    plot.data[i].append(0.0)
        pass
    
    
    
class plot:
    def __init__(self, plot, num_values, names, units):
        '''
        Intialize plot object
        
        Parameters:
            plot - pyqtgraph PlotWidget item
            num_values (int) - number of values to be plotted
            names - iterable of names of values to be plotted
            units - iterable containing units of items, ex. (Voltage, V)
        '''
        self.num_values = num_values
        self.names = names
        self.plot = plot
        self.plot.addLegend()
        self.plot.setLabel('bottom', 'Time', units='s')
        if units:
            self.plot.setLabel('left', units[0], units = units[1])
        self.hex_keys = []
        for el in names:
            self.hex_keys.append(dicts.name_dict[el])
        print(self.hex_keys)
        self.data = []
        for i in range(len(self.names)):
            self.data.append([])
            
        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MainWindow(None)
    myWindow.show()
    app.exec_()
