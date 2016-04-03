"""
BTI Serial Data Receiver 
For Blue Sky Solar Racing at the University of Toronto

By:
Jerry Li
"""

import serial
import time
import struct

RADIO_PORT = "COM4"
DATA_INDEX = 6
MESSAGE_LENGTH = 14
SYNCH_CMD = "<=>2E002;00000000\r\n"


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

    def __init__(self, port, baud_rate="115200", enabled=False,
                 parity=serial.PARITY_NONE, stop_bits=serial.STOPBITS_ONE,
                 byte_size=serial.EIGHTBITS):
        self.port = port
        self.baud_rate = baud_rate
        self.enabled = enabled
        self.parity = parity
        self.stop_bits = stop_bits
        self.byte_size = byte_size

    def open_port(self):
        self.ser = serial.Serial(self.port, self.baud_rate, self.byte_size,
                                 self.parity, self.stop_bits, write_timeout=1.0)
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


def hex_string_to_float(hex_string):
    try:
        result = struct.unpack('!f', bytes.fromhex(hex_string))[0]
    except:
        result = struct.unpack('!f', hex_string.decode('hex'))[0]
    return result

# def get_radio_data(radio):


if __name__ == "__main__":
    # Create radio settings
    radio = serial_device(RADIO_PORT)

    # Open radio port
    radio.open_port()
    prev = " "
    start = time.time()
    prevtime = start
    count = 0
    while(prev != ""):
        line = radio.ser.readline()
        #if (line):
        print(line)
        current = time.time()
        print(current - start, current - prevtime)
        count += 1
        prevtime = current
        prev = line
    print(count)
