"""
        EE2703 Applied Programming Lab - 2022
        Assignment 5
        Name : Suhas C
        Roll Number : EE20B132
        Date : 11 March 2022
"""
#Import modules for the code.									
from pylab import *									#importing pylab
import sys										#importing sys
import mpl_toolkits.mplot3d.axes3d as p3

#Assigning default values for the parameters
Nx = 25 								
Ny = 25								
radius = 8				
Niter = 1500

#For the case where parameters given through command line.
if(len(sys.argv)>1 and len(sys.argv)< 5 ):
	Nx = int(sys.argv[1])
	Ny = int(sys.argv[2])
	Niter = int(sys.argv[3])
elif(len(sys.argv)>= 5):
	print('No. of argumnets must be less than 5')
	exit()

#Creating the required functions for the code.
	
def fit_exp(x,A,B):									#defining the function fit_exp(x,A,B)
    return A*np.exp(B*x)								#Returning the value to A*np.exp(B*x) 
    
def error_fit(x,y):									#defining the function error_fit(x,y) 
    log_y=np.log(y)
    x_vec=np.zeros((len(x),2))
    x_vec[:,0]=x
    x_vec[:,1]=1
    B,log_A=np.linalg.lstsq(x_vec, np.transpose(log_y))[0]
    return (np.exp(log_A),B)								#Returning the value to (np.exp(logA),B)

#Function to plot initial contour
def plot_initial_contour():
    figure(0)
    plot(ii[0]/Nx-0.48,ii[1]/Ny-0.48,'ro',label="V = 1")
    title("Initial Potential Contour")
    xlim(-0.5,0.5)
    ylim(-0.5,0.5)
    xlabel(r'$X\rightarrow$')
    ylabel(r'$Y\rightarrow$')
    grid(True)
    legend()
    show()

#Function to semilog plot error vs iteration
def semilog_err_vs_iter():
    figure(1)
    semilogy(n,errors)
    semilogy(n[::50],errors[::50],'ro')
    title("Error versus iteration")
    xlabel(r'$Iteration\rightarrow$',size=15)
    ylabel(r'$Error\rightarrow$',size=15)
    grid(True)
    show()

#Function to plot loglog error vs iteration
def loglog_err_vs_iter():
    figure(2)
    loglog(n,errors)
    loglog(n[::50],errors[::50],'ro')
    title("Error versus iteration in a loglog plot")
    xlabel(r'$Iteration\rightarrow$',size=15)
    ylabel(r'$Error\rightarrow$',size=15)
    grid(True)
    show()

#Plotting best firt of error in semilog
def semilog_bestfit_err():
    fig3, ax1 = plt.subplots()
    ax1.semilogy(range(Niter)[::50],errors[::50],label='original')
    ax1.semilogy(range(Niter)[::50],fit_exp(range(Niter)[::50],A,B),label='fit1')
    ax1.semilogy(range(Niter)[::50],fit_exp(range(Niter)[::50],A_500,B_500),label='fit2')
    title("Best fit for error on semilog scale ")
    xlabel(r'$Iteration\rightarrow$',size=15)
    ylabel(r'$Error\rightarrow$',size=15)
    grid(True)
    legend()
    show()

#plotting best fit of error in loglog
def loglog_bestfit_err():
    fig4, ax2 = plt.subplots()
    ax2.loglog(range(Niter)[::50],errors[::50],label='original')
    ax2.loglog(range(Niter)[::50],fit_exp(range(Niter)[::50],A,B),label='fit1')
    ax2.loglog(range(Niter)[::50],fit_exp(range(Niter)[::50],A_500,B_500),label='fit2')
    title("Best fit for error on loglog scale ")
    xlabel(r'$Iteration\rightarrow$',size=15)
    ylabel(r'$Error\rightarrow$',size=15)
    grid(True)
    legend()
    show()
# Plotting the contour of potential.
def plot_contour_potential():
    figure(5)
    contourf(X,Y,phi)
    plot(ii[0]/Nx-0.48,ii[1]/Ny-0.48,'ro',label="V = 1")
    title("Contour plot of potential")
    xlabel(r'$X\rightarrow$')
    ylabel(r'$Y\rightarrow$')
    colorbar()
    grid(True)
    legend()
    show()

# Plotting the surface plots of potential.
def surf_plot_potential():
    fig1=figure(6)
    ax=p3.Axes3D(fig1, auto_add_to_figure = False)
    fig1.add_axes(ax) 
    title("The 3-D surface plot of the potential")
    xlabel(r'$X\rightarrow$')
    ylabel(r'$Y\rightarrow$')
    surf = ax.plot_surface(X, Y, phi, rstride=1, cstride=1, cmap=cm.jet)
    fig1.colorbar(surf)   
    show()

# plotting of the current vector plot along with the potential.
def plot_currVec_and_potential():
    figure(7)
    quiver(X,Y,J_x,J_y)
    plot(ii[0]/Nx-0.48,ii[1]/Ny-0.48,'ro')
    title("The vector plot of the current flow")
    xlabel(r'$X\rightarrow$')
    ylabel(r'$Y\rightarrow$')
    show()   

# Creating the respective matrices and initializing them.
phi = zeros((Ny,Nx))								
x = linspace(-0.5,0.5,Nx)							
y = linspace(-0.5,0.5,Ny)
X,Y = meshgrid(x,-y)				
n = array(range(Niter))							
niter = arange(500,1500,0.1)							
				

#Points inside the circle 
A = (X*X) + (Y*Y)
ii = where(A <= (0.35*0.35))

phi[ii] = 1.0 #phi = 1 for all the points inside the circle

#Perform the iteration and to calculate the error in the potential.
errors = empty((Niter,1))
for k in range(Niter):
	oldphi = phi.copy()
	phi[1:-1,1:-1] = 0.25*(phi[1:-1,0:-2] + phi[1:-1,2:] + phi[0:-2,1:-1] + phi[2:,1:-1])

#Applying the boundary conditions.
	phi[1:-1,0] = phi[1:-1,1]
	phi[1:-1,-1] = phi[1:-1,-2]
	phi[0,1:-1] = phi[1,1:-1]
	phi[ii] = 1.0
	errors[k]=(abs(phi-oldphi)).max()

# The exponent part of the error values.
c_approx_500 = lstsq(c_[ones(Niter-500),arange(500,Niter)],log(errors[500:]),rcond=None)#estimating laplace by lstsq function above 500 iterations. 
A_500,B_500 = exp(c_approx_500[0][0]),c_approx_500[0][1]
print("The values of A and B for the iterations after 500 are: ",A_500,B_500)

c_approx = lstsq(c_[ones(Niter),arange(Niter)],log(errors),rcond=None)		#estimating laplace by lstsq function for all iterations.
A, B = exp(c_approx[0][0]), c_approx[0][1]
print("The values of A and B are: ",A,B)

# The current density vectors is.
J_x = zeros((Ny, Nx))
J_y = zeros((Ny, Nx))
J_x[1:-1, 1:-1] = 0.5*(phi[1:-1, 0:-2] - phi[1:-1, 2:])
J_y[1:-1, 1:-1] = 0.5*(phi[2:, 1:-1] - phi[0:-2, 1:-1])

#Calling the functions to plot the graphs
plot_initial_contour()
semilog_err_vs_iter()
loglog_err_vs_iter()
semilog_bestfit_err()
loglog_bestfit_err()
plot_contour_potential()
surf_plot_potential()
plot_currVec_and_potential()

#End of the program

