# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:44:49 2016

@author: Armand Gurgu

This file contains the code that can be used to run simulation files given a
velocity profile.

"""

from packages import *
from PowerGrav import *
from simulator_constants import *


def Generate_Velocity_Profile(low_speed, high_speed, units):
    '''This function can be used to simulate a velocity profile
    for simulation purposes. Generates a profile based on numpy's random
    number generator capabilities.'''
    global f_hill_data
    velocity_profiles=list()
    for i in range (0, len(f_hill_data)):
        if units == 'si':    
            temp= np.random.randint(low_speed, high_speed, size=(np.shape(f_hill_data[i].iloc[:,1])[0],1))
            velocity_profiles.append(temp/3.6)
        else:
            temp= np.random.randint(low_speed, high_speed, size=(np.shape(f_hill_data[i].iloc[:,1])[0],1))
            velocity_profiles.append(temp)
    return velocity_profiles
    
def Read_Velocity_Profile(file):
    '''This function reads in a predefined velocity profile from
    an excel sheet or CSV file and outputs a list of numpy arrays for each column day
    '''
    path= os.getcwd()
    dir_files= os.listdir(path)
    for i in dir_files:
        form= i.split(".")
        if (i == file) and "xlsx" in form:
            data= pan.read_excel(i, delimiter= ",", keep_default_na= True)
            return data
        elif (i==file) and "csv" in form:
            data= pan.read_csv(i, delimiter= ",", keep_default_na= True)
            return data
def Generate_Constant_Velocity_Profile(speed, units):
    '''This function can be used to generate a constant velocity profile
    for the ASC race.'''
    global f_hill_data
    velocity_profiles=list()
    for i in range (0, len(f_hill_data)):
        if units == "si":
            temp= np.zeros((np.shape(f_hill_data[i].iloc[:,1])[0]))
            temp[:]= speed/3.6
            speed_limits= (f_hill_data[i].iloc[:,3] / 3.6).as_matrix()
            print(speed_limits.shape)
            print(temp.shape)
            collision_indices= np.where(temp > speed_limits)[0]
            if collision_indices.shape[0] != 0: #Deal with cases where velocity is greater than speed limit.
                temp[collision_indices]= speed_limits[collision_indices]
            velocity_profiles.append(temp)
        else:
            temp= np.zeros((np.shape(f_hill_data[i].iloc[:,1])[0]))
            temp[:]= speed
            speed_limits= (f_hill_data[i].iloc[:,3]).as_matrix()
            collision_indices= np.where(temp > speed_limits)[0]
            if collision_indices.shape[0] != 0: #Deal with cases where velocity is greater than speed limit.
                temp[collision_indices]= speed_limits[collision_indices]
            velocity_profiles.append(temp)
    return velocity_profiles
    
def Generate_Wind_Velocity_Profile(low_speed, high_speed, units):
    '''This function can be used to simulate a wind velocity profile
    for simulation purposes. Generates a profile based on numpy's random
    number generator capabilities.'''
    global f_hill_data
    wind_profiles=list()
    for i in range (0, len(f_hill_data)):
        if units == 'si':
            temp= np.random.randint(low_speed, high_speed, size=(np.shape(f_hill_data[i].iloc[:,1])[0],1))
            wind_profiles.append(temp/3.6)
        else:
            temp= np.random.randint(low_speed, high_speed, size=(np.shape(f_hill_data[i].iloc[:,1])[0],1))
            wind_profiles.append(temp)
    return wind_profiles
    
def Generate_Constant_Wind_Velocity_Profile(speed, units):
    global f_hill_data
    wind_profiles=list()
    for i in range (0, len(f_hill_data)):
        if units == "si":
            temp= np.zeros((np.shape(f_hill_data[i].iloc[:,1])[0],1))
            temp[:]= speed/3.6
            wind_profiles.append(temp)
        else:
            temp= np.zeros((np.shape(f_hill_data[i].iloc[:,1])[0],1))
            temp[:]= speed
            wind_profiles.append(temp)
        return wind_profiles
def Generate_Constant_Velocity_Profile_Daily(speeds):
    '''This function can be used to assign a target speed for each racing day.'''
    global f_hill_data
    velocity_profiles= list()
    for i in range (0, len(f_hill_data)):
        if units == "si":
            temp= np.zeros((np.shape(f_hill_data[i].iloc[:,1])[0],1))
            temp[:]= speeds[i]/3.6
            velocity_profiles.append(temp)
        else:
            temp= np.zeros((np.shape(f_hill_data[i].iloc[:,1])[0],1))
            temp[:]= speeds[i]
            velocity_profiles.append(temp)
    return velocity_profiles