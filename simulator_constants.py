# -*- coding: utf-8 -*-
"""
Spyder Editor

'''This file contains declarations of all the constants used
for the simulator.

This is a temporary script file.
"""
from PowerGrav import *

time_of_day= np.array([5,5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22])
race_day_start= 212
Pmax= 1000
#First element: Sunrise Time in Brecksville, 2nd: Sunrise time in Vincennes 6:25 am. 3rd: Sunrise time in  Republic MO is 5:53 am (same as first)
# 4th: Sunrise Time in Gering NE: 5:19 am. (got them from google)
SR= [5.8833333]
DL= 13.00
mass_of_car= 290
gravity= 9.81
#noon_angle= None
#path=None
n_array= 23.9
n_mppt= 95
n_cloud=np.array([1])
frontal_area=1
area_array= 6
solar_irradiance= 1370 #from google.
high_noon_angle=[12.5]

n_motor= 0.85

wind_velocity=None
velocity_si= None
velocity_kph= None

velocity_daily_profile= None
velocity_segment_profile=None

Cd=0.2
roll_coefficient=0.0055

electrical_parasitic_losses= 30

f_hill_data= ForceGrav(mass_of_car, gravity)

bat_capacity= 5000 #Wh.
bat_efficiency= 0.70 #ballpark!

 #lasts 45 minutes.
checkpoint_duration= (45.0*60.0)/3600.0

race_bat_capacity_energy=None
#Density of air for BTI data. (testing parameter not actual parameter)
rho= 1.17

driving_start_time=9.00
driving_end_time= 18.00

ASC_Route_Names= ["Brecksville-Dayton", "Dayton-Vincennes", "Vincennes-StLouis", "StLouis-Republic", "Republic-Topeka", "Topeka-Beatrice", "Beatrice-Scottsbluff", "Scottsbluff-Windcave"]