# BTI (WORK IN PROGRESS)

##### What is this?
This program reads and displays information sent to a computer's serial port from our solar car's radio. This allows us to view and store valuable information about the car's conditions during a race. 

##### Dependencies
* PySerial
* PyQt (probably)

### Status

##### Completed Features:
* Connect to a serial device and read the output
* Parse the output from the radio (currently stored in a dictionary)

##### TODO:
* Finish figuring out what each received hex string represents
* Design the GUI
* Create the GUI (using PyQt?)
* Decide on and implement a method of permanently storing the data
* Add support for serial devices other than the radio (maybe)

### Contributing

For now, Github is probably the easiest way for us to collaborate on this project. (We could create a Blue Sky organization page to have a centralized location to share the code perhaps?)

[Quick Git Tutorial if anyone needs it](https://try.github.io/). There are also lots of resources available online if you need help, just google stuff.

##### Getting Started
1. Get Python 3 and pip. Let me know if you need any help with this step (or google it). Development may be more convenient on Linux/Mac but Windows should work as well.
2. Install PySerial: `pip install pyserial`
3. Install binary packages for [SIP](https://www.riverbankcomputing.com/software/sip/download) and [PyQt](https://www.riverbankcomputing.com/software/pyqt/download5)
4. Clone the repository:  `git clone git://github.com/jerli/BTI.git`

...to be continued
