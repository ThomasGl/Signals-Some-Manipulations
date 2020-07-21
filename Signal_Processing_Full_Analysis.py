# Full Analysis on Decimation, Interpolation, Upsampling & Downsampling Process to DSP

#%%
import numpy as np
import matplotlib.pylab as plt
from scipy import signal

sample_size=101
sample_space=np.linspace(-25,25,sample_size)
x_value = np.zeros(sample_size)

x_value = np.power((2./sample_space*np.sin(sample_space*np.pi/8.)),2.)
x_value[np.where(sample_space==0)]=np.power((2.*np.pi/8.),2.)

plt.figure()
plt.style.use('seaborn')
# Some extra functions used
def upsample(arr, factor):#adding 0's to an array
    return signal.upfirdn([1], arr, factor)

def downsample(arr, factor):
    return arr[::factor]

#the following function is a way to get linear interpolation to an array
#the splitting of removing the last 'factor' elements is to get an exact interpolation, length wise.
def interp(arr, factor): #linear interpolation by factor
    
    #For the correct FIR coefficents of a Linear Interpolation method, harr is going to hold such coefficents

    harr=[]#we create an arry as to be the input of FIR at the upfirdn function, used from scipy
    harr.extend(np.linspace(1,factor-1,factor-1)) #we use extend as to iterate over the array generated and keep it in a single dimension
    harr.append(factor)#for signal dimension 'extension' we simply use append function
    harr.extend((np.linspace(factor-1,1,factor-1))) #inside the extend brackets one could also use: np.flip(np.linspace(1,factor-1,factor-1))

    harr=np.divide(harr,factor)

    return signal.upfirdn(harr, arr, factor)[:-factor]
    

# Fourier Transform of the Original Signal + Plottings
FTx=np.absolute(np.fft.fft(x_value))
omega=np.linspace(-2*np.pi,2*np.pi,sample_size)

plt.subplot(5,4,1);plt.plot(omega,FTx);plt.title('Original FT')
plt.subplot(5,4,2);plt.plot(sample_space,x_value);plt.title('Original')

# Downsample - Factor 3 - + Fourier Transform
sampled3=downsample(sample_space,3)
xd3=downsample(x_value,3)

FTxd3=np.absolute(np.fft.fft(xd3))
omegad3=np.linspace(-2.*np.pi,2.*np.pi,int(np.floor(sample_size/3.)+1))
plt.subplot(5,4,3);plt.plot(omegad3,FTxd3);plt.title('Downsample 3 FT')
plt.subplot(5,4,4);plt.plot(sampled3,xd3,':r*');plt.title('Downsample 3')

# Decimation  - Factor 3 -  + Fourier Transform
samplede3=signal.decimate(sample_space,3)
xde3=signal.decimate(x_value,3)
FTxde3=np.absolute(np.fft.fft(xde3))
omegade3=np.linspace(-2*np.pi,2*np.pi,int(np.floor(sample_size/3.)+1))
plt.subplot(5,4,5);plt.plot(omegade3,FTxde3);plt.title('Decimate 3 FT')
plt.subplot(5,4,6);plt.plot(samplede3,xde3,':g*');plt.title('Decimate 3')

# Downsample - Factor 5 - + Fourier Transform
sampled5=downsample(sample_space,5)
xd5=downsample(x_value,5)
FTxd5=np.absolute(np.fft.fft(xd5))
omegad5=np.linspace(-2.*np.pi,2.*np.pi,int(np.floor(sample_size/5.)+1))
plt.subplot(5,4,7);plt.plot(omegad5,FTxd5);plt.title('Downsample 5 FT')
plt.subplot(5,4,8);plt.plot(sampled5,xd5,':m*');plt.title('Downsample 5')

# Decimation  - Factor 5 -  + Fourier Transform
samplede5=signal.decimate(sample_space,5)
xde5=signal.decimate(x_value,5)
FTxde5=np.absolute(np.fft.fft(xde5))
omegade5=np.linspace(-2.*np.pi,2.*np.pi,len(FTxde5))
plt.subplot(5,4,9);plt.plot(omegade5,FTxde5);plt.title('Decimate 5 FT')
plt.subplot(5,4,10);plt.plot(samplede5,xde5,':k*');plt.title('Decimate 5')

