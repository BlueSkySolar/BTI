
from packages import *


def calculate_force_roll(mass,gravity, delta_h, delta_x, velocity, roll_coe, wheels):
    '''This function is used to calculate the rolling resistance force
    Speed values are in kph. (incline==cos(phi))'''
    del_h= delta_h.copy(deep=True)
    del_h[0]=0.000001
    cos_incline= delta_x / ((delta_h)**2 + (delta_x)**2)**(1.0/2.0)
    return ((1.0/3.6)*roll_coe*(1 + (velocity_kph / 161.0)) * mass * gravity * cos_incline)
def calculate_power_roll(mass,gravity,delta_h, delta_x, velocity_kph, roll_coe):
    '''This function estimates the power losses due to rolling resistance.'''
    del_h= delta_h.copy(deep=True)
    del_h[0]=0.000001
    cos_incline= delta_x / ((del_h)**2.0 + (delta_x)**2.0)**(1.0/2.0)
    return ((1.0/3.6)*roll_coe*(1 + (velocity_kph / 161.0)) * mass * gravity * cos_incline * velocity_kph)












