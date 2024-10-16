import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def equal(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_normal = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    img_equal = np.interp(image.flatten(), bins[:-1],cdf_normal)
    return img_equal.reshape(image.shape).astype(np.uint8)

path = "kontras beda lagi.jpg"

image = img.imread(path)

equalimg = equal(image)

hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
hist_e, bins_e = np.histogram(equalimg.flatten(), bins=256, range=[0, 256])


plt.figure(figsize=(3, 3))
plt.subplot(2, 2, 1)
plt.imshow(image)

plt.subplot(2, 2, 2)
plt.imshow(equalimg)

plt.subplot(2, 2, 3)
plt.plot(hist)

plt.subplot(2, 2, 4)
plt.plot(hist_e)

plt.show()
