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
        self.tables = []
        self.radio_port = ""
        self.pushButton.clicked.connect(self.start_listening)
        self.statusBar().showMessage("Not Connected")

        # set up plots by looping through widget items
        self.plots = []
        # ADD NEW TABS TO THIS LIST
        tabs = [self.bmsA, self.bmsB, self.bmsC, self.emA, self.emB,
                self.emC, self.MPPTs]
        for tab in tabs:
            for child in tab.children():
                for next_child in child.children():
                    if type(next_child) == pg.widgets.PlotWidget.PlotWidget:
                        # initialize plots
                        # The data to be plotted is defined in the accessibleName
                        # value of the plot object, with multiple data names separated
                        # by commas. The units of the data is defined in accessibleDescription 
                        names = next_child.accessibleName()
                        names = names.split(',')
                        units = next_child.accessibleDescription()
                        units = units.split(',')
                        plot_item = plot(next_child, len(names), names, units)
                        self.plots.append(plot_item)
                    elif type(next_child) == QtGui.QTableWidget:
                        #append each table widget to a list
                        self.tables.append(next_child)
                        
        
    def start_listening(self):
        '''start receiving data'''
        global time
        if self.radio:
            # stop listening if button pressed while running
            self.radio.enabled = False
            self.radio.ser.close()
            time = None
            self.radio = None
            self.statusBar().showMessage("Not Connected")
            return
        
        # ask for filename
        self.filename = QtGui.QInputDialog.getText(self, 'Input', "Enter a filename for this session's saved data")
        if not self.filename:
            return
            
        # start timer
        time = QtCore.QTime()
        time.start()
        
        # detect radio_port
        if not self.radio_port:
            self.radio_port = bti.get_radio_port()
        temp = QtGui.QInputDialog.getText(self, 'Enter Serial Port', "Port:\n\n(Windows:COMx  Linux:/dev/ttyUSBx)", text = self.radio_port)
        if temp[1]:
            radio_port = temp[0]
        else:
            self.statusBar().showMessage("Radio Port Not Found")
            return

        #connect to radio
        try:
            self.radio = bti.serial_device(radio_port)
            self.radio.open_port()
            self.radio.enabled = True
            if self.radio.ser.read(1):
                self.statusBar().showMessage("Connected to " + radio_port)
            else:
                self.radio.enabled = False
                self.radio.ser.close()
                self.radio = None
                return
        except:
            self.statusBar().showMessage("Radio Port Not Found")
        
        try:
            ####################### temporarily saving raw data for testing
            with open("raw_data.txt", "a") as text_file:
                temp = self.radio.ser.read_until(b'#')
                text_file.write(self.radio.ser.read_until(b'#').decode("utf-8"))
            #######################
            while self.radio and self.radio.enabled:
                self.update()
                QtCore.QCoreApplication.processEvents()
        except KeyboardInterrupt:
            self.radio.enabled = False
            self.radio.ser.close()
            self.radio = None
    
    def update(self):
        '''update everything with up-to-date values'''
        data = bti.get_value_dict(bti.get_radio_dict(self.radio))
        bti.csv_output(data, self.filename[0])
        
        # update current time while
        # keeping array under limit # of items
        if len(self.times) >= GRAPH_LIMIT:
            self.times = self.times[1:]
        self.times.append(time.elapsed())

        # update all plots
        for plot in self.plots:
            plot.plot.clear()
            for i in range(len(plot.names)):
                if plot.names[i] in data and data[plot.names[i]]:
                    if len(plot.data[i]) >= GRAPH_LIMIT:
                        plot.data[i] = plot.data[i][1:]
                    plot.data[i].append(data[plot.names[i]])
                    if len(plot.plot.plotItem.legend.items) != len(plot.names):
                        plot.plot.plot(self.times, plot.data[i], pen=(i, len(plot.names)), name=plot.names[i])
                    else:
                        plot.plot.plot(self.times, plot.data[i], pen=(i, len(plot.names)))
                else:
                    plot.data[i].append(0.0)

                    
        #go through each table and update the value corresponding to the row title
        for table in self.tables:
            for row in range(table.rowCount()):
                # sometimes rows are used as titles, so those are skipped
                if table.verticalHeaderItem(row).toolTip() == "i":
                    continue
                # all bool tables in BMS C have the accessibleDescription 
                # of 'colour', which is used to know whether or not to fill 
                # the cell with colour indicators
                elif table.accessibleDescription() == 'colour':
                    table.setItem(row,0,QtGui.QTableWidgetItem(""))
                    if data[table.accessibleName() + 
                            table.verticalHeaderItem(row).text()] == True:
                        table.item(row,0).setBackground(QtGui.QColor(0,255,0))
                    elif data[table.verticalHeaderItem(row).text()] == False:
                        table.item(row,0).setBackground(QtGui.QColor(255,0,0))
                    else:
                        pass
                else:        
                    # Since some values in the BTI have repeated names, 
                    # we can use the accessibleName value in a table to
                    # access the unique keys of each value without changing the 
                    # original name (accessibleName should be blank for others)
                    item_name = table.accessibleName()+table.verticalHeaderItem(row).toolTip()+\
                                table.verticalHeaderItem(row).text()
                    item = QtGui.QTableWidgetItem(str(data[item_name]))
                    if item_name not in dicts.name_dict:
                        print(item_name, "value not found")
                    table.setItem(row,0,item)
            
    def closeEvent(self, *args, **kwargs):
        super(QtGui.QMainWindow, self).closeEvent(*args, **kwargs)
        if self.radio:
            if self.radio.enabled:
                self.radio.enabled = False
                self.radio.ser.close()
                self.radio = None
    
class plot:
    '''Stores plot-related variables'''
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
        self.data = []
        for i in range(len(self.names)):
            self.data.append([])
            
        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MainWindow(None)
    myWindow.show()
    app.exec_()
