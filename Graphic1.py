import matplotlib.pyplot as plt
import numpy as np
import math

L = 100
V = 10
x = np.arange(0,L,0.1)
y = x*np.cos(x)



plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.show()