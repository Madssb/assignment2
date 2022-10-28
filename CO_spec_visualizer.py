import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("CO_spec.txt")
print(np.shape(data))
print(data[0,:])

plt.plot(data[:,0],data[:,1])
plt.show()








