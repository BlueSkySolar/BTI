"""
Serial Port Connections

This file contains the functions necessary to connect to serial devices.
"""

import serial
from serial.tools import list_ports

class serial_device:
    """
    Contains connection settings of a serial device

    Parameters:
        port (string) - port where the serial device is connected (ex. "COM3")

    Optional Parameters:
        baud_rate (int) - rate of information transfer (defaults to 115200)
        enabled (boolean) - if device is currently enabled
        parity (serial object) - for parity checking (defaults to None)
        stop_bits (serial object) - number of stop bits (defaults to 1)
        byte_size (serial object) - number of data bits in a byte (defaults to 8)
    """

    def __init__(self, port, baud_rate="115200", firstread=False, enabled=False,
                 parity=serial.PARITY_NONE, stop_bits=serial.STOPBITS_ONE,
                 byte_size=serial.EIGHTBITS):
        self.port = port
        self.baud_rate = baud_rate
        self.firstread = firstread
        self.parity = parity
        self.stop_bits = stop_bits
        self.byte_size = byte_size
        self.enabled = enabled

    def open_port(self):
        self.ser = serial.Serial(self.port, self.baud_rate, self.byte_size,
                                 self.parity, self.stop_bits, timeout=1.0)
        '''
        buf = SYNCH_CMD.encode('ascii')
        print(buf)
        for i in range(len(buf)):
            self.ser.write(SYNCH_CMD[i].encode('ascii'))
            time.sleep(0.005)
        self.ser.close()
        time.sleep(1)
        self.ser.open()
        self.ser.reset_input_buffer()
        '''

    def check_open(self):
        return self.ser.isOpen()


def get_serial_port():
    """
    This function returns the port that the serial device is plugged into, this may
    not always be used as there may be multiple serial devices.
    """

    for el in list_ports.comports():
        try:
            test = serial_device(el.device)
            test.open_port()
            #reset = test.ser.readline()
            line = test.ser.readline()
            if len(line) == 16:
                return el.device
                #print(len(test.ser.readline()))
            test.ser.close()
        except serial.SerialException:
            pass
    print("radio port not found")
    return


