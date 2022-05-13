"""
Quarter wavelength l = 0.5m
Speed of Light  = 2.99e8m/sec
Permeability of free space = uo = 4e-7*pi
Number of sections in each half of the antenna 
N = 4
 N = 100
Current injected into the antenna = 1.0
Radius of the wire a = 0.01 m

Dependent Parameters
Wavelength = l*4.0 m
Frequency f = c/lamda Hz
Wave number  k = 2*pi/lamda
Wave Number dz = l/N
"""

from pylab import *
import numpy as np
import math as ma
from cmath import pi
import matplotlib.pyplot as plt


l = 0.5
c = 2.9979e8
mu0 = 4e-7*pi
N = 4
Maximum_Current = 1
a = 0.01
lamda = l*4
f = c/lamda
k = 2*pi/lamda
dz = l/N


"""Question 1"""
#Calculating Vector Z 
z = np.linspace(-l,l,2*N+1)

#Calculating u vector
u = np.arange(1, 2*N)
#Removing the middlemost element
u = np.delete(u, N-1, axis=0)

#Calculating the I vector(standard expression ) - the actual I
Current_Vector = np.zeros(2*N+1)
Current_Vector[0:N] = Maximum_Current*sin(k*(l+z[0:N])) # for -l < z < 0
Current_Vector[N:2*N+1] = Maximum_Current*sin(k*(l-z[N:2*N+1])) # for 0 < z < l
I = Current_Vector

#Applying the given Boundary Condition

Unknown_Current=I[u]

""" QUESTION - 2 """
# Function to compute and return matrix M, H_phi
def H_p(J,n=N,r=a):
	Matrix = (1/(2*pi*r))*(identity(2*N-2))
	V = np.dot(Matrix,J)
	return Matrix,V

Matrix,H_phi = H_p(Unknown_Current,N,a) # Getting the matrix M

""" QUESTION - 3 """
# Computing vectors Rz, Ru and matrices PB, P
r = a
def Rij(z,r=a):
	ziz,zjz = np.meshgrid(z,z) #Return coordinate Matrices from coordinate vectors
	Radius = sqrt((ziz-zjz)**2 + r**2*np.ones((2*N+1,2*N+1)))
	return Radius

Rz = Rij(z,a)

def Riju(z,u,r=a):
	ziu,zju = np.meshgrid(z[u],z[u]) #Return coordinate Matrices from coordinate vectors
	R = sqrt((ziu-zju)**2 + r**2*np.ones((2*N-2,2*N-2)))
	return R
	
Ru = Riju(z,u,a)

def pij(r,k=k,z=dz):
	P = ((mu0/(4*pi))*(exp(-1j*k*r))*z/r)
	return P
	
P_ij = pij(Ru,k,dz)

RiN = Rz[N]
RiN = np.delete(RiN,[0,N,2*N],0)

Eq_0 = (exp(-1j*k*RiN))

P_B = ((mu0/(4*pi))*(Eq_0)*dz/RiN)

Eq_1 = (-1j*k/Ru)-(1/Ru**2)
Eq_2 = (-1j*k/RiN)-(1/RiN**2)

""" QUESTION - 4 """
# Computing the matrices Qij and QB

Q_ij = -P_ij*(r/mu0)*(Eq_1)
Q_B = -P_B*(r/mu0)*(Eq_2)

""" QUESTION - 5 """
# Solving for the current vector, I and comparing with the actual expression
#M1 = identity(2*N-2)/(2*pi*a)

Matrix_1 = np.identity(2*N-2)/(2*pi*r)
Unknown_Current_1 = dot(linalg.inv(Matrix_1-Q_ij),Q_B)

#Printing all the Matrices
print((Rz).round(2))
print((Ru).round(2))
print((P_ij).round(2))
print((P_B).round(2))
print((Q_ij).round(2))
print((Q_B).round(2))

# Finding I(expected value of current)
# Adding the three values given in question

Current_1 = np.insert(Unknown_Current_1,0,0)
Current_1 = np.insert(Current_1,N,Maximum_Current)
Current_1 = np.insert(Current_1,2*N,0)

plt.figure(1)
plt.plot(z,Current_1)
plt.plot(z,I)
plt.grid(True)
plt.savefig("/figure1.png")
plt.show()

print((I).round(2))
print((Current_1).round(2))