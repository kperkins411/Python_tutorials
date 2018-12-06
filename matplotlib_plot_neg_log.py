import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 1.0, 100)
y = -np.log(x)
z=  -(1-2*x)*np.log(x)

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1, -5,5])
line  = plt.plot(x, y, lw=2)
line2 = plt.plot(x, z, lw=2)
plt.show()

