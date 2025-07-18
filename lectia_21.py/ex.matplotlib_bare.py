import matplotlib.pyplot as plt
import numpy as np
import random

x = ["red", "yellow","green","blue", "pink", "orange", "black"]
y = np.array([random.randint(1,100) for x in range(1,6 +2)])
plt.barh(x,y, color = x)
plt.title("culorile preferate")
plt.show()