# Upsample - Factor 3 - + Fourier Transform
sampleu3=upsample(sample_space,3)
xu3=upsample(x_value,3)
FTxu3=np.absolute(np.fft.fft(xu3))
omegau3=np.linspace(-2*np.pi,2*np.pi,sample_size*3)
plt.subplot(5,4,11);plt.plot(omegau3,FTxu3);plt.title('Up sample 3 FT')
plt.subplot(5,4,12);plt.plot(sampleu3,xu3,':k*');plt.title('Up sample 3')

# Interpolation  - Factor 3 -  + Fourier Transform
samplein3=interp(sample_space,3)
xin3=interp(x_value,3)
FTxin3=np.absolute(np.fft.fft(xin3))
omegain3=np.linspace(-2*np.pi,2*np.pi,sample_size*3)
plt.subplot(5,4,13);plt.plot(omegain3,FTxin3);plt.title('Interpol 3 FT')
plt.subplot(5,4,14);plt.plot(samplein3,xin3,':y*');plt.title('Interpol 3')

# Upsample - Factor 5 - + Fourier Transform
sampleu5=upsample(sample_space,5)
xu5=upsample(x_value,5)
FTxu5=np.absolute(np.fft.fft(xu5))
omegau5=np.linspace(-2*np.pi,2*np.pi,sample_size*5)
plt.subplot(5,4,15);plt.plot(omegau5,FTxu5);plt.title('Up sample 5 FT')
plt.subplot(5,4,16);plt.plot(sampleu5,xu5,':r*');plt.title('Up sample 5')

# Interpolation - Factor 5 - + Fourier Transform
samplein5=interp(sample_space,5)
xin5=interp(x_value,5)
FTxin5=np.absolute(np.fft.fft(xin5))
omegain5=np.linspace(-2*np.pi,2*np.pi,sample_size*5)
plt.subplot(5,4,17);plt.plot(omegain5,FTxin5);plt.title('Interpol 5 FT')
plt.subplot(5,4,18);plt.plot(samplein5,xin5,':g*');plt.title('Interpol 5')

# Resampling - Factor 2/3 - + Fourier Transform
sample23=signal.upfirdn([.5,1,.5], sample_space, 2,3)
x23=signal.upfirdn([.5,1,.5], x_value, 2,3)
FTx23=np.absolute(np.fft.fft(x23))
omegax23=np.linspace(-2*np.pi,2*np.pi,int(sample_size*2/3)+1)
plt.subplot(5,4,19);plt.plot(omegax23,FTx23);plt.title('Rational 2/3 FT')
plt.subplot(5,4,20);plt.plot(sample23,x23,':b*');plt.title('Rational 2/3')

#plt.subplots_adjust(wspace=0.35,hspace=0.9)
plt.tight_layout()
plt.show()
# Sine Wave Manipulation

#Extracting audio_file
import ffmpeg

from audio2numpy import open_audio
fp = 'sin.wav'
#fp = 'sin.wav'
audio, sampling_rate = open_audio(fp)
#mu, sampling_rate = ffmpeg.input(fp)
sample_space=len(audio)

#Plotting + Fourier Transform

plt.figure()
plt.style.use('seaborn')

fourier_audio = np.absolute(np.fft.fft(audio))
omega_orginal = np.linspace(-2*np.pi, 2*np.pi, len(audio))

plt.subplot(2,2,(1,2));plt.plot(omega_orginal, fourier_audio);plt.title('Original')
#Down->Inter

audio_down=downsample(audio,4)
audio_down_inter = interp(audio_down, 4)
fourier_down_inter = np.absolute(np.fft.fft(audio_down_inter))
omega_2 = np.linspace(-2*np.pi, 2*np.pi, len(fourier_down_inter))

plt.subplot(2,2,3);plt.plot(omega_2, fourier_down_inter);plt.title('Down->Inter')
#Inter->Down
audio_inter = interp(audio, 4)
audio_inter_down = downsample(audio_inter, 4)
fourier_inter_down = np.absolute(np.fft.fft(audio_inter_down))
omega_3 = np.linspace(-2*np.pi, 2*np.pi, len(fourier_inter_down))

plt.subplot(2,2,4);plt.plot(omega_3, fourier_inter_down);plt.title('Inter->Down')

plt.tight_layout()
plt.show()
#%%