import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

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

# Menampilkan data gabungan
print(data.head())

# Visualisasi hubungan antara Waktu Belajar dan Nilai
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Waktu Belajar (jam/minggu)', y='Nilai', hue='Motivasi (skala 1-10)', palette='viridis', size='Kesehatan (skala 1-10)', sizes=(20, 200))
plt.title('Hubungan Waktu Belajar dan Nilai dengan Motivasi dan Kesehatan')
plt.xlabel('Waktu Belajar (jam/minggu)')
plt.ylabel('Nilai')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

# Visualisasi hubungan antara Nilai dan Faktor Tambahan
plt.figure(figsize=(10, 6))
sns.heatmap(data[['Nilai', 'Motivasi (skala 1-10)', 'Kesehatan (skala 1-10)', 'Partisipasi Kelas (skala 1-10)', 'Dukungan Sosial (skala 1-10)']].corr(), annot=True, cmap='coolwarm')
plt.title('Korelasi Nilai dengan Faktor Tambahan')
plt.show()

# Analisis regresi linier sederhana untuk melihat pengaruh Waktu Belajar terhadap Nilai
from sklearn.linear_model import LinearRegression

# Menyiapkan data
X = data['Waktu Belajar (jam/minggu)'].values.reshape(-1, 1)
y = data['Nilai'].values

# Membuat model regresi linier
model = LinearRegression()
model.fit(X, y)

# Memprediksi nilai
y_pred = model.predict(X)

# Visualisasi regresi linier
plt.figure(figsize=(10, 6))
plt.scatter(data['Waktu Belajar (jam/minggu)'], data['Nilai'], color='blue', label='Data Aktual')
plt.plot(data['Waktu Belajar (jam/minggu)'], y_pred, color='red', label='Regresi Linier')
plt.title('Regresi Linier Waktu Belajar dan Nilai')
plt.xlabel('Waktu Belajar (jam/minggu)')
plt.ylabel('Nilai')
plt.legend()
plt.show()

# Menampilkan koefisien regresi
print(f'Koefisien regresi: {model.coef_[0]}')
print(f'Intercept: {model.intercept_}')
print(f'Skor R^2: {model.score(X, y)}')
