import numpy as np
import matplotlib.pyplot as plt

# Euler Methods to solve a non linear ODE for a simple Pendulum
def Euler(y,derivative,timestep,state):
    y[state+1] = y[state] + (derivative * timestep)
    return y

    
# Euler-Cromer Method to solve a non linear ODE for a simple pendulum
def EulerCromer(y1,y2,timestep,state):
    y2[state+1] = y2[state] + ((-(g/l)*np.sin(y1[state]))) * dt 
    y1[state+1] = y1[state] + (y2[state+1]) * dt
    return y1,y2                            

    
N = 2500
ti = 0
tf = 25
dt = (tf-ti) / (N-1)
t = np.linspace(ti,tf,N)
g = 9.81
l = 1

thetaE = np.zeros([N])
omegaE = np.zeros([N])
                               

thetaC = np.zeros([N])
omegaC = np.zeros([N])

thetaE[0] = 0.2
omegaE[0] = 0.0
thetaC[0] = 0.2
omegaC[0] = 0.0


for i in range(0,N-1):
    # Split Second Order ODE into two first order ODE's
    thetaDerivative = omegaE[i]
    omegaDerivative = -(g/l)*np.sin(thetaE[i])
    omegaE = Euler(omegaE,omegaDerivative,dt,i)
    thetaE = Euler(thetaE,thetaDerivative,dt,i)
    
    omegaC, thetaC = EulerCromer(omegaC,thetaC,dt,i)
     
    
    
fig,a = plt.subplots(2, 1, figsize=(10,10)) 
a[0].plot(t,thetaE)
a[0].set_title('Oscillations of a single pendulum using Eulers Method')
a[0].set_ylabel('omega (radians)')
a[0].set_xlabel('time (seconds)')     
a[1].set_title('Oscillations of a single pendulum using  Euler-Cromer Method')
a[1].plot(t,thetaC,'g')
a[1].set_ylabel('omega (radians)')
a[1].set_xlabel('time (seconds)')
plt.tight_layout()
# Oscillations grows with time due to inaccuracy of the Euler Numerical Method. Hence Euler's Method should only be
# used to solve first order linear ODE's
