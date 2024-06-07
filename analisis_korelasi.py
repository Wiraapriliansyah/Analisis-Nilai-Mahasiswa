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

# Menghapus kolom non-numerik
data_numerik = data.drop(columns=['ID', 'Nama', 'Jurusan'])

# Menghitung korelasi antara nilai mahasiswa dengan faktor tambahan
correlation = data_numerik.corr()['Nilai'][['Motivasi (skala 1-10)', 'Kesehatan (skala 1-10)', 'Partisipasi Kelas (skala 1-10)', 'Dukungan Sosial (skala 1-10)']]

# Visualisasi korelasi dalam bentuk bar chart
plt.figure(figsize=(10, 6))
correlation.plot(kind='bar', color='lightblue')
plt.title('Korelasi Antara Nilai Mahasiswa dengan Faktor Tambahan')
plt.xlabel('Faktor Tambahan')
plt.ylabel('Korelasi')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Faktor dengan korelasi tertinggi
max_correlation_factor = correlation.idxmax()
print(f"Faktor yang paling mempengaruhi nilai mahasiswa adalah: {max_correlation_factor}")
