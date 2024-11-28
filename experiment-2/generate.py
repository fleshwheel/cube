import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

template = np.asarray(Image.open("template.bmp").convert("RGB"))

#template = template.sum(axis=2)/3

def mutate(img):
    idx = int(np.random.random() * (len(img)))
    row = img[idx]
	
    if np.random.random() > 0.5:
        color = [255, 0, 0]
    else:
        color = [0, 255, 0]

    for k in range(len(row)):
        row[k] = color

for _ in range(1, 255):
    m = template.copy()

    mutate(m)

    while np.random.random() < 0.5:
        mutate(m)

    im = Image.fromarray(m.astype(np.uint8), mode="RGB")
    im.save(f"inputs/{_}.bmp")
