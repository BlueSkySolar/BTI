
from packages import *

def calculate_air(altitude_array):
    den_air= np.power(altitude_array, 3) * (-3.64 * 10**(-14)) + np.power(altitude_array,2) * (3.88 * 10 **(-9)) + (-1.18*10**(-4)) * altitude_array + 1.17
    return den_air
def calculate_faero(frontal_area, v_car, v_wind, drag_coe, den_air):
    f_aero= 0.5*den_air* frontal_area * drag_coe * np.power(np.subtract(v_car, v_wind),2)
    return f_aero
def calculate_paero(frontal_area, v_car, v_wind, drag_coe, den_air):
    p_aero= 0.5*den_air* frontal_area * drag_coe * np.power(np.subtract(v_car, v_wind),3)
    return p_aero














