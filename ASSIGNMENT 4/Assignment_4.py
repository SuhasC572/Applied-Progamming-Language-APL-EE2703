'''
EE2703 Applied Programming Lab
Submission for Assignment-4
Name: Suhas C
Roll Numer: EE20B132
Date : 11-03-2022
'''

import os
import sys
from turtle import color, width
import numpy as np
import scipy as sp
import matplotlib.pyplot 
from  pylab import *
from scipy import integrate


pi = np.pi
e = np.e

#Defining the Functions exponential and cos(cos(x))
def f(x):
    return np.exp(x)
def g(x):
    return np.cos(np.cos(x))


x = np.linspace(-2*pi,4*pi,100)  #Dividing the 0 to 2*pi into 100 equal intervals

#Plot of g(x) vs x 
figure(1)
grid(True)
plot(x,g(x))
title('Plot of g(x)')
xlabel('x')
ylabel('g(x)')
show()

#Plot of f(x) vs x in semilog scale
figure(2)
grid(True)
semilogy(x,f(x))
title('Plot of f(x) in semilog scale')
xlabel('x')
ylabel('f(x)')
show()

#plot of f(x) vs x
figure(3)
grid(True)
plot(x,f(x))
title('Plot of f(x)')
xlabel('x')
ylabel('f(x)')
show()


#Functions for finding the coefficients of the fourier series
def m(x,k):        
    return f(x)*np.cos(k*x)
def n(x,k):
    return f(x)*np.sin(k*x)
def o(x,k):
    return g(x)*np.cos(k*x)
def p(x,k):
    return g(x)*np.sin(k*x)


#Defining the empty matrixes for the fourier coefficients 
a_coeff_of_f = np.zeros(26,)
b_coeff_of_f = np.zeros(25,)
a_coeff_of_g = np.zeros(26,)
b_coeff_of_g = np.zeros(25,)

#Integrating using the Quad integrate method
for i in range(26):
    a_coeff_of_f[i],_ = sp.integrate.quad(m,0,2*pi,(i,))
    a_coeff_of_g[i],_ = sp.integrate.quad(o,0,2*pi,(i,))
for i in range(25):
    b_coeff_of_f[i],_ = sp.integrate.quad(n,0,2*pi,(i+1,))
    b_coeff_of_g[i],_ = sp.integrate.quad(p,0,2*pi,(i+1,)) 

#Dividing the Coefficients by pi and the first coefficient by 2*pi
a_coeff_of_f /= pi
b_coeff_of_f /= pi
a_coeff_of_g /= pi
b_coeff_of_g /= pi
a_coeff_of_f[0] /= 2
a_coeff_of_g[0] /= 2

#An array to store all a and b coefficients of function f
F = [None]*(len(a_coeff_of_f)+len(b_coeff_of_f))
F[0] = a_coeff_of_f[0]
F[1::2] = a_coeff_of_f[1:]
F[2::2] = b_coeff_of_f
F = np.asarray(F)

#Plot of fourier coefficient of f(x) vs n Using Direct integration method 
#In semilog scale
figure(4)
grid(True)
semilogy(abs(F),'o',color = 'r',markersize = 4)
title('Fourier Coefficients for f(x) by direct integration')
xlabel('n')
ylabel('Fourier Coefficients') 
legend(loc="best")
show()

#Plot of fourier coefficient of f(x) vs n Using Direct integration method 
#In loglog scale
figure(5)
grid(True)
loglog(abs(F),'o',color = 'r',markersize = 4)
title('Fourier Coefficients for f(x) by direct integration')
xlabel('n')
ylabel('Fourier Coefficients') 
show()

#An array to store all a and b coefficients of function g
G = [None]*(len(a_coeff_of_f)+len(b_coeff_of_f))
G[0] = a_coeff_of_g[0]
G[1::2] = a_coeff_of_g[1:]
G[2::2] = b_coeff_of_g
G = np.asarray(G)

#Plot of fourier coefficient of g(x) vs n Using Direct integration method 
#In semilog scale
figure(6)
grid(True)
semilogy(abs(G),'o',color = 'r',markersize = 4)
title('Fourier Coefficients for g(x) by direct integration')
xlabel('n')
ylabel('Fourier Coefficients') 
show()


#Plot of fourier coefficient of g(x) vs n Using Direct integration method 
#In loglog scale
figure(7)
grid(True)
loglog(abs(G),'o',color = 'r',markersize = 4)
title('Fourier Coefficients for g(x) by direct integration')
xlabel('n')
ylabel('Fourier Coefficients') 
show()

#For finding the coefficients using the lstsq method
X = np.linspace(0,2*pi,401)
X = X[:-1]
b1 = f(X)
b2 = g(X)
A = np.zeros((400,51))
A[:,0] = 1
for k in range(1,26):
    A[:,2*k-1] = np.cos(k*X)
    A[:,2*k] = np.sin(k*X)

c1 = np.linalg.lstsq(A,b1,rcond = -1)[0]
c2 = np.linalg.lstsq(A,b2,rcond = -1)[0]

#Plot of fourier coefficient of f(x) vs n Using lstsq method 
figure(8)
grid(True)
plot(c1,'o',color = 'g')
title('Fourier Coefficients calculated using lstsq method')
xlabel('n')
ylabel('Coefficients')
show()

#Plot of fourier coefficient of g(x) vs n Using lstsq method 
figure(9)
grid(True)
plot(c2,'o',color = 'g')
title('Fourier Coefficients calculated using lstsq method')
xlabel('n')
ylabel('Coefficients')
show()


f_final_value = A.dot(c1)

#Plot of Reconstructed and the original function of f(x)
figure(10)
grid(True)
plot(X,f_final_value,'-',color = 'g')
plot(X,f(X),'-.',color = 'b')
title(' Original Function and Reconstructed Function from Fourier Coefficients')
xlabel('x')
ylabel('f(x)')
legend(['original','reconstructed'])
show()


g_final_value = A.dot(c2)

#Plot of Reconstructed and the original function of g(x)
figure(11)
grid(True)
plot(X,g_final_value,'-',color = 'g')
plot(X,g(X),'-.',color = 'b')
title(' Original Function and Reconstructed Function from Fourier Coefficients')
xlabel('x')
ylabel('g(x)')
legend(['original','reconstructed'])
show()


print("Mean Error in f(x) = exp(x) is {}".format(np.mean(abs(c1 - F))))
print("Mean Error in g(x) = cos(cos(x)) is {}".format(np.mean(abs(c2 - G))))
