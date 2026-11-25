
# DOKUMEN RENCANA PENGUJIAN SISTEM (TEST PLAN)
## Berdasarkan Standar ISO/IEC/IEEE 29119-3:2021 & ISO/IEC 25010:2023

---

### Informasi Dokumen

| Parameter | Deskripsi |
| :--- | :--- |
| **Judul Proyek** | Analisis Kualitas dan Fungsionalitas Website Mutoh2000 Menggunakan Metode Black Box Testing Berdasarkan Standar ISO/IEC 25010:2023 |
| **Nama Aplikasi / Target** | Website Mutoh2000 |
| **URL Target** | https://mutoh2000.com/ |
| **Tim Penyusun (Kelompok)** | 1. Nama (NIM)<br>2. Nama (NIM)<br>3. Nama (NIM)<br>4. Nama (NIM) |
| **Mata Kuliah** | Testing & Quality Assurance (QA) - Semester 7 |
| **Program Studi / Kampus** | Teknik Informatika / Universitas Pamulang |
| **Versi Dokumen** | 1.0.0 |
| **Tanggal Terbit** | 25 November 2026 |
| **Standar Acuan** | ISO/IEC/IEEE 29119-3:2021 (Test Documentation) & ISO/IEC 25010:2023 (Product Quality Model) |

---

## 1. Pendahuluan (Introduction)

### 1.1 Latar Belakang & Deskripsi Sistem

Mutoh2000 merupakan website yang menyediakan informasi dan katalog produk perlengkapan kantor dan sekolah. Produk yang ditawarkan meliputi lemari arsip, brankas, locker, kursi kantor, meja kantor, meja kursi siswa, rak buku, serta berbagai perlengkapan lainnya.

Melalui website ini, pengguna dapat mencari produk, melihat kategori produk, mengetahui harga dan spesifikasi produk, serta memperoleh informasi mengenai perusahaan dan layanan yang tersedia.

Beberapa fitur yang tersedia pada website Mutoh2000 antara lain:

- **Homepage:** Menampilkan kategori produk, produk rekomendasi, promosi, dan informasi umum.
- **Katalog Produk (Shop):** Menampilkan daftar produk beserta gambar, nama, harga, dan informasi ketersediaan.
- **Pencarian Produk:** Memungkinkan pengguna mencari produk berdasarkan kata kunci.
- **Kategori dan Filter Produk:** Membantu pengguna menemukan produk berdasarkan kategori dan rentang harga.
- **Detail Produk:** Menampilkan informasi mengenai produk yang dipilih.
- **Wishlist dan Compare Product:** Memungkinkan pengguna menyimpan dan membandingkan produk.
- **Informasi Perusahaan dan Kontak:** Menyediakan informasi perusahaan serta akses untuk menghubungi pihak Mutoh2000.

Pengujian dilakukan untuk mengetahui apakah fitur-fitur tersebut dapat berjalan sesuai dengan fungsi yang diharapkan. Selain itu, pengujian juga dilakukan untuk mengidentifikasi kendala yang dapat memengaruhi pengalaman pengguna saat mengakses website.

### 1.2 Tujuan Pengujian (Test Objectives)

1. Memastikan fitur utama pada website Mutoh2000 dapat berjalan sesuai dengan fungsi yang diharapkan.
2. Memverifikasi fungsi pencarian, kategori, filter, dan pengurutan produk.
3. Memastikan informasi produk yang ditampilkan sesuai dengan produk yang dipilih.
4. Memverifikasi fungsi wishlist dan perbandingan produk.
5. Mengidentifikasi defect atau bug melalui pengujian dengan metode Black Box Testing.
6. Mengevaluasi kualitas website berdasarkan karakteristik yang relevan pada ISO/IEC 25010:2023.
7. Mengetahui kompatibilitas dan responsivitas website pada beberapa browser dan ukuran layar.
8. Melaksanakan pengujian melalui pendekatan Manual Testing dan Automated Testing.

---

## 2. Ruang Lingkup Pengujian (Test Scope)

### 2.1 Item Pengujian (Items to be Tested)

