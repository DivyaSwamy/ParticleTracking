# April 13 2019 
# Divya Swaminathan

import sys
import numpy as np
import matplotlib.pyplot as plt

track_length = 500
maximum_lag = track_length-1
lag_axis = np.arange(1,track_length)
# 12 ms is the frame rate
tstp= 0.012  
r =  1 #np.sqrt(4*1*tstp)
x = np.zeros(track_length)
y = np.zeros(track_length)

# Create the track
for i in range(1,track_length):
    # Select angle theta
    theta = np.random.randint(0,180)
    x[i] = x[i-1] + r*np.cos(theta)
    y[i] = y[i-1] + r*np.sin(theta)


fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.scatter(x,y)
plt.show()

print('running')

# Declare a matrix which is basically keeping track of msd calculations per track
msd = np.zeros([track_length,track_length])
#
print('running')
# Calculate MSD vs lag
for lag in range(1,track_length):
    nsteps = maximum_lag-lag+1
    sp=0
    for ik in range(0,nsteps):
        # calculte r^2 per lag
        msd[lag,ik] = np.square(x[ik+lag]-x[ik]) + np.square(y[ik+lag]-y[ik])
        sp=sp+1
        
        
print('running')
 # Calculate Mean msd per lag for the track
mean_msd = np.zeros([track_length,1])
for i in range(0,track_length):
    mean_msd[i]=np.mean(msd[i,0:track_length-i])
     
     
print('running')
#Plot MSD vs lag graph
fig2= plt.figure()
ax = fig2.add_subplot(1,1,1)
ax.scatter(lag_axis,mean_msd[1:track_length])
plt.show()
     
    
    