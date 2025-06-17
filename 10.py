import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(10000, 3)
colors = ['green', 'blue', 'lime']

plt.hist(x,  density=True, histtype='bar', color=colors, label=colors)

plt.legend(fontsize=10)
plt.title('matplotlib.pyplot.hist() Example', fontweight='bold')

plt.show()