#### A. Homepage

URL: https://mutoh2000.com/

- Tampilan halaman utama website.
- Tampilan kategori produk.
- Tampilan produk rekomendasi dan promosi.
- Fungsi navigasi pada header dan footer.
- Fungsi tautan menuju kategori dan detail produk.

#### B. Katalog Produk (Shop)

URL: https://mutoh2000.com/shop/

- Tampilan daftar produk.
- Informasi nama, gambar, dan harga produk.
- Informasi ketersediaan produk.
- Fungsi pagination pada daftar produk.
- Pengurutan produk berdasarkan harga terendah dan tertinggi.
- Pengurutan produk berdasarkan opsi yang tersedia.

#### C. Pencarian Produk (Product Search)

- Pencarian menggunakan nama produk yang tersedia.
- Pencarian menggunakan sebagian nama produk.
- Pencarian menggunakan kata kunci yang tidak ditemukan.
- Pencarian dengan input kosong.
- Pencarian menggunakan angka dan karakter khusus.
- Kesesuaian hasil pencarian dengan kata kunci yang dimasukkan.

#### D. Kategori dan Filter Produk

- Pemilihan kategori produk.
- Pemilihan subkategori produk.
- Filter berdasarkan rentang harga.
- Kombinasi kategori dan filter harga.
- Kesesuaian produk yang ditampilkan dengan kategori yang dipilih.
- Pengujian kondisi ketika tidak terdapat produk yang sesuai dengan filter.

#### E. Detail Produk (Product Detail)

- Akses halaman detail melalui katalog produk.
- Tampilan nama dan gambar produk.
- Tampilan harga produk.
- Tampilan deskripsi dan spesifikasi produk.
- Informasi ketersediaan produk.
- Pemilihan variasi produk apabila tersedia.
- Konsistensi informasi antara katalog dan halaman detail produk.

#### F. Wishlist

- Menambahkan produk ke wishlist.
- Menghapus produk dari wishlist.
- Menambahkan lebih dari satu produk ke wishlist.
- Menambahkan produk yang sama secara berulang.
- Kesesuaian informasi produk yang tersimpan pada wishlist.

#### G. Compare Product

- Menambahkan produk ke daftar perbandingan.
- Membandingkan dua atau lebih produk.
- Menghapus produk dari daftar perbandingan.
- Kesesuaian informasi produk yang ditampilkan.
- Pengujian kondisi ketika daftar perbandingan kosong.

#### H. Informasi Perusahaan dan Kontak

Halaman yang menjadi target pengujian:

- Tentang Kami: https://mutoh2000.com/tentang-kami/
- Kontak Kami: https://mutoh2000.com/kontak-kami/
- Dokumentasi: https://mutoh2000.com/dokumentasi/
- Download: https://mutoh2000.com/download-2/

Item pengujian:

- Akses halaman informasi perusahaan.
- Tampilan informasi kontak.
- Fungsi tautan WhatsApp.
- Fungsi tautan media sosial.
- Fungsi tautan katalog atau dokumen yang tersedia.
- Tampilan dan validasi form kontak apabila tersedia, tanpa mengirimkan pesan ke pihak perusahaan.

#### I. Error Handling

- Akses halaman dengan URL yang tidak tersedia.
- Pencarian produk yang tidak ditemukan.
- Pemilihan filter yang tidak menghasilkan produk.
- Penanganan input yang tidak sesuai.
- Tampilan pesan ketika terjadi kesalahan.

#### J. Performance dan Responsivitas

- Waktu pemuatan halaman utama.
- Waktu pemuatan halaman katalog produk.
- Waktu pemuatan halaman detail produk.
- Responsivitas website pada perangkat desktop, tablet, dan smartphone.
- Konsistensi tampilan pada browser Google Chrome, Mozilla Firefox, dan Microsoft Edge.

### 2.2 Item yang Tidak Diuji (Out of Scope)

