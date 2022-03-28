'''
APL EE2703 ASSIGNMENT 6
SUHAS C
EE20B132
'''
          
import numpy as np
import scipy.signal as sp                                             # Scipy.signal module contains the functions helps us in solving the LTI sytems   
import pylab as py                                                  # Such as bilateral and inverse fourier transform , convolution , impulse response 
from pylab import *

# Question_1
# Finding the reponse for sinusoidal exponential decaying forced input for the spring equation with its natural frequency as 1.5rad/sec 

F1 = sp.lti([1,0.5],[1,1,2.5])                                        # Defining the laplace transform of input
X1 = sp.lti([1,0.5],[1,1,4.75,2.25,5.625])                            # Defining the laplace transform of the output
                                                                      
t,x1 = sp.impulse(X1,None,linspace(0,50,501))                         # Finding the time domain output by applying inverse laplace using sp.impulse
                                             
py.figure(0)                                                             # plotting the output response
py.plot(t,x1) 
py.xlabel(r'$t$')
py.ylabel(r'$x(t)$')
py.title(r' $x(t)$ vs $t$ for decay rate 0.5/sec - Question_1')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.savefig("suhas/figure0.png")
py.show()

# Question_2
# Recuding the Decay constant of the input

F2 = sp.lti([1,0.05],[1,0.1,2.2525])                                  # Defining the laplace transform of new input
X2 = sp.lti([1,0.05],[1,0.1,4.5025,0.225,5.068125])

t,x2 = sp.impulse(X2,None,linspace(0,50,501))                         # Finding the time domain output by applying inverse laplace using sp.impulse

py.figure(1)                                                             # plotting the output response
py.plot(t,x2)
py.xlabel(r'$t$')
py.ylabel(r'$x(t)$')
py.title(r' $x(t)$ vs $t$ for decay rate 0.05/sec - Question_2')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.savefig("suhas/figure1.png")
py.show()

# Question_3

H = sp.lti([1],[1,0,2.25])                                            # Defining the System transfer function   
dec = linspace(1.4,1.6,5)                                             # Set of cosine frequencies 

py.figure(2)                           
for i in dec:
    p = i*i + 0.0025
    F = sp.lti([1,0.05],[1,0.1,p])                                    # Defining the input laplace transform 
    t,f = sp.impulse(F,None,linspace(0,50,501))                       # Finding the input time domain equation
    t,y,svec = sp.lsim(H,f,t)                                         # Finding the Output by convolving the impulse response with the input using sp.lsim
    plot(t,y,label = 'freq = '+str(i)+' ')                            # plotting all responses in single plot with labels


py.xlabel(r'$t$')
py.ylabel(r'$y(t)$')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.title(r'Responses for different frequency inputs - Question_3')
py.legend() 
py.savefig("suhas/figure2.png")   
py.show()
   
# Question_4
# Coupled Spring problem with x and y as displacement 

X4 = sp.lti([1,0,2],[1,0,3,0])                                        # Defining the laplace transform of x(t) = X(s)                  
Y4 = sp.lti([2],[1,0,3,0])                                            # Defining the laplace transform of y(t) = Y(s)

t1,x4 = sp.impulse(X4,None,linspace(0,20,201))                        # Finding the time domain output of x(t)
t1,y4 = sp.impulse(Y4,None,linspace(0,20,201))                        # Finding the time domain output of y(t)

py.figure(3)                                                             # plotting the response x(t)
py.plot(t1,x4)
py.xlabel(r'$t$')
py.ylabel(r'$x(t)$')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.title(r'x(t) - Question_4')
py.savefig("suhas/figure3.png")
py.show()

py.figure(4)                                                             # plotting the response y(t)
py.plot(t1,y4)
py.xlabel(r'$t$')
py.ylabel(r'$y(t)$')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.title(r'y(t) - Question_4')
py.savefig("suhas/figure4.png")
py.show()

# Question_5
# TWO Port RLC network

R = 100                                                               # Default values for R,L,C
L = 10**(-6)
C = 10**(-6)

H5 = sp.lti([1],[L*C,R*C,1])                                          # Defining the system transfer function

w,S,phi = H5.bode()                                                   # Findiing the magnitude and phase response of the system transfer function using the system.bode()

py.figure(5)                                                             # plotting the magnitude response on the semilogx plot
py.semilogx(w,S)
py.xlabel(r'$w$')
py.ylabel(r'$|H(s)|$')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.title(r'Magnitude_Response - Question_5')
py.savefig("suhas/figure5.png")
py.show()

py.figure(6)                                                             # plotting the phase response on the semilogx plot
py.semilogx(w,phi)
py.xlabel(r'$w$')
py.ylabel(r'Phase$(H(s))$')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.title(r'Phase_Response - Question_5')
py.savefig("suhas/figure6.png")
py.show()

    
# Question_6
# Response for sinusoidal input of RLC network 
# It acts as an Low-Pass filter 

H5 = sp.lti([1],[L*C,R*C,1])                                          # System transfer function for RLC network 


t2 = linspace(0,0.01,(10**5+1))                                       # Time for 0<t<10 milli seconds
vi = np.cos(1000*t2)-np.cos((10**6)*t2)                               # Input to the system 
t2,vo,svec = sp.lsim(H5,vi,t2)                                        # Finding the output for 0<t<10ms 

t3 = linspace(0,0.00003,1001)                                         # Time for 0<t<30 micro seconds
vi1 = np.cos(1000*t3)-np.cos((10**6)*t3)
t3,vo1,svec = sp.lsim(H5,vi1,t3)                                      # Finding the output for 0<t<30us

py.figure(7)                                                             # plotting output and observing the steady state response
py.plot(t2,vo)
py.xlabel(r'$t$')
py.ylabel(r'V_output')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.title(r'steady state Output of network - Question_6')
py.savefig("suhas/figure7.png")
py.show()

py.figure(8)                                                             # plotting output and observing the steady state response 
py.plot(t3,vo1)
py.xlabel(r'$t$')
py.ylabel(r'V_output')
py.grid(True, color = "grey", linewidth = "1.4", linestyle = "-") 
py.title(r'Output of network for T<30 u sec:Transient_response - Question_6')
py.savefig("suhas/figure8.png")
py.show()
