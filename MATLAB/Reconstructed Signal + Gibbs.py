# Signal - Reconstruction

import numpy as np
import matplotlib.pylab as plt

def generate_vars(T,t):
    x=np.cos(2*np.pi*t/T)

    y=np.zeros(len(t))

    y[np.where(t<0)]=-1
    y[np.where(t>0)]=1
    s=x*y

    return [x,y,s]

def generate_T1(N,T):
    T1=(N+0.5)*T

    return T1

#The function below is the applied version of the Harmoic Analysis Theorem
#for function reconstruction.
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

def PlotFunctions(time, fOrig, nVec):
    Colors = ['y','m','c','r','g','b','k']
    plt.figure()
    plt.subplot(2,4,1);plt.plot(time, fOrig, 'k');plt.title('Input Signal') 
    for n in range(7):
        fReconsta = FindFourierCoeff(time, fOrig, nVec[n])
    
        plt.subplot(2,4,n+2);plt.plot(time, fReconsta,Colors[n])
        str_a = 'Reconstructed Signal N = ' +str(nVec[n])
        plt.title(str_a)

    plt.show()


#Step Function Definition

T=1;N=3
T1=generate_T1(3,1)
t=np.linspace(-T1,T1,1000)

[x,y,s]=generate_vars(1,t)

plt.figure()
plt.subplot(3,1,1);plt.plot(t,x);plt.title('Cos(2\pi * x)');plt.ylim(-1.5, 1.5)

#Dicontinued Cosine + Step Function

plt.subplot(3,1,2)
plt.plot(t,y,'r',t,s,'c');plt.title('Previous + Step Function');plt.ylim(-1.5, 1.5)
plt.legend('y(t) s(t)');plt.title('Wo(s)=1')

#Discontinous Reconstructed Signal

plt.subplot(3,1,3);plt.plot(t,FindFourierCoeff(t,s,100));plt.title('Reconstruced Cosine');

plt.show()
# Rectangular-Pulse Function Reconstruction

#Gibbs Phenomena Presentation, it happens for functions with discontinuetes
#approximated by Fourier Series

#Function Declaration
time = np.linspace(-4,4,2000)    
    
Original_Function = np.zeros(len(time))
Original_Function[np.where((time > -2) & (time < 2))]= 1

#Reconstruction Factors are declared on the vector below:
nVec = [1, 2, 4, 8, 16, 64, 128]
PlotFunctions(time, Original_Function, nVec)
        