- Kode sumber aplikasi dan database internal.
- Halaman administrator dan pengelolaan produk.
- Proses autentikasi yang membutuhkan akun resmi.
- Proses checkout, pembayaran, dan transaksi pembelian secara nyata.
- Proses pengiriman dan pengelolaan pesanan.
- Pengiriman pesan melalui form kontak atau WhatsApp secara nyata.
- Penetration Testing dan pengujian keamanan secara aktif.
- Load Testing dan Stress Testing terhadap server produksi.
- Integrasi internal dengan sistem pihak ketiga.

Fitur yang tidak tersedia atau tidak dapat diakses selama pengujian akan dicatat sebagai Not Applicable (N/A) atau Blocked sesuai dengan kondisi yang ditemukan.

---

## 3. Strategi Pengujian (Test Strategy)

### 3.1 Metode Pengujian: Black Box Testing

Pengujian dilakukan menggunakan metode Black Box Testing, yaitu pengujian yang berfokus pada fungsi sistem berdasarkan input dan output tanpa melihat kode sumber aplikasi.

Teknik pengujian yang digunakan meliputi:

#### A. Equivalence Partitioning (EP)

Teknik ini digunakan untuk mengelompokkan data pengujian berdasarkan kondisi valid dan invalid.

Contoh pengujian:

- Pencarian menggunakan nama produk yang tersedia.
- Pencarian menggunakan nama produk yang tidak tersedia.
- Pemilihan kategori produk yang tersedia.
- Pemilihan rentang harga yang menghasilkan dan tidak menghasilkan produk.

#### B. Boundary Value Analysis (BVA)

Teknik ini digunakan untuk menguji nilai batas dari suatu input.

Contoh pengujian:

- Nilai minimum dan maksimum pada filter harga.
- Nilai tepat pada batas harga produk.
- Nilai di bawah dan di atas batas harga produk.
- Rentang harga dengan nilai minimum dan maksimum yang sama, apabila didukung oleh sistem.

Nilai batas pengujian ditentukan berdasarkan hasil observasi terhadap fitur yang tersedia.

#### C. Error Guessing

Teknik ini digunakan untuk mengidentifikasi kemungkinan kesalahan berdasarkan kondisi yang dapat terjadi saat pengguna menggunakan website.

Contoh pengujian:

- Melakukan pencarian dengan input kosong.
- Mengakses halaman produk yang tidak ditemukan.
- Menambahkan produk yang sama ke wishlist secara berulang.
- Membuka daftar perbandingan tanpa produk.
- Menggunakan kombinasi filter yang tidak menghasilkan produk.

#### D. Exploratory Testing

Pengujian dilakukan dengan mengeksplorasi fitur website untuk menemukan kendala yang belum tercakup dalam test case.

Pengujian dapat meliputi navigasi antarhalaman, konsistensi tampilan, perubahan ukuran layar, dan interaksi pengguna dengan komponen website.

### 3.2 Pendekatan Eksekusi

#### A. Manual Testing

Pengujian dilakukan secara langsung melalui browser dengan mengikuti test scenario dan test case yang telah disusun.

Aktivitas pengujian meliputi:

- Pengujian fungsi navigasi.
- Pengujian pencarian dan filter produk.
- Pengujian detail produk.
- Pengujian wishlist dan compare product.
- Pengujian tampilan dan responsivitas.
- Pencatatan actual result dan dokumentasi defect.

#### B. Automated Testing

Pengujian otomatis direncanakan menggunakan Playwright untuk membantu menjalankan test case yang bersifat berulang.

Pengujian otomatis difokuskan pada:

- Akses halaman website.
- Navigasi antarhalaman.
- Pencarian produk.
- Pemilihan kategori produk.
- Filter dan pengurutan produk.
- Validasi elemen pada halaman.
- Pengukuran waktu pemuatan halaman.

Automated Testing dilakukan secara terbatas dan tidak menggunakan eksekusi paralel dalam jumlah besar untuk menghindari gangguan terhadap website produksi.

### 3.3 Karakteristik Kualitas ISO/IEC 25010:2023

