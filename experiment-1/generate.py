import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

template = np.asarray(Image.open("template.bmp"))

template = template.sum(axis=2)/3

for i in range(1, 255):
    m = template.copy()

    tone_row = m[i]
    for k in range(len(tone_row)):
        m[i][k] = 255

    im = Image.fromarray(m.astype(np.uint8), mode="L")
    im.save(f"inputs/{i}.bmp")
