# BTI (WORK IN PROGRESS)

##### What is this?
This program reads and displays information sent to a computer's serial port from our solar car's radio. This allows us to view and store valuable information about the car's conditions during a race. 

##### Dependencies
* PySerial
* PyQt 
* PyQtGraph

### Contributing

Git:
[Quick Git Tutorial if anyone needs it](https://try.github.io/). There are also lots of resources available online if you need help, or ask in the group chat.

##### Getting Started
Python 3 will be used. A virtual environment manager like [conda](http://conda.pydata.org/docs/download.html) may be helpful.

1. Clone the repository:  `git clone https://github.com/BlueSkySolar/BTI.git`
2. Install PySerial: `pip install pyserial`
3. Install PyQt4 (The steps vary depending on operating system) (if using conda `conda install pyqt`)
4. Install PyQtGraph `pip install pyqtgraph`

###### On Windows, you can install [WinPython](http://winpython.github.io/), which will include all of the required modules.

##### How BTI works

The serial data sent to us from the radio on the car is received in the format displayed in [this format](radio_data.txt). The code in bti.py is able to parse this data into a dictionary as seen in [radio_example](radio_example.txt), but we still need to match all of the hex values with their corresponding data type by looking at the [workspace file](legacy_workspace_file.txt) in the old BTI program. We should then be able to display real-time data with proper labeling in the GUI.

Basically:

1. Receive data from radio(done)
2. Parse data (mostly done)
3. Display latest data with real-time updates in a GUI (not done)
4. Store data somewhere, ex. a database (not done)

### Status

##### Completed Features:
* Connect to a serial device and read the output
* Parse the output from the radio (currently stored in a dictionary)

##### TODO:
* Finish figuring out what each received hex string  line represents
* Design the GUI
* Create the GUI (Qt Designer for layout, export to PyQt) This includes displaying all of the data, including a few plots.
* Decide on and implement a method of permanently storing the data
* ???
