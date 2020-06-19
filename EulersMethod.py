# Exploration into Eulers Method for numerically solving first order linear differential equations
import matplotlib.pyplot as plt
from sympy.interactive import printing
printing.init_printing(use_latex=True)
import sympy as sp
import numpy as np

x = sp.symbols('x')
y = sp.Function('F')(x)


# Eulers Method required a first order differential equation and an intital starting condition.

# The frist order differential equation which we are going to numerically solve
diffeq = Eq(f.diff(x,1)-4*f+2,0)
display(diffeq)


# plot the actual solution of the ODE
x = np.linspace(-10,10,100)
y = (2*x)*(x-1)+3
plt.plot(x,y)
plt.title('Particular Solution of a first order ODE')

# Using a numerical approximation technique to solve the same differential equation

def EulersMethod(numPointsToPlot,stepsize,initalX,initialY):

    xn = np.zeros(numPointsToPlot)
    yn = np.zeros(numPointsToPlot)

    xn[0] = initalX
    yn[0] = initialY

    for i in range(1, numPointsToPlot):
        xn[i] = xn[i-1]+h
        yn[i] = yn[i-1]+h*(4*xn[i-1]-2)
        
    return(xn,yn)
