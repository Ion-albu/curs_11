import numpy as nmp
import matplotlib.pyplot as plt
import random

x = nmp.array([random.randint(1,100) for x in range(1,100)])
y = nmp.array([random.randint(1,100) for y in range(1,100)])
plt.subplot(1,2,1)
colors = nmp.array([random.randint(1,100)for x in range(1,100)])
sizes =nmp.array([random.randint(1,100)for x in range(1,100)])
plt.scatter(x,y,c = colors, cmap = "CMRmap", s = sizes, alpha = 0.5)
plt.colorbar()
#plt.show()

x = ["ian", "feb", "mart", "april", "mai"]
y = [1000, 1200,1500,1700,500]
y1 = [200, 500, 1800, 1200, 0]
plt.subplot(2,2,2)
plt.plot(x,y,"s-r",label = "magazinul B")
plt.plot(x, y1, "o-y", label = "magazinul A")
plt.title("numarul de vanzari")
plt.xlabel("lunile anului")
plt.ylabel("numarul de vanzari")
plt.grid()
plt.legend()


x = nmp.array([random.randint(1,100) for x in range(1,100)])
y = nmp.array([random.randint(1,100) for y in range(1,100)])
plt.subplot(3,2,3)
colors = nmp.array([random.randint(1,100)for x in range(1,100)])
sizes =nmp.array([random.randint(1,100)for x in range(1,100)])
plt.scatter(x,y,c = colors, cmap = "CMRmap", s = sizes, alpha = 0.5)
plt.colorbar()
plt.show()

# plt.scatter(x,y)
# plt.show()