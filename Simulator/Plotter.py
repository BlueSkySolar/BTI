# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:06:56 2016
This file contains functions used to plot big data !!!!

@author: Armand Gurgu
@helper: Arnav Goel

"""

ASC_Route_Names= ["Brecksville-Dayton", "Dayton-Vincennes", "Vincennes-StLouis", "StLouis-Republic", "Republic-Topeka", "Topeka-Beatrice", "Beatrice-Scottsbluff", "Scottsbluff-Windcave"]

from packages import *

def Plot_Data_Constant_Velocity(power_array, step_array, velocity):
    '''This function accepts a list of numpy arrays stored in
    'array' and displays the data stored in the numpy arrays.'''
    global ASC_Route_Names
    for i in range (0, len(power_array)):
        plt.figure(num=(i+1), facecolor= 'w')
        plt.plot(step_array[i].as_matrix(), power_array[i].as_matrix(), label= (str(velocity)+ " km/h"))
        plt.title(ASC_Route_Names[i] + " at speed of " + str(velocity) + " km/h")
        plt.xlabel("Segment Number (#)")
        plt.ylabel("Total Mechanical and Electrical Losses (W)")
        plt.legend(loc='best')
    return        
    
def Plot_Data_Constant_Velocity_Daily(power_array, step_array, velocity_array):
    '''This function accepts a list of numpy arrays stored in
    'array' and displays the data stored in the numpy arrays.'''
    global ASC_Route_Names
    for i in range (0, len(power_array)):
        plt.figure(num=(i+1), facecolor= 'w')
        plt.plot(step_array[i].as_matrix(), power_array[i].as_matrix(), label= (str(velocity_array[i])+ " km/h"))
        plt.title(ASC_Route_Names[i] + " at speed of " + str(velocity_array[i]) + " km/h")
        plt.xlabel("Segment Number (#)")
        plt.ylabel("Total Mechanical and Electrical Losses (W)")
        plt.legend(loc='best')
    return