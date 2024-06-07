# Analisis Nilai Mahasiswa

## Deskripsi
Proyek ini bertujuan untuk menganalisis faktor-faktor yang mempengaruhi nilai mahasiswa. Data yang digunakan mencakup informasi umum mahasiswa, waktu belajar dan nilai, serta faktor tambahan seperti motivasi, kesehatan, partisipasi kelas, dan dukungan sosial.

## Langkah-Langkah

### Prasyarat
Pastikan Anda telah menginstal Python dan pustaka berikut:
- pandas
- matplotlib

Anda dapat menginstal pustaka tersebut menggunakan pip:
```bash
pip install pandas matplotlib
```

### File yang Dibutuhkan
- `mahasiswa_data_umum.csv`
- `mahasiswa_data_waktu_belajar_nilai.csv`
- `mahasiswa_data_faktor_tambahan.csv`

### Menjalankan Kode
1. Pastikan semua file CSV berada di direktori yang sama dengan script Python `analisis_nilai_tertinggi.py`.
2. Jalankan script Python dengan perintah berikut di terminal:
    ```bash
    python analisis_nilai_tertinggi.py
    ```

### Penjelasan Kode
Kode akan melakukan langkah-langkah berikut:
1. Membaca data dari tiga file CSV.
2. Menggabungkan data menjadi satu DataFrame.
3. Menghapus kolom non-numerik yang tidak relevan untuk analisis korelasi.
4. Menghitung korelasi antara nilai mahasiswa dengan faktor tambahan.
5. Menampilkan korelasi dalam bentuk bar chart.
6. Menentukan faktor yang paling mempengaruhi nilai mahasiswa.

### Pertanyaan dan Jawaban

#### Pertanyaan 1
**Bagaimana cara memuat dan menggabungkan data dari beberapa file CSV?**
Jawaban:
Data dimuat menggunakan `pd.read_csv()` dan digabungkan menggunakan `merge()`. Contohnya:
```python
data_umum = pd.read_csv('mahasiswa_data_umum.csv')
data_waktu_belajar_nilai = pd.read_csv('mahasiswa_data_waktu_belajar_nilai.csv')
data_faktor_tambahan = pd.read_csv('mahasiswa_data_faktor_tambahan.csv')
data = data_umum.merge(data_waktu_belajar_nilai, on='ID').merge(data_faktor_tambahan, on='ID')
```

#### Pertanyaan 2
**Bagaimana cara menghapus kolom non-numerik dari DataFrame?**
Jawaban:
Kolom non-numerik dihapus menggunakan `drop()`. Contohnya:
```python
data_numerik = data.drop(columns=['ID', 'Nama', 'Jurusan'])
```

#### Pertanyaan 3
**Bagaimana cara menghitung korelasi antara nilai mahasiswa dengan faktor tambahan?**
Jawaban:
Korelasi dihitung menggunakan `corr()` dari pandas. Contohnya:
```python
correlation = data_numerik.corr()['Nilai'][['Motivasi (skala 1-10)', 'Kesehatan (skala 1-10)', 'Partisipasi Kelas (skala 1-10)', 'Dukungan Sosial (skala 1-10)']]
```

#### Pertanyaan 4
**Bagaimana cara memvisualisasikan korelasi dalam bentuk bar chart?**
Jawaban:
Korelasi divisualisasikan menggunakan `plot()` dari matplotlib. Contohnya:
```python
plt.figure(figsize=(10, 6))
correlation.plot(kind='bar', color='lightblue')
plt.title('Korelasi Antara Nilai Mahasiswa dengan Faktor Tambahan')
plt.xlabel('Faktor Tambahan')
plt.ylabel('Korelasi')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
```

#### Pertanyaan 5
**Faktor apa yang paling mempengaruhi nilai mahasiswa berdasarkan analisis korelasi?**
Jawaban:
Faktor dengan korelasi tertinggi ditentukan menggunakan `idxmax()`. Contohnya:
```python
max_correlation_factor = correlation.idxmax()
print(f"Faktor yang paling mempengaruhi nilai mahasiswa adalah: {max_correlation_factor}")
```

## Hasil
Faktor yang paling mempengaruhi nilai mahasiswa akan ditampilkan di terminal setelah menjalankan script.
```
