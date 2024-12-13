import matplotlib.pyplot as plt
import numpy as np

x_degrees = np.arange(0, 361, 1)
x_radians = np.radians(x_degrees)

y = np.sin(x_radians)

plt.plot(x_degrees, y)
plt.show()