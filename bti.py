"""
BTI Module

This file contains the functions necessary for connecting with and
receiving data from serial devices.
"""

import serial
import time
import struct
import dicts
import datetime
import os
import csv
from collections import OrderedDict

########
# DEFINE SERIAL PORT HERE
#RADIO_PORT = "/dev/ttyUSB0"
#RADIO_PORT = "COM3"
########


# This info is taken from the old BTI,
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
OUTPUT_NAME = None
CSV_OUTPUT_TYPE = None


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


def hex_string_to_float(hex_string):
    '''
    Convert a hex string to a floating point value.

    Parameters:
        hex_string - self explanatory
    '''
    try:
        result = struct.unpack('!f', bytes.fromhex(hex_string))[0]
    except:
        result = struct.unpack('!f', hex_string.decode('hex'))[0]
    return result


def organize_data(data):
    """
    Parse raw data and output a dictionary with each distinct
    line as a key value pair.

    Parameters:
        data - string containing output from radio
    """
    # Split lines
    data = data.split('\r\n')
    data_dict = OrderedDict()
    # Store each line as dictionary key value pair
    for i in range(len(data)):
        temp = data[i].split(';')
        # print(data)
        if len(data[i]) == MESSAGE_LENGTH:
            data_dict[temp[0]] = temp[1]
    #print(data_dict)
    return data_dict


def display_radio_values(data_dict):
    '''
    Parse and print the received data.

    Parameters:
        data_dict - dictionary containing received hex values,
                    organized with the organize_data function.
                    Example format: {'01F42': '40D1B3D0'}
    '''

    # Using name_dict in dicts.py, we can correspond the received
    # hex values to data values whe want to display
    # print('Sample Data ---------')
    for el in dicts.name_dict.items():
        # Print items, converting hex values to floats
        if el[1] in data_dict:
            print("{}: {}".format(el[0], hex_string_to_float(data_dict[el[1]])))
        else:
            print("{} not found in dictionary", el[1])


def get_radio_data(radio):
    """
    Starts listening for data from radio and displays it.

    Parameters:
        radio - serial_device representing the radio

    Press Ctrl-C to end the loop and close the radio.
    """
    if radio.ser.read(1):
        radio.enabled = True
    else:
        radio.enabled = False
        print("No data received from serial port")
    try:
        while radio.enabled:
                data_dict = get_radio_dict(radio)
                display_radio_values(data_dict)
                file_output(data_dict, OUTPUT_NAME + "_RAW.txt")
                file_output(get_value_dict(data_dict), OUTPUT_NAME + "_PARSED.txt")
                csv_output(data_dict, OUTPUT_NAME + "_RAW.csv")
                csv_output(get_value_dict(data_dict), OUTPUT_NAME + "_PARSED.csv")
            # Ends when Ctrl-C is pressed
    except KeyboardInterrupt:
        # Close radio serial port.
        radio.enabled = False
        radio.ser.close()


def get_radio_dict(radio):
    '''
    return the most recent set of raw data received from the
    radio in a dictionary
    '''

    if radio.enabled:
        data = radio.ser.read_until(b'#')
        return organize_data(data.decode("utf-8"))
    else:
        print("Radio not enabled")
        return {}


def get_value_dict(in_dict):
    '''
     Interprets the dictionary returned via the radio sensor and supplies an interpreted dictionary.
    '''
    output = OrderedDict()
    for tup in dicts.name_dict.items():
        # Print items, converting hex values to floats
        if tup[1] in in_dict:
            output[tup[0]] = hex_string_to_float(in_dict[tup[1]])
    return output

def file_output(input_dict, output_name):
    '''
    Prints the input dictionary out to a text file.
    Current format is
    YYYY-MM-DD HH:MM:SS || Key: Value | Key: Value ...
    '''
    folder_path = "/" + datetime.datetime.now().strftime("%B") + "_" + str(datetime.datetime.today().day)

    if not os.path.exists(os.getcwd() + folder_path):
        os.makedirs(os.getcwd() + folder_path)

    output_file = open(os.getcwd() + folder_path + "/" + "BTI_output_" + output_name, "a")
    output_file.write("%s|| "%datetime.datetime.now())
    for key in input_dict.keys():
        output_file.write("%s: %s | " %(key,input_dict[key]))
    output_file.write("\n")

def csv_output(input_dict, output_name):
    '''
    Prints the input dictionary out to a CSV file.
    Formatting of columns is timestamp | each key
    '''
    folder_path = "/" + datetime.datetime.now().strftime("%B") + "_" + str(datetime.datetime.today().day)

    if not os.path.exists(os.getcwd() + folder_path):
        os.makedirs(os.getcwd() + folder_path)

    output_file = open(os.getcwd() + folder_path + "/" + "BTI_output_" + output_name, CSV_OUTPUT_TYPE, newline = '')
    csv_output = csv.writer(output_file)

    if os.path.getsize(os.getcwd() + folder_path + "/" + "BTI_output_" + output_name) == 0:
        l = ["time"]
        l.extend(input_dict.keys())
        csv_output.writerow(l)

    l = [datetime.datetime.now()]
    l.extend(input_dict.values())
    csv_output.writerow(l)
    output_file.close()

def get_port_and_name():
    global RADIO_PORT, OUTPUT_NAME, CSV_OUTPUT_TYPE
    OUTPUT_NAME = input("Specify output name: ")
    sys = int(input("1 if linux, 2 if windows: "))
    if sys == 1:
        RADIO_PORT = "/dev/ttyUSB" + input("Specify port 1-8: ")
        CSV_OUTPUT_TYPE = "a"
    else:
        RADIO_PORT = "COM" + input("Specify port: ")
        CSV_OUTPUT_TYPE = "wb"
    return


if __name__ == "__main__":
    get_port_and_name()
    # Create radio settings
    radio = serial_device(RADIO_PORT)
    # Open radio port
    radio.open_port()
    # Start listening and displaying data
    get_radio_data(radio)
