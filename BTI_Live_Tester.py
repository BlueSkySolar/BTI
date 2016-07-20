# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:19:14 2016
This file contains the tester that will interface with the simulator in real time based on the
live feed from the telemetry system.
@author: Armand Gurgu
"""

from packages import *
from PowerAero import *
from PowerGrav import *
from PowerRolling import *
from BTI_Live_Output import *
from ArrayPower import *
from BatteryModel import *
from VelocityProfile import *
from Optimization_Routine import *
from Plotter import *
from simulator_constants import *
from Race_Simulator import *

class Read_BTI_RT():
    def __init__(self,duration,file_name,directory_name,flag):
        self.duration= duration
        self.file_name= file_name
        self.directory_name= directory_name
        self.flag= flag
        self.file_list=None
        self.list_of_test_files=None
        if self.flag == "past":    
            self.file_list, self.list_of_test_files= Read_Previous_Testing_Data(self.directory_name)
        else:
            self.file_list= Read_BTI_Data(self.duration, self.file_name)
        self.parsed_data= list()
        self.time_list= list()
        self.number_of_dep_vars= 0
    def Parse_Data(self, independent_variable, dependent_variable):
        print("Removing garbage from data. Pls Wait.")
        for i in range (0, len(self.file_list)):
            self.parsed_data.append(Parse_Previous_Testing_Data(self.file_list[i].copy(), independent_variable, dependent_variable))
        self.number_of_dep_vars += 1
        return 0
    def Parse_Time_Array(self):
        '''Only applicable if reading time stamps.'''
        for i in range (0, len(self.parsed_data)):
            temp_time= self.parsed_data[i].index.hour
            if (min(temp_time) + 2) in temp_time:
                self.time_list.append(Timestamp_To_Time_Minutes(self.parsed_data[i]))
            else:
                self.time_list.append(Timestamp_To_Time_Hours(self.parsed_data[i]))
        return 0
    '''def Get_Coast_Down_Data(self):
        for i in range (0, len(self.parsed_data)):
            self.coast_down_data.append(Get_Coast_Down_Values(self.parsed_data[i].values, self.time_list[i]))
            self.max_velocity_kph.append((self.coast_down_data[i][1]*3.6))
        return 0
    def Curve_Fit_Data(self):
        if self.curve_type == "poly":
            for i in range (0, len(self.coast_down_data)):
                self.fitted_results.append(Curve_Fit_Data_Polynomial(self.coast_down_data[i][0], self.coast_down_data[i][1], self.poly_deg))
        else:
            pass
        return 0'''
    def Reset_All_Data(self):
        '''Method used to reset all the class attributes.'''
        self.file_list= None
        self.parsed_data= list()
        self.time_list= list()
        self.number_of_dep_vars= 0
        
class Power_Data_BTI():
    def __init__(self, BTI_object):
        print("Inheritance Worked!")
        self.BTI_object= BTI_object
        self.net_power= list()
        self.peak_power=None
    def Calculate_Bus_Power(self):
        '''Method used to calculate net power for the car.'''
        max_array=list()
        for i in range (0, len(self.BTI_object.file_list)):
            result= self.BTI_object.parsed_data[i] * self.BTI_object.parsed_data[i+len(self.BTI_object.file_list)]
            result= result.dropna()
            self.net_power.append(result)
            max_array.append(result.copy().max())
        self.peak_power= max(max_array)
        print(self.peak_power)
        return self.net_power
class Tester_RaceCrew(Read_BTI_RT, Power_Data_BTI):
    def __init__(self):
        print("Initiating the tester subroutine.")
        self.results= None
        self.july_11= None
        self.july_12= None
        self.july_13=None
        self.power_july11= None
        self.power_july12=None
        self.power_july13=None
        self.time_july11=list()
        self.time_july12=list()
        self.time_july13=list()
    def Run_Tester(self):
        self.july_11=Read_BTI_RT(0.2, "morning_charging","\\July_11", "past")
        self.july_12= Read_BTI_RT(0.2, "morning_charging","\\July_12", "past")
        self.july_13= Read_BTI_RT(0.2, "morning_charging", "\\July_13", "past")
        self.july_13.Parse_Data("time", "Batt Bus Current (A)")
        self.july_13.Parse_Data("time", "Batt Bus Voltage (V)")
        for i in range (0, int((len(self.july_13.parsed_data)/2))):
        # Dealing with files where batt bus current is < -15 A at turns (when in reality it should be positive)
            temp_indices= self.july_13.parsed_data[i].where(self.july_13.parsed_data[i]<-15).copy().dropna().index
            self.july_13.parsed_data[i][temp_indices]= abs(self.july_13.parsed_data[i][temp_indices])
        self.power_july13= Power_Data_BTI(self.july_13)
        self.results= self.power_july13.Calculate_Bus_Power()
        return 0
    def Solve_Time_Collisions(self):
        for i in range (0, len(self.results)):
            temp_time= self.results[i].index.hour
            if (min(temp_time) + 2) in temp_time:
                self.time_july13.append(Timestamp_To_Time_Minutes(self.results[i]))
            else:
                self.time_july13.append(Timestamp_To_Time_Hours(self.results[i]))
        return 0
    def Plot_Bus_Power_Results(self):
        '''Method that plots the power balance for all the test results (also handles
        the negative current software issue).'''
        path= os.getcwd()
        '''Create a directory to save the plots.'''
        dir_path= path+ "\Drivers_Data"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        os.chdir(dir_path)
        '''Plotting the data.'''
        for i in range (0, len(self.results)):
            plt.figure(num=i, facecolor= 'w')
            plt.title(self.july_13.list_of_test_files[i], fontsize=14)
            #Get the starting time for the power results.
            get_start_time = self.results[i].index.hour[0]
            time_shift= (self.time_july13[i]/3600.0)+get_start_time
            plt.plot(time_shift, self.results[i].values)
            plt.xlabel("Time of Day (Hour)", fontsize= 14)
            plt.ylabel("Battery Pack Bus Power (W)", fontsize=14)
            plt.savefig(self.july_13.list_of_test_files[i] + ".jpg")
        os.chdir(path)
        return 0
    def Reset_Tester(self):
        self.results= None
        return 0
        
        
if __name__ == '__main__':
    global f_hill_data
    #use pan.to_datetime() to convert time object to a datetime64 object.
    '''Previous_Data= Read_Previous_Testing_Data()
    time_list=list()
    fitted_val_list=list()
    fitted_val_deri_list=list()
    fitted_polynomials_list=list()
    fitted_derivatives_list= list()
    coast_val_fit_list=list()
    coast_val_fit_deri_list=list()    
    coast_val_actual_list=list()
    
    fitted_results= list()
    fitted_deri_results=list()
    
    real_roll_coe_fit=list()
    real_roll_coe_nonfit=list()
    #For plotting Purposes.
    max_velocity_kph=list()
    
    for i in range (0,len(Previous_Data)):
        print("Iteration number: " + str(i))
        print("\n")
        b= Parse_Previous_Testing_Data(Previous_Data[i].copy(), "Vehicle Velocity (m/s)", "time")
        if i == 0 :
            time_array= Timestamp_To_Time_Minutes(b)
        elif i==2:
            print(b)
            time_array= Timestamp_To_Time_Hours(b)
        else:
            time_array= Timestamp_To_Time_Hours(b)
        time_list.append(time_array)
        coast_val_actual= Get_Coast_Down_Values(b.values,time_array)
        coast_val_actual_list.append(coast_val_actual)
        max_velocity_kph.append(max(coast_val_actual[1]))
    #Curve fitting code.
        fitted_polynomials = Curve_Fit_Data_Polynomial(coast_val_actual_list[i][0],coast_val_actual_list[i][1],3)
        fitted_results.append(fitted_polynomials)
        fitted_der= Der_Poly_Data(fitted_results[i], 1, coast_val_actual_list[i][0])
        fitted_deri_results.append(fitted_der)
        roll_coe_fit= Calculate_RT_Rolling_Coefficient_Fit(fitted_deri_results[i], fitted_results[i], mass_of_car, Cd, frontal_area, rho, gravity)
        real_roll_coe_fit.append(roll_coe_fit)
        roll_coe_nonfit= Calculate_RT_Rolling_Coefficient_Nonfit(coast_val_actual_list[i][1], coast_val_actual_list[i][0], mass_of_car, Cd, frontal_area, rho, gravity)
        real_roll_coe_nonfit.append(roll_coe_nonfit[0])
       
    real_roll_coe_nonfit= np.asarray(real_roll_coe_nonfit)
    max_velocity_kph= np.asarray(max_velocity_kph)
    #Normalize for wind.
    v1= (max_velocity_kph[1:][0] +max_velocity_kph[1:][1])/2
    v2= (max_velocity_kph[1:][2] +max_velocity_kph[1:][3])/2
    v3= (max_velocity_kph[1:][4] +max_velocity_kph[1:][5])/2
    v4= (max_velocity_kph[1:][6] +max_velocity_kph[1:][7])/2
    v5= (max_velocity_kph[1:][8] +max_velocity_kph[1:][9])/2
    v6= (max_velocity_kph[1:][10] +max_velocity_kph[1:][11])/2
    a1= (real_roll_coe_nonfit[1:][0] +real_roll_coe_nonfit[1:][1])/2
    a2= (real_roll_coe_nonfit[1:][2] +real_roll_coe_nonfit[1:][3])/2
    a3= (real_roll_coe_nonfit[1:][4] +real_roll_coe_nonfit[1:][5])/2
    a4= (real_roll_coe_nonfit[1:][6] +real_roll_coe_nonfit[1:][7])/2
    a5= (real_roll_coe_nonfit[1:][8] +real_roll_coe_nonfit[1:][9])/2
    a6= (real_roll_coe_nonfit[1:][10] +real_roll_coe_nonfit[1:][11])/2
    coefficients= np.asarray([a1,a2,a3,a4,a5,a6])
    vel_coe= np.asarray([v1,v2,v3,v4,v5,v6])
    plt.plot((3.6*vel_coe), coefficients)
    plt.title("Rolling Resistance Coefficient Nonfit vs Speed of Car")
    plt.xlabel("Speed (kph)")
    plt.ylabel("Rolling Resistance Coefficient")
    
    #Test the data.
    #Plot_Previous_Data_Polynomial(coast_val_actual[1], fitted_val_list, coast_val_actual[0],1, "Time (s)", "Vehicle Velocity (m/s)", "Coast Down Profile")
    '''
    #Objects for each testing day.
    test= Tester_RaceCrew()
    test.Run_Tester()
    test.Solve_Time_Collisions()
    test.Plot_Bus_Power_Results()
    
    
    #a.Get_Coast_Down_Data()
    #a.Curve_Fit_Data()    