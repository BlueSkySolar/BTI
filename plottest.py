'''
The GUI

Currently in the progress of testing plotting with PyQtGraph

Code is kind of messy for now, we will move to a more organized
object-oriented approach soon.
'''

import sys
from PyQt4 import QtGui, QtCore
from btiplottestv2 import Ui_MainWindow
import bti
import pyqtgraph as pg
#import numpy as np
#from collections import deque
import datetime  # for text data outputs
import atexit

GRAPH_POINT_LIMIT = 100
app = None
ui = None
win = None
p_power = None
p_array = None
time = None
radio = None
power_text = None
array_text = None
x1 = [] 
y1 = [[],[],[],[],[],[],[],[],[]] # panel power values 

x2 = []
y2 = [] # variable naming will improve in the future when we start using objects lol 


def makeUI():  # this method is so jank it hurts my soul
    global app, ui, win, p_power, p_array, time, power_text, array_text

    app = QtGui.QApplication(sys.argv)  # QtGui object

    # Setting up window stuff
    win = QtGui.QMainWindow()
    win.setWindowTitle('pyqtgraph example: ScatterPlotSpeedTest')
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()

    # setup actual plot
    p_power = ui.power_plot
    p_power.setLabel('left', 'Power', units='W')
    p_power.setLabel('bottom', 'Time', units='s')
    p_power.addLegend()

    power_text = ui.power_text
    power_text.setPlainText("No Data")

    p_array = ui.array_plot
    p_array.setLabel('left', 'Voltage', units='V')
    p_array.setLabel('bottom', 'Current', units='A')
    p_array.addLegend()

    array_text = ui.array_text
    array_text.setPlainText("No Data")

    button = ui.pushButton
    button.clicked.connect(start_listening)

    atexit.register(goodbye)
    # start_listening(radio)
    QtGui.QApplication.instance().exec_()


def start_listening():
    global radio, time
    # start timer
    time = QtCore.QTime()
    time.start()

    # connect to radio
    if radio:
        radio.enabled = False
        radio.ser.close()
        radio = None
        return

    radio = bti.serial_device(bti.RADIO_PORT)
    radio.open_port()
    if radio.enabled:
        radio.enabled = False
    elif radio.ser.read(1):
        radio.enabled = True
    else:
        radio.enabled = False
        print("No data received from serial port")

    try:
        while radio.enabled:
            update(radio)
            QtCore.QCoreApplication.processEvents()
    except KeyboardInterrupt:
        # Close radio serial port.
        radio.enabled = False
        radio.ser.close()


def update(radio):
    global x1, y1, x2, y2, p_power, power_text, p_array, array_text, time
    data = bti.get_value_dict(bti.get_radio_dict(radio))
    power_string = ""
    for i in range(10):
        name = "Panel " + str(i) + " Power (W)"
        if name in data:
            while(len(x1) >= GRAPH_POINT_LIMIT):
                x1 = x1[1:]
                y1[i] = y1[i][1:]
            x1.append(time.elapsed())
            y1[i].append(data[name])
            power_string += name + " : " + str(data[name]) + "\n"
            p_power.plot(x1, y1[i], pen=(i, 9), name=name)
        else:
            power_string += name + " : N/A\n"
    power_text.setPlainText(power_string)

    arr_bus_i = "Arr Bus Current (A)"
    arr_bus_v = "Arr Bus Voltage (V)"

    arr_string = ""
    if arr_bus_i in data:
        while(len(x2) >= GRAPH_POINT_LIMIT):
            x2 = x2[1:]
            y2 = y2[1:]
        x2.append(data[arr_bus_i])
        y2.append(data[arr_bus_v])
        arr_string += arr_bus_i + " : " + str(data[arr_bus_i]) + "\n"
        arr_string += arr_bus_v + " : " + str(data[arr_bus_v]) + "\n"
        p_array.plot(x2, y2, name=arr_bus_v + " vs " + arr_bus_i)
    else:
        arr_string = "Arr Bus Current N/A"
    if "EM_ARR Temp (deg C)" in data:
        arr_string += "EM_ARR Temp (deg C)" + " : " + str(data["EM_ARR Temp (deg C)"]) + "\n"
    array_text.setPlainText(arr_string)

    bti.file_output(data, "plottest.txt")


# newer version of file_output function in bti.py
'''
def file_output(input_dict, output_name):
    
    Prints the input dictionary out to a text file.
    Current format is
    YYYY-MM-DD HH:MM:SS || Key: Value | Key: Value ...
    
    output_file = open(output_name, "a")
    output_file.write("%s|| " % datetime.datetime.now())
    for key in input_dict.keys():
        output_file.write("%s: %s | " % (key, input_dict[key]))
    output_file.write("\n")
'''

def goodbye():
    global radio
    if radio:
        if radio.enabled:
            radio.enabled = False
            radio.ser.close()
            radio = None

if __name__ == '__main__':
    makeUI()
