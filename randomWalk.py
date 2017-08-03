import random 
import numpy as np 
import matplotlib.pyplot as plt
import time

X_0 = np.array([[0], [0]])
delta_x = np.random.normal(0, 1, (2,10000)) 
X = np.cumsum(delta_x, axis=1)
Y = np.concatenate((X_0, X), axis = 1)
plt.plot(Y[0], Y[1], "ro-")
print (Y)
plt.show()