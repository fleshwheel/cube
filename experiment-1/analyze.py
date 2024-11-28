import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def image_entropy(filename):
    im = np.asarray(Image.open(filename))
    im = im # to account for sqrt scaling
    totals = im.sum(axis=1)
    return totals.sum()

x = []
y = []
for filename in os.listdir("data"):
    x.append(int(filename.split(".")[0]))
    y.append(image_entropy(f"data/{filename}"))

data = list(zip(x, y))
data.sort(key=lambda x: x[0])

x = [z[0] for z in data]
y = [z[1] for z in data]

plt.plot(x, y)


plt.show()