| Karakteristik | Fokus Pengujian |
| :--- | :--- |
| Functional Suitability | Kesesuaian fungsi pencarian, filter, kategori, wishlist, dan compare product. |
| Performance Efficiency | Waktu pemuatan halaman dan respons sistem terhadap interaksi pengguna. |
| Interaction Capability | Kemudahan navigasi, kejelasan informasi, dan interaksi pengguna dengan website. |
| Compatibility | Konsistensi fungsi dan tampilan pada beberapa browser. |
| Reliability | Konsistensi fungsi serta kemampuan sistem dalam menangani kondisi kesalahan. |
| Flexibility | Kemampuan website menyesuaikan tampilan pada berbagai ukuran layar. |
| Security | Pemeriksaan dasar penggunaan HTTPS tanpa melakukan pengujian keamanan secara aktif. |

Karakteristik yang dipilih disesuaikan dengan ruang lingkup dan keterbatasan akses pengujian. Maintainability dan Safety tidak menjadi fokus pengujian dalam studi kasus ini.

---

## 4. Kriteria Kelayakan (Pass / Fail Criteria)

### 4.1 Pass Criteria

Test case dinyatakan Pass apabila:

- Actual result sesuai dengan expected result.
- Halaman yang diuji dapat diakses dengan baik.
- Fitur pencarian menampilkan hasil yang sesuai dengan kata kunci.
- Filter dan kategori menampilkan produk yang sesuai.
- Informasi produk ditampilkan secara konsisten.
- Wishlist dan compare product berjalan sesuai dengan fungsi yang diharapkan.
- Sistem memberikan penanganan yang sesuai ketika data tidak ditemukan.
- Tampilan website dapat digunakan pada perangkat dan browser yang menjadi target pengujian.

### 4.2 Fail Criteria

Test case dinyatakan Fail apabila:

- Actual result tidak sesuai dengan expected result.
- Fitur yang tersedia tidak dapat digunakan sebagaimana mestinya.
- Hasil pencarian atau filter tidak sesuai dengan input pengguna.
- Terdapat informasi produk yang tidak konsisten.
- Tombol atau tautan tidak berfungsi.
- Terjadi kesalahan sistem pada alur penggunaan normal.
- Terdapat kendala tampilan yang menghambat penggunaan website.

### 4.3 Kriteria Performance

Sebagai target awal pengujian, waktu pemuatan halaman ditetapkan maksimal 3,5 detik berdasarkan kondisi jaringan dan perangkat yang digunakan.

Pengukuran dilakukan sebanyak tiga kali pada setiap halaman yang diuji. Hasil pengukuran dicatat beserta kondisi jaringan dan browser yang digunakan.

Target tersebut merupakan kriteria yang ditetapkan oleh tim penguji, bukan batas waktu yang diwajibkan oleh ISO/IEC 25010:2023.

### 4.4 Status Pengujian

| Status | Deskripsi |
| :--- | :--- |
| Pass | Actual result sesuai dengan expected result. |
| Fail | Actual result tidak sesuai dengan expected result. |
| Blocked | Pengujian tidak dapat dilanjutkan karena terdapat kendala atau ketergantungan. |
| Not Run | Test case belum dijalankan. |
| N/A | Test case tidak relevan atau fitur tidak tersedia. |

---

## 5. Lingkungan Pengujian (Test Environment)

| Parameter | Deskripsi |
| :--- | :--- |
| Environment | Production |
| Target URL | https://mutoh2000.com/ |
| Operating System | Windows 11 |
| Browser | Google Chrome, Microsoft Edge, Mozilla Firefox |
| Desktop Resolution | 1920 x 1080 |
| Tablet Resolution | 768 x 1024 |
| Mobile Resolution | 375 x 812 dan 414 x 896 |
| Manual Testing Tools | Web Browser dan Chrome DevTools |
| Automated Testing Tools | Playwright |
| Performance Testing Tools | Lighthouse dan Chrome DevTools |
| Test Documentation | GitHub |
| Defect Tracking | GitHub Issues |

---

## 6. Tahapan Pengujian (Test Process)

