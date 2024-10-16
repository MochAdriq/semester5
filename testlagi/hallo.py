import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file Excel
# Gantilah 'Data Petani Kabupaten Sukabumi.xlsx' dan 'Sheet1' sesuai dengan nama file dan sheet Anda
df = pd.read_excel('C:\\Users\\User\\Documents\\nitip adriq\\semester5\\testlagi\\Data Petani Kabupaten Sukabumi.xlsx', sheet_name='Sheet1')

# Misalkan kolom 'Tanggal' dan 'Produksi' ada dalam dataset
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

# Plot grafik garis
plt.figure(figsize=(12, 6))
plt.plot(df['Tanggal'], df['Produksi'], marker='o', label='Produksi')

# Menambahkan anotasi untuk titik tertentu
for i in range(len(df)):
    if df['Produksi'][i] < df['Produksi'].mean():  # Misal, anotasi jika di bawah rata-rata
        plt.annotate(f"{df['Produksi'][i]}", (df['Tanggal'][i], df['Produksi'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Tren Produksi Pertanian')
plt.xlabel('Tanggal')
plt.ylabel('Produksi')
plt.legend()
plt.grid(True)
plt.show()