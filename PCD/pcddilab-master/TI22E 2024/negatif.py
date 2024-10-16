import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt


path = "C:\\Users\\KOMPUTER JARKOM 29\Documents\TI22E 2024\\1neg.jpg"

image = img.imread(path)

# S=L-1-R

image_neg = 255 - image

r_image = image[:,:,0]
r_neg  = image_neg[:,:,0]

hist_r, bist_r = np.histogram(r_image.flatten(), bins=256, range=[0,256])
hist_r_neg, bist_r_neg = np.histogram(r_neg.flatten(), bins=256, range=[0,256])

plt.figure(figsize=(0.9,0.9))

plt.subplot(2,2,1)
plt.plot(hist_r, color="blue", label="histogram r awal")
plt.legend()

plt.subplot(2,2,2)
plt.imshow(image_neg)
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(image)
plt.axis("off")

plt.subplot(2,2,3)
plt.plot(hist_r_neg, color="red", label="histogram r akhir")
plt.legend()

plt.show()
# img.imwrite("C:\\Users\\KOMPUTER JARKOM 29\Documents\TI22E 2024\\1negneg.jpg",image_neg)