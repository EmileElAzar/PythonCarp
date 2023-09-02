#Importing NumPy 
import numpy as np
#Import os to resolve path issues 
import os
#Import matplotlib pyplot for plotting 
import matplotlib.pyplot 


#This line joins path of current work directory, obtained by os.getcwd() and the 
#the path where the data is stored 
path = os.path.join(os.getcwd(),'swc-python/data/')
#To simplify everything we just change our current directory to that of data
os.chdir(path)
#Using /numpy to load the file in, and store it in data 
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(data.shape)

#Using matplotlb to plot a heat map 
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
#Now plotting the ave
#Average inflammation per day over time 
#This would be taking the average along columns thus axis = 0
averageInflammation = np.mean(data,axis=0)
averagePlot = matplotlib.pyplot.plot(averageInflammation)
matplotlib.pyplot.show()
#Plotting the maximum inflammation per day against the number of days 
#Again, remember that we are taking average per day therefore along columns thus axis = 0
maxInflammation = np.amax(data,axis=0)
maxPlot = matplotlib.pyplot.plot(maxInflammation)
matplotlib.pyplot.show()
#Repeating the same for the minimum 
minInflammation = np.amin(data,axis=0)
minPlot = matplotlib.pyplot.plot(minInflammation)
matplotlib.pyplot.show()
#Creating a space where we are going to put all 3 plots side by side
#The space will be 10 x 3.0 
fig = matplotlib.pyplot.figure(figsize=(10.0,3.0))
#We are now going to create 3 subplot into the figure
#The figures will be horizontally stacked, so 1 row, 3 columns:
sub1 = fig.add_subplot(1,3,1) #First subplot so '1' in third place
sub2 = fig.add_subplot(1,3,2) #Second subplot so '2' in third place
sub3 = fig.add_subplot(1,3,3)
#Filling in and labelling each subplot 
#Subplot 1
sub1.set_ylabel('Average Daily Inflammation')
sub1.set_xlabel('Day')
sub1.plot(np.mean(data,axis=0))
#Subplot 2 
sub2.set_ylabel('Maximum Daily Inflammation ')
sub2.set_xlabel('Day')
sub2.plot(np.amax(data,axis=0))
#Subplot 3 
sub3.set_ylabel('Minimum Daily Inflammation ')
sub3.set_xlabel('Day')
sub3.plot(np.amin(data,axis=0))
#Configuring the total figure and subplot 
fig.tight_layout()
#Saving the figure as a picture 
matplotlib.pyplot.savefig('Inflammation.png')
matplotlib.pyplot.show()

#Creating figure and adding subplots 
fig2 = matplotlib.pyplot.figure(figsize=(10.0,6.0))
sub1 = fig2.add_subplot(2,2,1)
sub2 = fig2.add_subplot(2,2,2)
sub3 = fig2.add_subplot(2,2,3)
sub4 = fig2.add_subplot(2,2,4)
#Adding details and plots on the subplot. Now sub1
sub1.set_ylabel('Average Daily Inflammation')
sub1.plot(np.mean(data,axis=0))
sub1.set_xlabel('Day')
sub1.set_ylim(0,15)
#Adding details to sub2
sub2.set_ylabel('Maximum Daily Inflammation ')
sub2.set_xlabel('Day')
sub2.plot(np.amax(data,axis=0))
sub2.set_ylim(0,25)
#Adding details to sub3
sub3.set_ylabel('Minimum Daily Inflammation')
sub3.plot(np.amin(data,axis=0))
sub3.set_xlabel('Day')
sub3.set_ylim(0,5)
#Adding details to sub4
sub4.set_ylabel('Standard Deviation of Inflammation')
sub4.plot(np.std(data,axis=0))
sub4.set_xlabel('Day')
#Tightening Up 
fig2.tight_layout()
#Saving the figure as a picture 
matplotlib.pyplot.savefig('Inflammation2.png') 
matplotlib.pyplot.show()

#A quick example of indexing with a step increment for example
primes = [2,3,5,7,11,13,17,19,23,29,31,37]
subset = primes[0:12:3] #Indexing elements with a step size of 3
print(("Indexed elements are {}").format(subset))

#Code without an enumeration test
x = 5
coefs = [2,4,3]
y = coefs[0]*(x**0)+coefs[1]*(x**1)+coefs[2]*(x**2)
print(y)

#Doing the same by using an enumeration 
y = 0
for i,coef in enumerate(coefs):
    y = y+((coef)*(x**i))