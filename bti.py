"""
BTI Module

This file contains the functions necessary for connecting with and
receiving data from serial devices.
"""

import serial
from serial.tools import list_ports
import time
import struct
import dicts
import datetime
import os
import csv
from collections import OrderedDict
import json

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
RADIO_PORT = None

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
                 byte_size=serial.EIGHTBITS, timeout=1.0):
        self.port = port
        self.baud_rate = baud_rate
        self.firstread = firstread
        self.parity = parity
        self.stop_bits = stop_bits
        self.byte_size = byte_size
        self.timeout = timeout
        self.enabled = enabled
        self.ser = None

    def open_port(self):
        self.ser = serial.Serial(self.port, self.baud_rate, self.byte_size,
                                 self.parity, self.stop_bits, self.timeout)
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
                parsed_dict = get_value_dict(data_dict)
                display_radio_values(data_dict)
                file_output(data_dict, OUTPUT_NAME + "_RAW.txt")
                file_output(parsed_dict, OUTPUT_NAME + "_PARSED.txt")
                csv_output(data_dict, OUTPUT_NAME + "_RAW.csv")
                csv_output(parsed_dict, OUTPUT_NAME + "_PARSED.csv")
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
        if isinstance(tup[1], str):
            if tup[1] in in_dict:
                output[tup[0]] = hex_string_to_float(in_dict[tup[1]])
            else:
                output[tup[0]] = None
        elif tup[1][1] == "long":
            if tup[1][0] in in_dict:
                output[tup[0]] = int(in_dict[tup[1][0]],16)
            else:
                output[tup[0]] = None
        elif tup[1][1] == "hex string":
            if tup[1][0] in in_dict:
                output[tup[0]] = in_dict[tup[1][0]]
            else:
                output[tup[0]] = None
        else:
            if tup[1][0] in in_dict:
                if in_dict[tup[1][0]] == tup[1][1]:
                    output[tup[0]] = True
                else:
                    output[tup[0]] = False
            else:
                output[tup[0]] = None
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
    file_path = os.getcwd() + folder_path + "/" + "BTI_output_" + output_name + ".csv"
    
    output_file = open(file_path, 'a', newline = '')
    csv_output = csv.writer(output_file)

    if os.path.getsize(file_path) == 0:
        l = ["time"]
        l.extend(input_dict.keys())
        csv_output.writerow(l)

    l = [datetime.datetime.now()]
    l.extend(input_dict.values())
    csv_output.writerow(l)
    output_file.close()

def get_port_and_name():
    global RADIO_PORT, OUTPUT_NAME, CSV_OUTPUT_TYPE
    
    #Detect radio port
    for el in list_ports.comports():
        try:
            test = serial_device(el.device)
            test.open_port()
            reset = test.ser.readline()
            line = test.ser.readline()
            if len(line) == 16:
                RADIO_PORT = el.device
                #print(len(test.ser.readline()))
            test.ser.close()
        except serial.SerialException:
            pass
    if not RADIO_PORT:
        print("radio port not found")
        return

    OUTPUT_NAME = input("Specify output name: ")
    #sys = int(input("1 if linux, 2 if windows: "))
    #if sys == 1:
    #    RADIO_PORT = "/dev/ttyUSB" + input("Specify port 1-8: ")
    #else:
    #    RADIO_PORT = "COM" + input("Specify port: ")
    
    return

def get_radio_port():
    '''
    Finds the port the radio is connected to by connecting to all available
    ports and checking if the length of one line is 16 chars.
    '''
    port = ""
    for el in list_ports.comports():
        test = serial_device(el.device)
        try:
            test.open_port()
            if test.ser.readline():
                line = test.ser.readline()
                if len(line) == 16:
                    port = el.device
                    #print(len(test.ser.readline()))
        except serial.SerialException:
            pass
        finally:
            if test.ser:
                test.ser.close()
            
    return port

def get_ext_sensor_ports():
    '''
    Finds all serial ports with sensors outputting in json.
    Connects to all available ports and attempts to parse json. If the key
    'sensor' is found, the port is added to the list.
    '''
    
    ports = []
    for el in list_ports.comports():
        test = serial_device(el.device, baud_rate=9600, timeout=2.5)
        try:
            test.open_port()
            test.ser.readline() #Potentially incomplete line
            line = test.ser.readline().decode("utf-8").strip()

            if line:
                try:
                    res = json.loads(line)
                    if "sensor" in res:
                        ports.append(el.device)
                except:
                    pass

        except:
            pass
        finally:
            if test.ser:
                test.ser.close()
            
    return ports

def get_ext_dict(device):
    try:
        return json.loads(device.ser.readline().decode("utf-8").strip())
    except:
        return {}
    
if __name__ == "__main__":
    ports = get_ext_sensor_ports()
    devices = []

    for port in ports:
        device = serial_device(port, baud_rate=9600, timeout=2.5)
        try:
            device.open_port()
            devices.append(device)
        except:
            pass
    
    for device in devices:
        try:
            print(get_ext_dict(device))
        except:
            pass
        finally:
            print(device.port)
            if device.ser:
                device.ser.close()
