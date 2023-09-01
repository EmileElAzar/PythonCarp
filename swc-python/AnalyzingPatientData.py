#Importing NumPy 
import numpy as np
#Import is to resolve path issues 
import os

#This line joins path of current work directory, obtained by os.getcwd() and the 
#the path where the data is stored 
path = os.path.join(os.getcwd(),'swc-python/data/')
#To simplify everything we just change our current directory to that of data
os.chdir(path)
#Using numpy to load the file in, and store it in data 
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
#Gathering information on the type of the data variable, the type of variable data holds, and the shape of data 
print(type(data)) 
print(data.dtype)
print(data.shape)
#Printing the first and middle value of the data matrix 
print(("The first value in data is {}.").format(data[0,0]))
print(("The middle value in data is {}.").format(data[29,19]))
#Printing the first 4 rows (patients) and 10 columns (days)
print(data[0:4,0:10])
#Calculating the average inflammation for all patients on all days, i.e the mean of data 
print(np.mean(data))
#Using multiple assignment and calculating the maximum and minimum inflammation, and the std of inflammation
maxval,minval,stdval = np.amax(data),np.amin(data),np.std(data)
#Formatting the output 
print(("For data, the maximum value is {}, minimum is {}, and std is {}.").format(maxval,minval,stdval))
#indexing out the data for patient 0 
patient_0 = data[0,:] #Indexing everything for the first patient 
#Outputting the maximum inflammation of patinet 0 
print(("The maximum inflammation of patient 0 is {}.").format(np.amax(patient_0)))
#Outputting the maximum inflammation of patient 2
print(("The maximum inflammation of patient 2 is {}.").format(np.amax(data[2,:])))
#Calculating the average across the rows 
print(np.mean(data,axis=0))

#Stacking Arrays now
#Defining 3 x 3 array 
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(("\nInitial matrix A is \n{}.\n").format(A))
#Defining an array B that horizontally stacks the array A, so the new array would be 
#[A A] 
B = np.hstack([A,A])
print(("B, horizontally stacked A is \n{}.\n").format(B))
#Defining an array C that vertically stacks the array A so C' = [A A]
C = np.vstack([A,A])
print(("C, vertically stacked A is \n{}.\n").format(C))
