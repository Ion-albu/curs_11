import matplotlib.pyplot as plt
lunile = ["ian", "feb", "mart", "april", "mai"]
preturile = [1000, 1200, 1500,500, 200]

plt.plot(lunile, preturile, marker = ".")
plt.title("veniturile pe luna")
plt.xlabel("luni")
plt.ylabel("numere")
plt.grid(True)
plt.show()