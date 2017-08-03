import random 
import numpy as np 
import matplotlib.pyplot as plt
import time

#print (random.choice(["H", "T"]))

#print (random.choice(range(1,7)))

#print (random.choice([range(1,7), range(1,9), range(1,11)]))

random.choice([1,2,3,4,5,6])

rolls = []
for k in range(1):
	rolls.append(random.choice([1,2,3,4,5,6]))
plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7))

start_time = time.clock()
ys = []
for rep in range(1000000):
	y = 0
	for k in range(10):
		x = random.choice([1,2,3,4,5,6])
		y = y + x
	ys.append(y)
end_time = time.clock()
	
print (end_time - start_time)
plt.hist(ys)
plt.show()