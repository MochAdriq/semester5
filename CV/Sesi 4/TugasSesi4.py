import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread('CV\Sesi 4\otak1.jpg')
img2 = cv2.imread('CV\Sesi 4\otak2.jpg')

# Menerapkan Gaussian filter
gaussian_filtered_img = cv2.GaussianBlur(img, (5, 5), 0)
gaussian_filtered_img2 = cv2.GaussianBlur(img2, (5, 5), 0)

# Menampilkan hasil
plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.imshow(img)
plt.axis("off")
plt.title("Gambar 1 awal")

plt.subplot(2,2,2)
plt.imshow(img2)
plt.axis("off")
plt.title("Gambar 2 awal")

plt.subplot(2,2,3)
plt.imshow(gaussian_filtered_img)
plt.axis("off")
plt.title("Gambar 1 akhir")

plt.subplot(2,2,4)
plt.imshow(gaussian_filtered_img2)
plt.axis("off")
plt.title("Gambar 2 akhir")
plt.show()