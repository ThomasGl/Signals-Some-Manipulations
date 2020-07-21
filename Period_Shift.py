import numpy as np
import matplotlib.pylab as plt

n=np.linspace(-np.pi,np.pi,20)
w0=3*np.pi/4;#same as 6pi/8
x=np.sin(w0*n)
y=np.zeros(len(n))
   
factor=3 

plt.figure()
#Ploting 3 periods
for p in range(factor):
    index=p+1
    w1=w0*index 
    x=np.sin(w1*n)
    plt.subplot(factor,1,index);plt.stem(x,use_line_collection=True);plt.title(str(index) + ' Period Shift')

plt.show()