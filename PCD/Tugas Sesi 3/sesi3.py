import numpy as np
import imageio.v3 as image
import matplotlib.pyplot as plt

# Path ke gambar
path = "PCD/TUGAS SESI 2/assets/citra.jpeg"
image_source = image.imread(path)

# Ekstrak channel warna
red_ch = image_source[:,:,0]  
green_ch = image_source[:,:,1]
blue_ch = image_source[:,:,2]

# Konversi ke grayscale menggunakan bobot kanal RGB
grayscale_weighted = (0.2989 * red_ch + 0.5870 * green_ch + 0.1140 * blue_ch).astype(np.uint8)

# Buat gambar grayscale dalam format RGB (3 channel dengan nilai yang sama)
image_gray = np.zeros_like(image_source)
image_gray[:,:,0] = grayscale_weighted  # Red channel
image_gray[:,:,1] = grayscale_weighted  # Green channel
image_gray[:,:,2] = grayscale_weighted  # Blue channel

# Hitung histogram untuk gambar asli dan grayscale
hist, bist = np.histogram(image_source.flatten(), bins=256, range=[0,256])
hist_g, bist_g = np.histogram(image_gray.flatten(), bins=256, range=[0,256])

# a. Hitung jumlah total piksel untuk setiap intensitas
# Menggunakan numpy untuk menghitung histogram intensitas grayscale
histogram, bin_edges = np.histogram(grayscale_weighted, bins=256, range=(0, 255))

# Hitung total piksel (jawaban untuk soal a)
total_pixels = np.sum(histogram)
print(f"Jumlah total piksel: {total_pixels} piksel")

# Menemukan intensitas yang dominan (jawaban untuk soal b)
dominant_intensity = np.argmax(histogram)
dominant_count = histogram[dominant_intensity]
print(f"Intensitas yang dominan: {dominant_intensity} dengan {dominant_count} piksel")

# Visualisasi hasil
plt.figure(figsize=(10,10))

plt.subplot(3,2,1)
plt.imshow(image_source)
plt.axis("off")
plt.title("Citra Asli")

plt.subplot(3,2,2)
plt.plot(hist)
plt.title("Histogram Asli")

plt.subplot(3,2,3)
plt.imshow(image_gray)
plt.axis("off")
plt.title("Citra Grayscale")

plt.subplot(3,2,4)
plt.plot(hist_g)
plt.title("Histogram Grayscale")

plt.subplot(3,2,5)
plt.hist(grayscale_weighted.ravel(), bins=256, range=[0, 256], color='black')
plt.title('Histogram Intensitas')
plt.xlabel('Intensitas')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Cetak jumlah piksel untuk setiap intensitas (opsional, jika perlu ditampilkan)
for i in range(256):
    print(f"Intensitas {i}: {histogram[i]} piksel")
