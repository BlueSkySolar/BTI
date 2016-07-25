'''
Main BTI GUI code will be in this file
'''

import sys
from PyQt4 import QtGui, QtCore, uic
import dicts
import bti
import pyqtgraph as pg
import ctypes
#import pyuic generated ui file
from main_ui import Ui_MainWindow
#import time
import main
from collections import deque

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


GRAPH_LIMIT = 50
FILE_NAME = "test"
elap_time = QtCore.QTime()
start_time = QtCore.QTime()

#window_class = uic.loadUiType("main.ui")[0]

class timeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.start = 0
        self.start_time = QtCore.QTime().addSecs(-1)
        #self.prev_time = QtCore.QTime().addSecs(-1)

    def tickStrings(self, values, scale, spacing):
#        curr = QtCore.QTime().currentTime()
#        print (curr.msecsTo(QtCore.QTime()))
#        print(self.prev_time.msecsTo(QtCore.QTime()))
#        if curr.msecsTo(QtCore.QTime()) - self.prev_time.msecsTo(QtCore.QTime()) > 2000:
#            self.start = 0
#        elif curr.msecsTo(QtCore.QTime()) - self.prev_time.msecsTo(QtCore.QTime()) > 0 and self.start == 0:
#            self.start_time = curr
#            self.start = 1
        
        ret = [self.start_time.addMSecs(value).toString('hh:mm:ss') for value in values]
        #self.prev_time = curr 
        return ret
        

class timePlotWidget(pg.PlotWidget):
    '''
    Wrapper class which replaces the x-axis values with the current time
    '''
    def __init__(self, parent=None, **kargs):
        super().__init__(axisItems={'bottom':timeAxisItem(orientation='bottom')})


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.setupUi(self)
        self.radio = None
        self.ext_devices = []
        self.filename = None
        self.times = []
        self.tables = []
        self.radio_port = ""
        self.ext_ports = []
        self.pushButton.clicked.connect(self.start_listening)
        self.statusBar().showMessage("Not Connected")

        # set up plots by looping through widget items
        self.plots = []
        # ADD NEW TABS TO THIS LIST
        tabs = [self.bmsA, self.bmsB, self.bmsC, self.emA, self.emB,
                self.emC, self.MPPTs, self.VC, self.VDa, self.VDb, self.MCa,
                self.MCb, self.MCc]
        for key, value in self.__dict__.items():
            if type(value) == main.timePlotWidget:
                # initialize plots
                # The data to be plotted is defined in the accessibleName
                # value of the plot object, with multiple data names separated
                # by commas. The units of the data is defined in accessibleDescription
                names = value.accessibleName()
                names = names.split(',')
                units = value.accessibleDescription()
                units = units.split(',')
#                parent = self.__dict__[key].parentWidget()
#                print(self.__dict__[key])
#                exec('self.'+key + "=pg.PlotWidget(parent,axisItems={'bottom':timeAxisItem(orientation='bottom')})")
#                print(self.__dict__[key])
                #self.__dict__[key] = 
                plot_item = plot(value, len(names), names, units)
                #print(next_child)
                self.plots.append(plot_item)
            elif type(value) == QtGui.QTableWidget:
                #append each table widget to a list
                self.tables.append(value)
                        
        
    def start_listening(self):
        '''start receiving data'''
        global elap_time, start_time
        if self.radio:
            # stop listening if button pressed while running
            self.radio.enabled = False
            self.radio.ser.close()
            elap_time = QtCore.QTime()
            start_time = QtCore.QTime()
            self.radio = None
            self.statusBar().showMessage("Not Connected")
            return
        
        # detect external ports
        self.ext_ports = bti.get_ext_sensor_ports()
        
        # connect to external ports
        for port in self.ext_ports:
            device = bti.serial_device(port, baud_rate=9600, timeout=2.5)
            try:
                device.open_port()
                self.ext_devices.append(device)
            except:
                pass
            
        # ask for filename
        self.filename = QtGui.QInputDialog.getText(self, 'Input', "Enter a filename for this session's saved data")
        if not self.filename:
            return
            
        # start timer
        elap_time = QtCore.QTime()
        elap_time.start()
        start_time = QtCore.QTime().currentTime()
        for plot in self.plots:
            plot.plot.getAxis('bottom').start_time = start_time
        
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
        
        self.update() # test setup for ext devices
            
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
        
        # add external device values to data dict
        for device in self.ext_devices:
            data.update(bti.get_ext_dict(device))
        
        bti.csv_output(data, self.filename[0])
        
        # update current time while
        # keeping array under limit # of items
        if len(self.times) >= GRAPH_LIMIT:
            self.times = self.times[1:]
        #self.times.append(time.elapsed())
        self.times.append(elap_time.elapsed())
        # update all plots
        for plot in self.plots:
            plot.plot.clear()
            for i in range(len(plot.names)):
                if len(plot.data[i]) >= GRAPH_LIMIT:
                        plot.data[i] = plot.data[i][1:]
                if plot.names[i] in data and data[plot.names[i]]:

                    plot.data[i].append(data[plot.names[i]])
                    if len(plot.data[i]) == len(self.times):
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
                item_name = table.accessibleName()+table.verticalHeaderItem(row).toolTip()+\
                            table.verticalHeaderItem(row).text()
                if item_name in data:
                # all bool tables in BMS C have the accessibleDescription 
                # of 'colour', which is used to know whether or not to fill 
                # the cell with colour indicators
                    if table.accessibleDescription() == 'colour':
                        table.setItem(row,0,QtGui.QTableWidgetItem(""))
                        if data[item_name] == 'Green':
                            table.item(row,0).setBackground(QtGui.QColor(0,255,0))
                        elif data[item_name] == 'Red':
                            table.item(row,0).setBackground(QtGui.QColor(255,0,0))
                        elif data[item_name] == 'Yellow':
                            table.item(row,0).setBackground(QtGui.QColor(255,255,0))
    #                    elif data[table.accessibleName() +
    #                              table.verticalHeaderItem(row).text()] == False:
                        else:
                            continue
                    else:        
                        # Since some values in the BTI have repeated names, 
                        # we can use the accessibleName value in a table to
                        # access the unique keys of each value without changing the 
                        # original name (accessibleName should be blank for others)
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
        for device in self.ext_devices:
            if device.ser:
                device.ser.close()
    
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
        self.plot.setLabel('bottom', 'Time', units='hh:mm:ss')
        plot_item = self.plot.getPlotItem()
        #print(id(plot_item.getAxis('bottom')))
        #axis_mem = (ctypes.py_object).from_address(id(plot_item.getAxis('bottom')))
        #time_axis = timeAxisItem('bottom')
        #ctypes.memmove(id)
        if units:
            if units[0]:
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
