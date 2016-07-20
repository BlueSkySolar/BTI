
from packages import *

def Read_BTI_Data(duration, name):
    '''This function can be used to dynamically read the data outputted
    by the BTI in real time after a specified time "time".'''
    BTI_Data_list=list()
    old_path= os.getcwd()
    new_path= old_path + '\\' + datetime.datetime.now().strftime("%B") + "_" + str(datetime.datetime.now().day)
    os.chdir(new_path)
    start= time.time()
    end= time.time()
    #Stall the program to allow the BTI data to update.
    while ((end-start)/60.0) < duration:
        end= time.time()
    #Once loop is done, time minutes has passed.
    file= os.listdir(os.getcwd())
    for files in file:
        if name in files:
            print("the name of the file i opened is: " + files)
            BTI_Data_list.append(pan.read_csv(files, delimiter= ',', error_bad_lines=False, keep_default_na=True))
    os.chdir(old_path)
    return BTI_Data_list

def Read_Previous_Testing_Data(Directory_Date):
    '''This function can be used to read the data stored by the BTI
    from the past.'''
    data_array=list()
    curr_path= os.getcwd()
    new_path= curr_path+ '\\Past_Test_Data_Folder_BTI' + Directory_Date
    files= os.listdir(os.chdir(new_path))
    for i in range(0, len(files)):
        data= pan.read_csv(files[i], delimiter= ',', error_bad_lines=False, keep_default_na=True) #Keep this as True, black magic happens if False.
        data=data.reset_index()
        data_array.append(data)
        print("\n\n")
        print("Results for test file: " + str (i))
        print("Name of file: " + files[i])
        print("\n\n")
    os.chdir(curr_path)
    return [data_array, files]

def Parse_Previous_Testing_Data(file, indep_variable, dep_variable):
    '''This function accepts a Pandas Dataframe object and an independent
    and dependent variable and returns a numpy array with the nan values stripped out'''
    x_data= file[indep_variable]
    y_data= file[dep_variable]
    if (x_data.dtype) == np.dtype('O'):
        time_frame_x= pan.to_datetime(x_data) #convert to time series.
        result= pan.Series(y_data.values, index=time_frame_x)
        result= result.dropna()
        return result
    elif (y_data.dtype) == np.dtype('O'): #time series objects. need to convert them to a proper form.
        time_frame_y= pan.to_datetime(y_data) #convert to time series.
        result= pan.Series(x_data.values, index=time_frame_y)
        result= result.dropna()
        return result
    print(type(x_data))
    print(type(y_data))
    print("Yay printing variables.")
    x_data= x_data.dropna() #Convert series to dataframe and strip out NaN values.
    y_data= y_data.dropna() #Strip out any NaN Values.
    print(x_data)
    print(y_data)
    if x_data.shape[0] <= y_data.shape[0]:  #x has least number of points.
        indices= (x_data.where(x_data != np.nan)).index.values
        print(indices)
        y_data= y_data.iloc[indices-1]
    else:
        indices= (y_data.where(y_data != np.nan)).index.values
        x_data= x_data.iloc[indices-1]
    return [x_data, y_data]

def Curve_Fit_Data_Polynomial(indep_variable, dep_variable, degree):
    '''This function accepts a pandas/Numpy array file and a
    string called variable and returns the coefficients of
    curve fitting the data up to the degree variable "degree."'''
    result= list()
    for i in range (1, degree+1):    
        coefficients= np.polyfit(indep_variable, dep_variable, i)
        fitted_func= np.poly1d(coefficients)
        fitted_values= fitted_func(indep_variable)
        result.append([fitted_values, fitted_func])
    return result

#DO NOT FORGET TO ADD CURVE FITTING FOR OTHER FUNCTIONS (EXPONENTIAL, SINE/COSINE Etc.)

def Plot_Previous_Data_Polynomial(actual_values, fitted_values, independent_variable, figure_number, indep_var_name, dep_var_name, title_figure):
    '''This function accepts a pandas.'''
    labels=['Linear', 'Quadratic', 'Cubic']
    plt.figure(num=figure_number, facecolor= 'w')
    for i in range(0, len(fitted_values)):
        if i == 0:
            plt.plot(independent_variable, actual_values, label= 'Actual')
        plt.plot(independent_variable, fitted_values[i], label=labels[i])
        plt.title(title_figure)       #plots the variable's name (columns returns an array of the string name of the variable.)
        plt.xlabel(indep_var_name)
        plt.ylabel(dep_var_name)
        plt.legend(loc='best')
    
