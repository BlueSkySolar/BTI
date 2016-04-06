"""
BTI Radio Data Receiver
For Blue Sky Solar Racing at the University of Toronto

By:
    Jerry Li

Dependencies:
    PySerial

Tested using Python3.5
"""

import serial
import time
import struct
# import msvcrt


RADIO_PORT = "/dev/ttyUSB1"
# This info is taken straight from the old BTI, 
# and will be used to interpret received data
DATA_INDEX = 6
INDEX_LENGTH = 5
MESSAGE_LENGTH = 14
SYNCH_CMD = "<=>2E002;00000000\r\n"
MY_ID = 'E'
BROADCAST_ID = 'F'
MESSAGE_TYPE_READ = '0'
MESSAGE_TYPE_WRITE = '1'
MESSAGE_TYPE_COMMAND = '2'
MESSAGE_TYPE_STATUS = '4'
MESSAGE_TYPE_INDEX = 0
SENDER_ID_INDEX = 1
RECEIVER_ID_INDEX = 2
COMMAND_TAG_INDEX = 3
DATA_LENGTH = 8


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


def organize_data(data):
    data = data.split('\r\n')
    data_dict = {}
    for i in range(len(data)):
        temp = data[i].split(';')
        # print(data)
        if len(data[i]) == MESSAGE_LENGTH:
            data_dict[temp[0]] = temp[1]
    print(data_dict)
    return data_dict


def display_values(data_dict):
    index_list = [("Module 1 Voltage", '01F41'),
                  ("Module 2 Voltage", '01F42'),
                  ("Module 3 Voltage", '01F43'),
                  ("Module 4 Voltage", '01F44')]
    for el in index_list:
        if el[1] in data_dict:
            print("{}: {}".format(el[0], hex_string_to_float(data_dict[el[1]])))
        else:
            print("{} not found in dictionary", el[1])


'''
def get_radio_data(radio):
    if not radio.reading:
        while(radio.ser.read() != b"#"):
            continue
        radio.firstread = True
        return
    data_read = []
    return


def read_until(serial_device, char):
    leneol = len(char)
    data = bytearray()
    curr = serial_device.read(1)
    print(curr)
    while True:
        if curr:
            data += curr
            print("1", data)
            if data[-leneol:] == curr:
                break
        else:
            break
    return bytes(data)
'''


if __name__ == "__main__":
    # Create radio settings
    radio = serial_device(RADIO_PORT)


    '''
    radio.open_port()
    test = read_until(radio.ser, b'#')
    count = 1
    while (len(test)>0):
        print(count)
        print('-------')
        print(test)
        test = read_until(radio.ser, b'#')
        count += 1

    radio.ser.close()
    start = time.time()
    prevtime = start
    '''
    # Open radio port
    radio.open_port()
    radio.enabled = True
    prev = b" "

    count = 0
    # each item in data represents a set of data 
    data = []
    data.append(bytearray())
    # Not sure if while loop condition works properly atm
    try:
        while radio.enabled:
            '''
            if msvcrt.kbhit():
                key = ord(msvcrt.getch())
                if key == 27:  # ESC
                    radio.enabled = False
            '''
            # Gets latest line sent by serial device
            line = radio.ser.readline()
            # Each set of data is separated by "#""
            if b"#" in line:
                # convert from bytearray to string
                data[count] = data[count].decode("utf-8")
                #print(data[count])
                display_values(organize_data(data[count]))
                count += 1
                # create new list item once "#" is found
                data.append(bytes())
            data[count] += line
            '''
            current = time.time()
            print(current - start, current - prevtime)
            count += 1
            prevtime = current
            '''
            # prev = line
    except KeyboardInterrupt:
        radio.enabled = False
        radio.ser.close()
    # print(data)