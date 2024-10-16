import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def contrast(image, factor):
    mean = 128
    img_contrast = image.astype(np.float32)
    img_contrast = mean + factor * (img_contrast - mean)
    img_contrast = np.clip(img_contrast, 0, 255)
    
    return img_contrast.astype(np.uint8)

def blend(image1,f1,image2,f2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)
    
    result = (img1 * f1) + (img2 * f2)
    result = np.clip(result,0,256)
    
    return result.astype(np.uint8)

path = "kontras.jpg"
path2 = "kontras beda.jpg"

image = img.imread(path)
image2 = img.imread(path2)

hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

imgContrast = contrast(image, 1.5)
hist_c, bins_c = np.histogram(imgContrast.flatten(), bins=256, range=[0, 256])

plt.figure(figsize=(3, 3))

plt.subplot(3, 2, 1)
plt.imshow(image)
plt.title('sebelum kontras')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(imgContrast)
plt.title('setelah Kontrast')
plt.axis('off')

plt.subplot(3, 2, 3)
# plt.bar(bins[:-1], hist, width=1, color='black')
plt.plot(hist)
plt.title('sebelum kontras Histogram')
# plt.xlim([0, 256])

plt.subplot(3, 2, 4)
# plt.bar(bins_c[:-1], hist_c, width=1, color='black')
plt.plot(hist_c)
plt.title('Seudah Kontrast Histogram')
# plt.xlim([0, 256])

plt.subplot(3,2,5)
plt.imshow(blend(image,1,image2,1))

plt.show()
