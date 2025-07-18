import matplotlib.pyplot as plt
import numpy as np
import random

x = ["red", "yellow","green","blue", "pink", "orange", "black"]
y = np.array([random.randint(1,100) for x in range(1,6 +2)])
plt.subplot(1,2,1)
plt.bar(x,y, color = x)
plt.title("culorile preferate")
plt.subplot(1,2,2)

x = np.random.normal(10,70,250)
plt.hist(x)
plt.show()