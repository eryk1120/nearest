import numpy as np 
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

rand = np.random.RandomState(42)
x = rand.rand(10,2)
plt.scatter(x[:, 0], x[:, 1], s=100);
#plt.show()
dist_sq = np.sum((x[:,np.newaxis,:]-x[np.newaxis,:,:])**2,axis = -1)
print (dist_sq)
closest = np.argsort(dist_sq,axis=1)
print ( closest)
for i in range(x.shape[0]):
	plt.plot(*zip(x[i],x[closest[i,1]]),color='blue')
plt.show()