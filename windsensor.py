from serial_connect import serial_device

#Output Info
#Option 1: M2, U1 ,O1 ,L1, P1, B3, H1 , NQ, F1, E3, T1, S4, C2, G0, K50
#Option 2/3: M2, U1, O1, L1, P1, B3, H1, NQ, F1, E2, T1, S4, C2, G0, K50

#message_format = Gill Polar Continuous     #M2
#output_units = metres/second               #U1
#measurement_mode = ??                      #Q1
#message_terminator = <CR> <LF>             #L1
#output_rate = 1                             #P1 (Hz)
baud_rate = 9600                            #B3
#power_up_message = ON                      #H1
#node_address = Q..(A to Z)                 #NQ
#data_and_parity_options = 8bit no parity   #F1
#communication_protocol = RS232             #E3
#analogue_output_type = 0                   #T1
#analogue_output_range = 0-30 m/s           #S4
#analogue_settings = 0 - 359 deg            #C2 (only for option 3)
#max_velocity = 0.05 -> 5 m/s               #K50



if __name__ == "__main__":

    windsensor = serial_device("/dev/ttyUSB0", baud_rate)
    windsensor.open_port()
    print(windsensor.check_open())

    if windsensor.check_open:
        data = windsensor.ser.readline()
        print(data)
    else:
        print("radio not enabled")

