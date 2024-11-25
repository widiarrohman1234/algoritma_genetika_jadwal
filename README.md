# Algoritma Genetika untuk Penjadwalan Belajar

Algoritma genetika ini dirancang untuk menghasilkan jadwal belajar yang optimal. Penjadwalan mempertimbangkan parameter seperti hari, ruang, mata pelajaran, dosen, dan waktu. Tujuannya adalah meminimalkan konflik seperti bentrokan jadwal dosen, waktu kelas, atau ruang.

---

## Data Konfigurasi

Berikut adalah parameter yang digunakan dalam penjadwalan:

- **Hari (HARI):**
['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
- **Mata Pelajaran (PELAJARAN):** 
['Metodologi Riset dan Penulisan Ilmiah', 'Komunikasi dan Jaringan Komputer', 'Kecerdasan Buatan', 'Pembelajaran dan Perhitungan Evolusioner', 'Praktikum Pembelajaran dan Perhitungan Evolusioner', 'Sinyal dan Sistem']
- **Dosen (DOSEN):**
['Firman Arifin', 'Iwan Syarif', 'Aliridho Barakbah', 'Riyanto Sigit', 'Tri Budi Santoso']
- **Waktu (WAKTU):**
['08:00 sd 09:40', '09:40 sd 10:30', '10:30 sd 12:10', '13:10 sd 15:40', '15:40 sd 16:30']
- **Ruang Kelas (KELAS):**
['PS-03.17', 'PS-08.07']

---

## Hasil Jadwal

Berikut adalah beberapa jadwal yang dihasilkan oleh algoritma genetika:

| Dosen             | Kelas     | Mata Pelajaran                                         | Waktu           | Hari    |
|--------------------|-----------|-------------------------------------------------------|-----------------|---------|
| Iwan Syarif        | PS-08.07  | Kecerdasan Buatan                                     | 08:00 sd 09:40  | Jumat   |
| Firman Arifin      | PS-08.07  | Kecerdasan Buatan                                     | 09:40 sd 10:30  | Kamis   |
| Tri Budi Santoso   | PS-03.17  | Kecerdasan Buatan                                     | 10:30 sd 12:10  | Kamis   |
| Aliridho Barakbah  | PS-08.07  | Komunikasi dan Jaringan Komputer                      | 13:10 sd 15:40  | Kamis   |
| Firman Arifin      | PS-08.07  | Pembelajaran dan Perhitungan Evolusioner             | 08:00 sd 09:40  | Rabu    |
| Riyanto Sigit      | PS-08.07  | Pembelajaran dan Perhitungan Evolusioner             | 09:40 sd 10:30  | Rabu    |
| Riyanto Sigit      | PS-03.17  | Kecerdasan Buatan                                     | 08:00 sd 09:40  | Selasa  |
| Riyanto Sigit      | PS-03.17  | Metodologi Riset dan Penulisan Ilmiah                | 09:40 sd 10:30  | Selasa  |
| Firman Arifin      | PS-08.07  | Praktikum Pembelajaran dan Perhitungan Evolusioner   | 13:10 sd 15:40  | Selasa  |
| Firman Arifin      | PS-03.17  | Sinyal dan Sistem                                    | 15:40 sd 16:30  | Selasa  |
| Riyanto Sigit      | PS-03.17  | Metodologi Riset dan Penulisan Ilmiah                | 08:00 sd 09:40  | Senin   |
| Aliridho Barakbah  | PS-03.17  | Kecerdasan Buatan                                     | 10:30 sd 12:10  | Senin   |

---

## Proses Algoritma Genetika

1. **Inisialisasi Populasi:**
 - Populasi awal terdiri dari sejumlah individu (jadwal lengkap) yang dibuat secara acak.
2. **Evaluasi Fitness:**
 - Fitness function mengevaluasi konflik pada jadwal, seperti:
   - Dosen mengajar di lebih dari satu kelas pada waktu yang sama.
   - Kelas memiliki lebih dari satu mata pelajaran di waktu yang sama.
   - Dua kelas menggunakan ruang yang sama pada waktu yang sama.
3. **Seleksi:**
 - Individu dengan fitness terbaik (sedikit konflik) dipilih untuk menghasilkan generasi berikutnya.
4. **Crossover dan Mutasi:**
 - Crossover menggabungkan dua individu untuk menghasilkan individu baru.
 - Mutasi dilakukan secara acak untuk menjaga keragaman populasi.
5. **Iterasi:**
 - Proses diulang hingga mencapai generasi maksimum atau nilai fitness optimal (tanpa konflik).

---

## Kontribusi dan Perbaikan

- Anda dapat menyesuaikan jumlah populasi, generasi maksimum, dan tingkat mutasi untuk hasil yang lebih baik.
- Penjadwalan dapat ditambahkan parameter tambahan, seperti batas waktu pengajaran untuk dosen atau prioritas mata pelajaran tertentu.

---

## Lisensi

Proyek ini bebas digunakan untuk keperluan akademik atau eksperimen. Mohon sertakan atribusi jika menggunakan atau memodifikasi algoritma ini.

## Kontak
email: widiarrohman1234@gmail.com

