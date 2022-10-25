import matplotlib.pyplot as plt

import numpy as np
x = np.array([1,2,3,4,5,6,7])

plt.plot(x, x ** 2, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show()

