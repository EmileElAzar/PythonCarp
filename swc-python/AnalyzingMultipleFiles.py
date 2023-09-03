#Code follows the 'Analyzing Data from Multiple Files' class
import glob 
import os
import numpy as np 
import matplotlib.pyplot as mpl

path = os.path.join(os.getcwd(),'swc-python/data/')
os.chdir(path)

FileNames=sorted(glob.glob('inflammation*.csv')) #Obtaining and sorting all file names 
FileNames = FileNames[0:3] #Taking only the first 3 for now 

for i in FileNames: 
    print(i)
    data = np.loadtxt(fname=i,delimiter=',') #Loading data 
    fig = mpl.figure(figsize=(10.0,6.0))
    #Adding and configuring all subplots 
    #We have 1 row and 3 column subplots
    sub1 = fig.add_subplot(1,3,1)
    sub1.plot(np.mean(data,axis=0)) #Average
    sub1.set_xlabel("Day")
    sub1.set_ylabel("Average Inflammation per day")
    sub2 = fig.add_subplot(1,3,2)
    sub2.plot(np.amax(data,axis=0)) #Maximum
    sub2.set_xlabel("Day")
    sub2.set_ylabel("Maximum Inflammation per day")    
    sub3 = fig.add_subplot(1,3,3)
    sub3.plot(np.amin(data,axis=0)) #Minimum
    sub3.set_xlabel("Day")
    sub3.set_ylabel("Minimum Inflammation per day")    
    
    #Configuring the figure 
    fig.suptitle(("For data sheet {}").format(i))
    fig.tight_layout()
    
    #Show
    mpl.show()
    
#Coding our function: 
def fahrToCelsius(temp):
    #Input: A temperature value in Fahrenheit 
    #Output: The equivalent temperature in Celsius
    return ((temp-32)*(5/9))

#Calling it 
print(fahrToCelsius(32))

def rescale(array,lowValue = 0,highValue = 1):
    #Body that does something 
    return((array/2)*lowValue*highValue)

#Creating code that 
numbers = [1.5,2.3,0.7,-0.001,4.4]
total = 0.0
for i in numbers:
    assert i>0.0 #Data should only contain positive values 
    total += i
print('Total is:',total)