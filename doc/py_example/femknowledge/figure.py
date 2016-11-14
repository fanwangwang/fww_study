# 给出一个函数 $f(x) = x*x$ ,作出它的图像，设坐标比例相同，且去除坐标轴

import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
plt.figure(2)
x = np.linspace(-30,30,120)
plt.figure(1)
plt.plot(x,x*x)
plt.figure(2)
plt.plot(x,np.sin(x))
plt.show()
