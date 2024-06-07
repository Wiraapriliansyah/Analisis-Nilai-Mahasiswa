import pandas as pd
import os
import matplotlib.pyplot as plt

# Membaca data dari file CSV
file_umum = 'mahasiswa_data_umum.csv'
file_waktu_belajar_nilai = 'mahasiswa_data_waktu_belajar_nilai.csv'
file_faktor_tambahan = 'mahasiswa_data_faktor_tambahan.csv'

# Memeriksa keberadaan file
if not all(map(os.path.exists, [file_umum, file_waktu_belajar_nilai, file_faktor_tambahan])):
    print("File tidak ditemukan.")
    exit()

data_umum = pd.read_csv(file_umum)
data_waktu_belajar_nilai = pd.read_csv(file_waktu_belajar_nilai)
data_faktor_tambahan = pd.read_csv(file_faktor_tambahan)

# Menggabungkan data menjadi satu DataFrame
data = data_umum.merge(data_waktu_belajar_nilai, on='ID').merge(data_faktor_tambahan, on='ID')

# Mengurutkan data berdasarkan nilai secara menurun
data_sorted = data.sort_values(by='Nilai', ascending=False)

# Mengambil 10 nilai mahasiswa tertinggi
top_10_mahasiswa = data_sorted.head(10)

# Analisis faktor-faktor tambahan yang mempengaruhi nilai mahasiswa tertinggi
faktor_tambahan_columns = ['Motivasi (skala 1-10)', 'Kesehatan (skala 1-10)', 'Partisipasi Kelas (skala 1-10)', 'Dukungan Sosial (skala 1-10)']
avg_faktor_tambahan = top_10_mahasiswa[faktor_tambahan_columns].mean()

# Mencetak nilai mahasiswa tertinggi
print("10 Nilai Mahasiswa Tertinggi:")
print(top_10_mahasiswa)

# Mencetak rata-rata faktor tambahan untuk nilai mahasiswa tertinggi
print("\nRata-rata Faktor Tambahan untuk 10 Nilai Mahasiswa Tertinggi:")
print(avg_faktor_tambahan)

# Visualisasi kedua plot dalam satu jendela
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

# Histogram distribusi nilai
axes[0].hist(data_sorted['Nilai'], bins=10, color='skyblue', edgecolor='black')
axes[0].set_title('Distribusi Nilai Mahasiswa')
axes[0].set_xlabel('Nilai')
axes[0].set_ylabel('Frekuensi')
axes[0].grid(True)

# Bar chart rata-rata faktor tambahan
avg_faktor_tambahan.plot(kind='bar', ax=axes[1], color='lightgreen')
axes[1].set_title('Rata-rata Faktor Tambahan untuk 10 Nilai Mahasiswa Tertinggi')
axes[1].set_xlabel('Faktor Tambahan')
axes[1].set_ylabel('Rata-rata Skor')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y')

plt.tight_layout()
plt.show()
