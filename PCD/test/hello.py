import pandas as pd
import matplotlib.pyplot as plt

# Misalkan kita memiliki data dalam bentuk DataFrame
data = {
    'Tanggal': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'Nilai': [100, 95, 80, 85, 70]
}

df = pd.DataFrame(data)
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

# Plot grafik garis
plt.figure(figsize=(10, 6))
plt.plot(df['Tanggal'], df['Nilai'], marker='o', label='Nilai')

# Menyoroti penurunan
for i in range(1, len(df)):
    if df['Nilai'][i] < df['Nilai'][i - 1]:
        plt.plot(df['Tanggal'][i-1:i+1], df['Nilai'][i-1:i+1], color='red', linewidth=2.5)

plt.title('Grafik Penurunan Nilai')
plt.xlabel('Tanggal')
plt.ylabel('Nilai')
plt.legend()
plt.grid(True)
plt.show()