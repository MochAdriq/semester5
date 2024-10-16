import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt


def br(image,factor):
    bright_image = image.astype(np.float32)
    bright_image = bright_image + factor

    bright_image = np.clip(bright_image,0,255)

    return bright_image.astype(np.uint8)

path = "C:\\Users\\KOMPUTER JARKOM 29\\Documents\\TI22E 2024\\1.jpg"
image = img.imread(path)

r_image = image[:,:,0]

hist_r, bist_r = np.histogram((br(image,200)).flatten(), bins=256, range=[0,256])
hist_r, bist_r = np.histogram((br(image,20)).flatten(), bins=256, range=[0,256])


plt.figure(figsize=(100,100))
plt.subplot(2,2,1)
plt.imshow(br(image,200))
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(br(image,100))
plt.axis("off")

plt.subplot(2,2,3)
plt.plot(hist_r, color="blue", label="histogram r awal")

plt.show()
