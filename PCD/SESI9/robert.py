import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
image = img.imread("C:/Users/User/Documents/nitipAdriq/semester5/PCD/lena.png", mode='F')

# Kernel Robert
robertX = np.array([
    [1, 0],
    [0, -1]
])

robertY = np.array([
    [0, 1],
    [-1, 0]
])

# Padding untuk Robert
imgPad = np.pad(image, pad_width=1, mode='constant', constant_values=0)

# Inisialisasi Gx, Gy, dan G untuk Robert
Gx_r = np.zeros_like(image)
Gy_r = np.zeros_like(image)

# Proses Convolution untuk model Robert
for y in range(1, imgPad.shape[0] - 1):
    for x in range(1, imgPad.shape[1] - 1):
        region = imgPad[y-1:y+1, x-1:x+1]  # 2x2 region
        Gx_r[y-1, x-1] = (region * robertX).sum()
        Gy_r[y-1, x-1] = (region * robertY).sum()

G_r = np.sqrt(Gx_r**2 + Gy_r**2)
G_r = (G_r/G_r.max()) * 255
G_r = np.clip(G_r, 0, 255)
G_r = G_r.astype(np.uint8)

# Thresholding untuk Robert
thr_r = np.where(G_r > 50, 255, 0).astype(np.uint8)

# Plot hasil Sobel dan Robert
plt.figure(figsize=(15, 15))

# Hasil Model Sobel
plt.subplot(2, 4, 1)
plt.title("Sobel Gx")
plt.imshow(Gx, cmap='gray')

plt.subplot(2, 4, 2)
plt.title("Sobel Gy")
plt.imshow(Gy, cmap='gray')

plt.subplot(2, 4, 3)
plt.title("Sobel G")
plt.imshow(G, cmap='gray')

plt.subplot(2, 4, 4)
plt.title("Sobel Threshold")
plt.imshow(thr, cmap='gray')

# Hasil Model Robert
plt.subplot(2, 4, 5)
plt.title("Robert Gx")
plt.imshow(Gx_r, cmap='gray')

plt.subplot(2, 4, 6)
plt.title("Robert Gy")
plt.imshow(Gy_r, cmap='gray')

plt.subplot(2, 4, 7)
plt.title("Robert G")
plt.imshow(G_r, cmap='gray')

plt.subplot(2, 4, 8)
plt.title("Robert Threshold")
plt.imshow(thr_r, cmap='gray')

plt.tight_layout()
plt.show()
