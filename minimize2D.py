# HW 10

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *
from scipy import optimize

# define 2D function
def func(z):
    x, y = z
    return (x-2)**2 + (y-2)**2 + 2

# minimize
result = optimize.minimize(func, [3,10])
minimum = result.x 
calls = result.nfev

print(minimum)
print("The number of function calls used was %i" %(calls))

# plot
x = np.arange(-2,7,1)
y = np.arange(-2,7,1)
X, Y = np.meshgrid(x,y)
function = (X-2)**2 + (Y-2)**2 + 2

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,function)
plt.xlabel("x")
plt.ylabel("y")
plt.title("My Function to Minimize")
ax.set_zlim(-5,20)

plt.show()


