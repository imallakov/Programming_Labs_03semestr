import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10.0, 10.0, 50)
y = np.tan(x) + 1.0/np.tan(x)
plt.plot(x, y,label="tan(x)+ctg(x)")

y = 2*np.cos(3*x)
plt.plot(x,y,label="2cos(3x)")
plt.legend()
plt.show()