def Der_Poly_Data(fitted_func, n, indep_variable):
    '''This function calculates the nth derivative of the polynomial
    defined by fitted_func.'''
    result= list()
    for i in range (0, len(fitted_func)):
        derivative= np.polyder(fitted_func[i][1], m=n)
        fitted_values_derivative= derivative(indep_variable)
        result.append([fitted_values_derivative, derivative])
    return result
    
def Plot_Previous_Data_Derivative(actual_values, deri_values, independent_variable, figure_number, indep_var_name, dep_var_name, title_figure):
    '''This function accepts a pandas.'''
    labels=['Constant', 'Linear', 'Quadratic']
    plt.figure(num=figure_number, facecolor= 'w')
    for i in range(0, len(deri_values)):
        #if i == 0:
            #plt.plot(independent_variable, actual_values, label= 'Actual')
        plt.plot(independent_variable, deri_values[i], label=labels[i])
        plt.title(title_figure)       #plots the variable's name (columns returns an array of the string name of the variable.)
        plt.xlabel(indep_var_name)
        plt.ylabel(dep_var_name)
        plt.legend(loc='best')

def Calculate_RT_Rolling_Coefficient_Fit(accel, vel, m, Cd, A, rho, g):
    '''Subroutine that can be used to calculate the Rolling resistance coefficient.'''
    roll_coe=list()
    for i in range (0, len(vel)):
        copy_vel_square= vel[i][0].copy()
        copy_vel_square= np.power(copy_vel_square,2)
        result= ((-1)*m * accel[i][0]- 0.5 * rho * Cd * A * copy_vel_square)/(m*g*(1+ ((18*vel[i][0])/(5*161))))
        result= np.average(result)
        if result < 0:
            result= abs(result)
        roll_coe.append(result)
    return roll_coe
    
def Timestamp_To_Time_Minutes(series):
    '''Returns a numpy array representation of the timestamps of test data.'''
    array= series.index
    result= array.hour * 60.0 + array.minute + array.second / 1000.0
    return (result - min(result))
    
def Timestamp_To_Time_Hours(series):
    '''Returns a numpy array representation of the timestamps of test data.'''
    array= series.index
    result= array.hour * 3600.0 + array.minute * 60.0 + array.second
    return (result - min(result))
    
def Get_Coast_Down_Values(coast_values, independent_variable):
    '''Values used to estimate tire rolling resistance coefficient.'''
    copy_values= np.copy(coast_values)
    copy_indep_var= np.copy(independent_variable)
    index_max= np.where(copy_values == max(copy_values))[0][0]
    index_min= np.where(copy_values[index_max:] == min(copy_values[index_max:]))[0][0] + index_max
    copy_values=copy_values[index_max:(index_min+1)]
    copy_indep_var= copy_indep_var[index_max:(index_min+1)]
    return [copy_indep_var, copy_values, index_max]
def Get_Coast_Down_Fitted_Values(fitted_values, independent_variable, index_max):
    '''Get the fitted values (non-testing values) for coast down.'''
    copy_values= np.copy(fitted_values)
    copy_values= copy_values[index_max:]
    return copy_values
def Plot_RT_Rolling_Coefficient_Single():
    pass
def Plot_RT_Rolling_Coefficient_Multiple():
    pass
def Calculate_RT_Rolling_Coefficient_Nonfit(vel, time, m, Cd, A, rho, g):
    time_size= time.shape[0]
    car_dynamic_array= np.zeros((time_size,4))
    #Copy in the time and velocity values from test data.
    car_dynamic_array[:, 0]= time.copy()
    car_dynamic_array[:, 1]= vel.copy()
    #Calculate raw acceleration values.
    car_dynamic_array[1:, 2]= (vel.copy()[1:] - vel.copy()[0:(time_size-1)])/ (time.copy()[1:]-time.copy()[0:(time_size-1)])
    #Average out these acceleration values.
    car_dynamic_array[1:, 2] = (car_dynamic_array[1:,2] + car_dynamic_array[0:(time_size-1), 2])/2.0
    car_dynamic_array[:, 3]= ((-1) * m * car_dynamic_array[:,2] - 0.5 * rho * Cd * A * car_dynamic_array[:, 1] ** 2.0) / (m*g*(1+(18*car_dynamic_array[:,1])/(5*161)))
    result= np.average(car_dynamic_array[:,3])
    if result < 0:
        result= abs(result)
    return [result, car_dynamic_array]
def Match_Two_Variable_Sizes(x_data, y_data):
    pass