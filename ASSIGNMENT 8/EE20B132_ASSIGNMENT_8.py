'''
SUHAS C
EE20B132
EE2703 - THE APPLIED PROGRAMMING LANGUAGE
ASSIGNMENT 8 - THE DIGITAL FOURIER TRANSFORM
'''

from pylab import *
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-4*pi,4*pi,513)[:-1]
w = np.linspace(-64,64,513)[:-1]
y1 = (np.sin(x))**3
Y1 = fftshift(fft(y1))/512

fig,ax = plt.subplots(2)
ax[0].plot(w,abs(Y1))
ax[0].set_xlim([-10,10])
ax[0].set_title(r"Magnitude and Phase plots of DFT of $\sin^3(t)$ ")
ax[0].set_ylabel(r"$|Y|$",size=16)
ax[0].set_xlabel(r"$\omega$",size=16)
ax[0].grid(True)

ii1 = np.where(abs(Y1)<10**-3)
ph = angle(Y1)
ph[ii1] = 0 

ax[1].plot(w,ph,"bo")
ax[1].set_xlim([-10,10])
ax[1].grid(True)
ax[1].set_ylabel(r"Phase of $Y$",size=16)
ax[1].set_xlabel(r"$\omega$",size=16)
plt.show()

x = np.linspace(-4*pi,4*pi,129)[:-1]
w = np.linspace(-16,16,129)[:-1]
y2 = (np.cos(x))**3
Y2 = fftshift(fft(y2))/128

fig,bx = plt.subplots(2)
bx[0].plot(w,abs(Y2))
bx[0].set_xlim([-10,10])
bx[0].grid(True)
bx[0].set_ylabel(r"$|Y|$",size=16)
bx[0].set_xlabel(r"$\omega$",size=16)
bx[0].set_title(r"Magnitude and Phase plots of DFT of $\cos^3(t)$ ")

ii2 = np.where(abs(Y2)>10**-3)

bx[1].plot(w[ii2],angle(Y2[ii2]),"bo")
bx[1].set_xlim([-10,10])
bx[1].grid(True)
bx[1].set_ylabel(r"Phase of $Y$",size=16)
bx[1].set_xlabel(r"$\omega$",size=16)
plt.show()

x = np.linspace(-4*pi,4*pi,513)[:-1]
w = np.linspace(-64,64,513)[:-1]
y1 = cos(20*x + 5*cos(x))
Y1 = fftshift(fft(y1))/512

fig,ax = plt.subplots(2)
ax[0].plot(w,abs(Y1))
ax[0].set_xlim([-40,40])
ax[0].grid(True)
ax[0].set_ylabel(r"$|Y|$",size=16)
ax[0].set_xlabel(r"$\omega$",size=16)
ax[0].set_title(r"Magnitude and Phase plots of DFT of $ \cos(20t +5 \cos(t))$ ")

ii1 = np.where(abs(Y1)<10**-3)
ph = angle(Y1)
ph[ii1] = 0 

ax[1].plot(w,ph,"bo")
ax[1].set_xlim([-40,40])
ax[1].grid(True)
ax[1].set_ylabel(r"Phase of $Y$",size=16)
ax[1].set_xlabel(r"$\omega$",size=16)
plt.show()


def ideal(w):
    return (1/np.sqrt(2*pi)) * (exp((-1*w*w)/2))
def tol(N=128,tol=10**-6):
    T = 8*pi
    N = 128
    error = 10**10
    yold =0
    while error>tol:
        x = np.linspace(-T/2,T/2,N+1)[:-1]
        w = pi* np.linspace(-N/T,N/T,N+1)[:-1]
        Y1 = (T/(2*pi*N)) * fftshift(fft(ifftshift(exp(-x*x/2))))
        error = sum(abs(Y1-ideal(w)))
        yold = Y1
        T = T*2
        N = N*2
    print("max error =" + str(error))

fig,ax = plt.subplots(2)
ax[0].plot(w,abs(Y1))
ax[0].set_xlim([-10,10])
ax[0].grid(True)
ax[0].set_ylabel(r"$|Y|$",size=16)
ax[0].set_xlabel(r"$\omega$",size=16)
ax[0].set_title(r"Magnitude and Phase plots(calculated) of DFT of $ \exp(-t^{2}/2)$ ")

ii1 = np.where(abs(Y1)<10**-3)
ph = angle(Y1)
ph[ii1] =0

ax[1].plot(w,ph,"r+")
ax[1].set_xlim([-10,10])
ax[1].grid(True)
ax[1].set_ylabel(r"Phase of $Y$",size=16)
ax[1].set_xlabel(r"$\omega$",size=16)
plt.show()

fig2,bx = plt.subplots(2)
bx[0].plot(w,abs(ideal(w)))
bx[0].set_xlim([-10,10])
bx[0].grid(True)
bx[0].set_ylabel(r"$|Y|$",size=16)
bx[0].set_xlabel(r"$\omega$",size=16)
bx[0].set_title(r"Magnitude and Phase plots(ideal) of DFT of $ \exp(-t^{2}/2)$ ")
    
bx[1].plot(w,angle(ideal(w)),"r+")
bx[1].set_xlim([-10,10])
bx[1].grid(True)
bx[1].set_ylabel(r"Phase of $Y$",size=16)
bx[1].set_xlabel(r"$\omega$",size=16)
plt.show()
