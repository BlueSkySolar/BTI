
from packages import *

def ForceGrav(mass, gravity):
    '''This function can be used to estimate the power losses due to going up a hill.
    ie: P= mgsin theta. '''
    old_path= os.getcwd()
    data_path= old_path+ '\\Road_Data'
    new_path= os.listdir(os.chdir(data_path))
    print(new_path)
    data_files=list()
    for i in range(0,len(new_path)): #loop through 0 to 7. (each file in the directory).
        road_data= pan.read_csv(new_path[i], delimiter=',') #The way np works is that it is meant for arrays of the same data type which is not the case for us.
        data_files.append(road_data)
        data_files[i].iloc[1:,9]= mass*gravity*((data_files[i].iloc[1:,6]/1000) / (((data_files[i].iloc[1:,2])**2 + (data_files[i].iloc[1:,6]/1000)**2)**(1.0/2.0)))
    os.chdir(old_path)
    return data_files

def PowerGrav_Plot(data_files):
    '''This function will plot the distribution of the power losses due to hill. '''
    old_path= os.getcwd()
    print(old_path)
    data_path= old_path+ '\\Road_Data'
    names_checkpoints= os.listdir(os.chdir(data_path))

    plt.close('all')

    f, axarr= plt.subplots(8, sharex= True, sharey=True)
    for i in range (0, len(names_checkpoints)):
        #plt.figure("Distribution of Phill over the race")
        #plt.subplot(2,1,1+i)
        #plt.title(names_checkpoints[i])
        axarr[i].plot(data_files[i].as_matrix()[:,1], data_files[i].as_matrix()[:,9])
        axarr[i].set_title(names_checkpoints[i])
    return
    '''#Opens up the graphing application UI.
    app= QtGui.QApplication(sys.argv)
    #Initiating the UI widget.
    window= pg.GraphicsWindow("Distribution of Phill over ASC race")
    window.resize(2400,1200)
    window.setWindowTitle("Plots for each city of Phill")

    pg.setConfigOptions(antialias=True)

    #for i in range(0, len(names_checkpoints)):
        #if (i!=0 and (i%3) ==0):
            #window.nextRow()
    a=window.addPlot(title= str(""+ str(names_checkpoints[0])))
    print(data_files[0].as_matrix()[:,1])
    print(data_files[0].as_matrix()[:,9])
    a.plot(x=data_files[0].as_matrix()[:,1], y= data_files[0].as_matrix()[:,9])
    a.showGrid(x=True, y=True)
    window.show()
    print("No Error")
    #return 0'''
def Return_Route_Files():
    '''Helper function for the tester.'''
    old_path= os.getcwd()
    data_path= old_path+ '\\Road_Data'
    new_path= os.listdir(os.chdir(data_path))
    os.chdir(old_path)
    return new_path
