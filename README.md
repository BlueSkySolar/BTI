# BTI (WORK IN PROGRESS)

##### What is this?
This program reads and displays information sent to a computer's serial port from our solar car's radio. This allows us to view and store valuable information about the car's conditions during a race. 

##### Dependencies
* PySerial
* PyQt (probably)


### Contributing

Git:
[Quick Git Tutorial if anyone needs it](https://try.github.io/). There are also lots of resources available online if you need help, just google stuff.

We could look into creating a Blue Sky organization page to have a centralized place for strategy code.

##### Getting Started
This assumes that you have Python 3 and pip already installed

1. Install PySerial: `pip install pyserial`
2. Install PyQt4 (The steps vary depending on operating system)
3. Clone the repository:  `git clone git://github.com/jerli/BTI.git`

##### How BTI works

The serial data sent to us from the radio on the car is received in the format displayed in [this format](radio_data.txt). The code in bti.py is able to parse this data into a dictionary as seen in radio_example.txt, but we still need to match all of the hex values with their corresponding data type by looking at the workspace file in the old BTI program. We should then be able to display real-time data from the most up to date dictionary in the GUI.

Essentially:
1. Receive data from radio(done)
2. Parse data into dictionary (mostly done)
3. Display latest data with real-time updates in a GUI (not done)
4. Store data somewhere, ex. a database (not done)

### Status

##### Completed Features:
* Connect to a serial device and read the output
* Parse the output from the radio (currently stored in a dictionary)

##### TODO:
* Finish figuring out what each received hex string represents
* Design the GUI
* Create the GUI (using PyQt?)
* Decide on and implement a method of permanently storing the data
* (maybe) Add support for serial devices other than the radio
