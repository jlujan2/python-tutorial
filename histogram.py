import numpy as np 
import matplotlib.pyplot as plt

x = np.random.normal(size=1000)
plt.hist(x)
plt.show()

plt.hist(x, normed=True, bins=np.linspace(-5, 5, 21))
plt.show()

x = np.random.gamma(2, 3, 10000)
plt.hist(x, bins = 30, normed=True, cumulative= True, histtype = "step")
plt.show()

plt.figure()
plt.subplot(221)
plt.hist(x, bins = 30)
plt.subplot(222)
plt.hist(x, bins = 30, normed=True)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative=True)
plt.subplot(224)
plt.hist(x, bins = 30, normed=True, cumulative= True, histtype = "step")
plt.show()