from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5]
y = [3,4,5,6,7]

z = np.zeros(len(x))
dx=dy = np.ones(len(x))
frequencias=[5,2,6,8,1]

ax1.bar3d(x,y,z,dx,dy,frequencias)

#ax1.set_xlabel('x axis')
#ax1.set_xlabel('y axis')
#ax1.set_xlabel('z axis')

plt.show()

