# Projek Kriptografi

Aplikasi berbasis website untuk melakukan enkripsi dan dekripsi pesan dari file .txt. Aplikasi ini dibuat menggunakan Streamlit.  
Algoritma kriptografi yang digunakan adalah:  
1. [**Shift Cipher**](#Shift-Cipher)  
2. [**Spiral Cipher**](#Spiral-Cipher)  

## Shift Cipher
Shift Cipher adalah salah satu algoritma kriptografi klasik yang bekerja dengan cara menggantikan setiap huruf dalam teks dengan huruf lain yang terletak sejauh **kunci** tertentu dalam alfabet. Prosesnya adalah sebagai berikut:
- **Enkripsi**: Setiap huruf digeser maju sejauh kunci. Misalnya, dengan kunci 3, huruf "A" menjadi "D".
- **Dekripsi**: Setiap huruf digeser mundur sejauh kunci untuk mendapatkan teks asli.

### Contoh:
- Teks asli (plainteks): `HELLO`
- Kunci: `3`
- Hasil enkripsi: `KHOOR`
- Hasil dekripsi: `HELLO`

Kelebihan algoritma ini adalah sederhana dan cepat untuk diimplementasikan. Namun, karena hanya ada 26 kemungkinan kunci (untuk alfabet Latin), algoritma ini rentan terhadap serangan brute force.

## Spiral Cipher
Spiral Cipher adalah algoritma kriptografi yang bekerja dengan cara menulis teks dalam bentuk matriks berukuran tertentu (ditentukan oleh pengguna) dengan pola **spiral**. Proses enkripsi dan dekripsi adalah sebagai berikut:
- **Enkripsi**: 
  1. Tulis plainteks dalam matriks dengan pola spiral, dimulai dari sudut atas kiri dan bergerak ke dalam.
  2. Bacalah isi matriks **baris per baris** untuk mendapatkan cipherteks.
- **Dekripsi**: 
  1. Tulis cipherteks dalam matriks **baris per baris**.
  2. Bacalah matriks dalam pola spiral untuk mendapatkan plainteks asli.

### Contoh Enkripsi:
- Teks asli (plainteks): `testimoni`
- Ukuran matriks: `3x3`  
  Matriks setelah pengisian spiral:  
- Hasil enkripsi (dibaca baris per baris): `tesnitomi`

### Contoh Dekripsi:
- Cipherteks: `tesnitomi`
- Ukuran matriks: `3x3`  
Matriks setelah pengisian baris per baris:
- Hasil dekripsi (dibaca spiral): `testimoni`

## Daftar Isi
- [Anggota Kelompok](#anggota-kelompok)
- [Fungsi Aplikasi](#fungsi-aplikasi)
- [Fitur Utama](#fitur-utama)
- [Link Deployment](#link-deployment)

## Anggota Kelompok
| Nama                 | NPM          |
|:--------------------:|:------------:|
| Muhammad Faiz Fahri  | 140810220002 | 
| Mohammad Aria Ardhana | 140810220041 | 
| Muhammad Satria Dharma | 140810220080 | 

## Fungsi Aplikasi
Fungsi dari aplikasi ini adalah untuk memudahkan pengguna dalam melakukan enkripsi atau dekripsi teks, terutama untuk teks yang panjang, menggunakan file .txt. Aplikasi ini juga memungkinkan pengguna memilih di antara dua metode cipher, yaitu **Shift Cipher** dan **Spiral Cipher**.

Fungsi-fungsi aplikasi ini mencakup:
- Membantu pengguna mengenkripsi pesan sensitif untuk menjaga kerahasiaan.
- Memudahkan pengguna mendekripsi pesan untuk membaca teks asli yang terenkripsi.
- Mendukung pengolahan teks panjang dengan file `.txt` untuk efisiensi.
- Menyediakan opsi input manual atau melalui file untuk fleksibilitas penggunaan.
- Menghasilkan file hasil proses enkripsi/dekripsi yang dapat diunduh untuk penyimpanan lokal.

## Fitur Utama
- **Shift Cipher**:
- Enkripsi dan dekripsi teks melalui input manual.
- Enkripsi dan dekripsi teks menggunakan file `.txt`.
- Mendukung pengaturan kunci shift oleh pengguna.

- **Spiral Cipher**:
- Enkripsi dan dekripsi teks melalui input manual.
- Enkripsi dan dekripsi teks menggunakan file `.txt`.
- Mendukung pengaturan dimensi matriks (baris dan kolom) untuk proses enkripsi.

- **General Features**:
- Mendukung pengunggahan file `.txt` sebagai sumber teks.
- Menyediakan opsi untuk memproses file berisi teks panjang.
- Menghasilkan file `.txt` hasil enkripsi atau dekripsi yang dapat diunduh.
- Menampilkan hasil enkripsi atau dekripsi langsung di antarmuka.

## Link Deployment
[Aplikasi enkripsi dan dekripsi dari file .txt](https://uas-kripto-kelompok-11.streamlit.app)
