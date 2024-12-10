# Perbandingan Deteksi Tepi: Robert vs Sobel

Proyek ini mengeksplorasi implementasi dan perbandingan hasil deteksi tepi menggunakan dua model deteksi tepi populer: **Robert** dan **Sobel**. Analisis ini mencakup implementasi, perbandingan hasil, dan kelebihan serta kekurangan masing-masing metode.

---

## 1. Deskripsi Metode

### Sobel

- **Kernel**: Menggunakan matriks 3x3 untuk menghitung gradien horizontal (Gx) dan vertikal (Gy).
- **Karakteristik**: Lebih presisi dalam mendeteksi perubahan intensitas yang halus, sehingga cocok untuk gambar yang memiliki detail gradasi.
- **Keunggulan**:
  - Mendeteksi tepi halus dengan baik.
  - Lebih stabil terhadap noise karena menggunakan area konvolusi yang lebih besar.
- **Kelemahan**:
  - Memerlukan lebih banyak komputasi dibanding Robert.

### Robert

- **Kernel**: Menggunakan matriks 2x2 untuk menghitung gradien diagonal (Gx) dan anti-diagonal (Gy).
- **Karakteristik**: Lebih sederhana dan cepat, cocok untuk lingkungan dengan keterbatasan sumber daya.
- **Keunggulan**:
  - Lebih cepat diproses karena kernel yang lebih kecil.
  - Deteksi tepi yang tajam lebih terlihat.
- **Kelemahan**:
  - Sensitif terhadap noise karena menggunakan area konvolusi yang lebih kecil.
  - Kurang efektif dalam menangkap detail pada perubahan gradasi.

---

## 2. Implementasi

Kode Python dalam proyek ini memanfaatkan pustaka berikut:

- `imageio` untuk membaca gambar.
- `numpy` untuk operasi matriks.
- `matplotlib` untuk visualisasi hasil.

### Struktur Kernel

#### Sobel

```plaintext
sobelX = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

sobelY = [[-1, -2, -1],
          [ 0,  0,  0],
          [ 1,  2,  1]]
```

#### Robert

```plaintext
robertX = [[ 1,  0],
           [ 0, -1]]

robertY = [[ 0,  1],
           [-1,  0]]
```

## 3. Kesimpulan

- Gunakan **Sobel** untuk analisis gambar yang memerlukan presisi tinggi dan mampu menangkap detail halus.
- Gunakan **Robert** untuk aplikasi yang membutuhkan hasil cepat atau bekerja dengan keterbatasan sumber daya.

---