| No. | Tahapan | Aktivitas |
| :--- | :--- | :--- |
| 1 | System Analysis | Mempelajari website dan mengidentifikasi fitur yang tersedia. |
| 2 | Test Planning | Menentukan tujuan, ruang lingkup, metode, dan strategi pengujian. |
| 3 | Test Scenario Design | Menyusun skenario pengujian berdasarkan fitur website. |
| 4 | Test Case Design | Menyusun test case, test steps, test data, dan expected result. |
| 5 | Test Preparation | Menyiapkan perangkat, browser, tools, dan data pengujian. |
| 6 | Test Execution | Menjalankan pengujian manual dan otomatis. |
| 7 | Defect Reporting | Mencatat defect yang ditemukan selama pengujian. |
| 8 | Retesting | Melakukan pengujian ulang apabila terdapat perbaikan. |
| 9 | Test Reporting | Menyusun laporan hasil pengujian dan kesimpulan. |

---

## 7. Entry dan Exit Criteria

### 7.1 Entry Criteria

Pengujian dapat dimulai apabila:

- Website dapat diakses.
- Ruang lingkup pengujian telah ditentukan.
- Test scenario dan test case telah disusun.
- Perangkat dan tools pengujian telah disiapkan.
- Data pengujian telah tersedia.

### 7.2 Exit Criteria

Pengujian dapat dinyatakan selesai apabila:

- Seluruh test case dalam ruang lingkup telah dijalankan atau memiliki alasan yang terdokumentasi jika tidak dapat dijalankan.
- Seluruh hasil pengujian telah dicatat.
- Defect yang ditemukan telah didokumentasikan.
- Hasil pengujian manual dan otomatis telah dirangkum.
- Laporan hasil pengujian telah disusun.

Pengujian dapat dinyatakan selesai meskipun masih terdapat defect, karena tim penguji tidak memiliki akses untuk melakukan perbaikan terhadap website.

---

## 8. Risiko dan Mitigasi (Risk and Mitigation)

| No. | Risiko | Mitigasi |
| :--- | :--- | :--- |
| 1 | Website tidak dapat diakses selama pengujian. | Menjadwalkan ulang pengujian dan mencatat kondisi website. |
| 2 | Perubahan fitur atau tampilan website. | Menyesuaikan test case berdasarkan kondisi website terbaru. |
| 3 | Keterbatasan akses terhadap fitur tertentu. | Mencatat status Blocked atau N/A beserta alasannya. |
| 4 | Koneksi internet tidak stabil. | Mengulangi pengujian menggunakan koneksi yang stabil. |
| 5 | Pengujian mengganggu operasional website. | Membatasi jumlah request dan menghindari transaksi nyata. |
| 6 | Perubahan harga atau ketersediaan produk. | Memeriksa data produk sebelum menjalankan test case. |

---

## 9. Dokumen Hasil Pengujian (Test Deliverables)

Dokumen yang akan dihasilkan selama proses pengujian meliputi:

- [ ] Test Plan
- [ ] Test Scenario
- [ ] Test Case
- [ ] Test Data
- [ ] Manual Testing Result
- [ ] Automated Testing Script
- [ ] Automated Testing Result
- [ ] Defect Report
- [ ] Test Evidence (Screenshot atau Video)
- [ ] Test Summary Report

Seluruh dokumen dan hasil pengujian akan disimpan pada repository GitHub sebagai dokumentasi kegiatan pengujian.

---

## 10. Referensi

1. ISO/IEC/IEEE 29119-1:2022 - Software Testing: General Concepts  
   https://www.iso.org/standard/81291.html

2. ISO/IEC/IEEE 29119-2:2021 - Software Testing: Test Processes  
   https://www.iso.org/standard/79428.html

3. ISO/IEC/IEEE 29119-3:2021 - Software Testing: Test Documentation  
   https://www.iso.org/standard/79429.html

4. ISO/IEC/IEEE 29119-4:2021 - Software Testing: Test Techniques  
   https://www.iso.org/standard/79430.html

5. ISO/IEC 25010:2023 - Product Quality Model  
   https://www.iso.org/standard/78176.html

6. Website Mutoh2000  
   https://mutoh2000.com/

7. Playwright Documentation  
   https://playwright.dev/docs/intro
