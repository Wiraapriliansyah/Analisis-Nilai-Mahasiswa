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
ID,Nama,Jurusan,Semester
1,Budi,Teknik Informatika,4
2,Siti,Manajemen,3
3,Andi,Akuntansi,5
4,Rina,Psikologi,2
5,Yanto,Teknik Elektro,6
6,Dinda,Hukum,7
7,Rudi,Kedokteran,8
8,Wati,Ilmu Komunikasi,1
9,Bambang,Teknik Mesin,4
10,Nurul,Sastra Inggris,3
11,Agus,Teknik Sipil,2
12,Fitri,Manajemen,6
13,Hendri,Teknik Industri,7
14,Lestari,Psikologi,5
15,Sari,Akuntansi,3
16,Johan,Teknik Informatika,8
17,Mega,Hukum,4
18,Arif,Kedokteran,2
19,Dian,Sastra Jepang,6
20,Indra,Teknik Mesin,7
21,Ayu,Ilmu Komunikasi,1
22,Riko,Teknik Elektro,4
23,Lina,Manajemen,5
24,Bayu,Psikologi,3
25,Tono,Teknik Sipil,2
26,Riska,Akuntansi,6
27,Rahman,Teknik Industri,8
28,Anita,Hukum,7
29,Fahmi,Kedokteran,4
30,Nia,Sastra Inggris,5
31,Ari,Teknik Informatika,6
32,Dwi,Manajemen,3
33,Widya,Psikologi,8
34,Andika,Akuntansi,4
35,Ririn,Teknik Elektro,7
36,Farid,Teknik Sipil,2
37,Galuh,Ilmu Komunikasi,1
38,Syahrul,Teknik Industri,5
39,Rendy,Hukum,6
40,Maya,Sastra Jepang,7
41,Rika,Manajemen,4
42,Gita,Psikologi,5
43,Nanda,Akuntansi,2
44,Fajar,Kedokteran,3
45,Tini,Teknik Informatika,6
46,Doni,Teknik Elektro,7
47,Yuli,Teknik Sipil,8
48,Asep,Ilmu Komunikasi,4
49,Ratna,Sastra Inggris,5
50,Ahmad,Manajemen,2
![image](https://github.com/Wiraapriliansyah/Analisis-Nilai-Mahasiswa/assets/152155184/819ffc68-06a9-4369-bffb-3c2fbfa457b0)

- `mahasiswa_data_waktu_belajar_nilai.csv`
  ID,Waktu Belajar (jam/minggu),Nilai
1,10,68
2,15,78
3,20,82
4,25,88
5,30,89
6,35,91
7,40,93
8,45,94
9,50,95
10,5,60
11,8,62
12,12,70
13,18,74
14,22,79
15,28,87
16,32,90
17,37,92
18,41,93
19,45,94
20,50,95
21,7,64
22,13,71
23,17,73
24,21,77
25,27,86
26,33,91
27,36,92
28,42,94
29,46,95
30,4,58
31,9,65
32,14,72
33,19,75
34,23,80
35,26,84
36,31,90
37,38,92
38,43,94
39,47,95
40,6,61
41,11,69
42,16,76
43,24,81
44,29,88
45,34,91
46,39,92
47,44,94
48,48,95
49,3,57
50,5,63
![image](https://github.com/Wiraapriliansyah/Analisis-Nilai-Mahasiswa/assets/152155184/023fb1eb-32d8-4254-a533-47d1068083bc)

- `mahasiswa_data_faktor_tambahan.csv`
  ID,Motivasi (skala 1-10),Kesehatan (skala 1-10),Partisipasi Kelas (skala 1-10),Dukungan Sosial (skala 1-10)
1,7,8,6,7
2,8,7,7,8
3,9,8,8,6
4,9,9,9,8
5,8,8,8,9
6,9,9,9,8
7,10,10,10,9
8,8,9,8,7
9,10,9,9,10
10,6,7,5,6
11,7,8,6,7
12,8,7,7,8
13,9,8,8,6
14,9,9,9,8
15,8,8,8,9
16,9,9,9,8
17,10,10,10,9
18,8,9,8,7
19,10,9,9,10
20,10,9,9,10
21,7,8,6,7
22,8,7,7,8
23,9,8,8,6
24,9,9,9,8
25,8,8,8,9
26,9,9,9,8
27,10,10,10,9
28,8,9,8,7
29,10,9,9,10
30,6,7,5,6
31,7,8,6,7
32,8,7,7,8
33,9,8,8,6
34,9,9,9,8
35,8,8,8,9
36,9,9,9,8
37,10,10,10,9
38,8,9,8,7
39,10,9,9,10
40,7,8,6,7
41,8,7,7,8
42,9,8,8,6
43,9,9,9,8
44,8,8,8,9
45,9,9,9,8
46,10,10,10,9
47,8,9,8,7
48,10,9,9,10
49,6,7,5,6
50,7,8,6,7
![image](https://github.com/Wiraapriliansyah/Analisis-Nilai-Mahasiswa/assets/152155184/066fd5e8-15e0-4a16-addd-017f07bbac3d)
  

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

![Figure_1](https://github.com/Wiraapriliansyah/Analisis-Nilai-Mahasiswa/assets/152155184/3372cfd0-3aab-46a6-b1d3-262245c0b480)

![Figure_2](https://github.com/Wiraapriliansyah/Analisis-Nilai-Mahasiswa/assets/152155184/f5f48f2e-8b59-42fa-9d3a-c106121ae9c3)

![Figure_3](https://github.com/Wiraapriliansyah/Analisis-Nilai-Mahasiswa/assets/152155184/737d9b92-6af8-4c73-856b-e172742a8842)

![Figure_4](https://github.com/Wiraapriliansyah/Analisis-Nilai-Mahasiswa/assets/152155184/45e0afe7-2d13-4562-a80b-287fed5d1b7e)




