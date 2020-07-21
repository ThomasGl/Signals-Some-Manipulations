import numpy as np
import matplotlib.pylab as plt


T1=1;T=4;N=[1,3,7,19,79]

#Function definition:
time = np.arange(-T/2,T/2, 0.01) 
    
x = np.zeros(len(time))
x[np.where( (time > -T1) & (time < T1) )] = 1

#The color vector below is critical for an efficient data visualization
Colors = ['y','m','c','r','g','b']
    
plt.figure()
plt.plot(time,x,'k', label='Original Signal');plt.title('Pulse Function Reconstruction')

def FindFourierCoeff(time, fOrig, k):
    dx = time[2] - time[1]
    a0 = (1/np.pi) * sum(fOrig*dx)
        
    sumVal = 0
    aN = np.zeros(k)
    bN = np.zeros(k)
    for iter in range(k):
        aN[iter] = (1/np.pi) * sum(fOrig*np.cos((iter+1)*time)*dx)
        bN[iter] = (1/np.pi) * sum(fOrig*np.sin((iter+1)*time)*dx)
        
        sumVal = sumVal + aN[iter]*np.cos((iter+1)*time) + bN[iter]*np.sin((iter+1)*time)
        
    fReconst = a0/2 + sumVal
    return fReconst

for j in range(len(N)):
    fReconsta = np.zeros(N[j])
    fReconsta = FindFourierCoeff(time, x, N[j])
    txt=['Reconstructed Signal N='+str(N[j])]
    plt.plot(time, fReconsta, color=Colors[j],label='txt')
    #plt.legend(txt)

plt.show()   
