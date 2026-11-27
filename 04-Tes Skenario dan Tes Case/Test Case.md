# Test Case - Mutoh2000

## 1. Informasi Pengujian

| Parameter | Deskripsi |
| :--- | :--- |
| Nama Sistem | Mutoh2000 |
| URL | https://mutoh2000.com/ |
| Metode | Black Box Testing |
| Environment | Production |
| Total Test Case | 40 |
| Status | Ready for Review |

## 2. Precondition

- Perangkat terhubung dengan internet.
- Browser dapat digunakan dengan normal.
- Website Mutoh2000 dapat diakses.
- Data produk yang digunakan tersedia pada website, kecuali untuk pengujian data invalid.
- Pengujian dilakukan tanpa transaksi pembelian secara nyata.

## 3. Daftar Test Case

### 3.1 Homepage & Navigation

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-001 | TS-001 | Mengakses halaman utama website. | Buka browser dan akses https://mutoh2000.com/. | Halaman utama berhasil ditampilkan tanpa error. | Positive |
| TC-002 | TS-001 | Memeriksa tampilan homepage. | Periksa banner, gambar, kategori, dan informasi produk. | Komponen utama ditampilkan dengan baik. | Positive |
| TC-003 | TS-002 | Mengakses menu utama. | Klik setiap menu utama pada header. | Pengguna diarahkan ke halaman yang sesuai. | Positive |
| TC-004 | TS-002 | Mengakses submenu. | Buka menu yang memiliki submenu dan pilih salah satu submenu. | Halaman sesuai submenu berhasil ditampilkan. | Positive |
| TC-005 | TS-003 | Mengakses tautan pada header dan footer. | Klik tautan internal yang tersedia pada header dan footer. | Seluruh tautan mengarah ke halaman yang sesuai. | Positive |

### 3.2 Product Catalog

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-006 | TS-004 | Mengakses katalog produk. | Buka halaman Shop. | Daftar produk berhasil ditampilkan. | Positive |
| TC-007 | TS-004 | Memeriksa informasi pada katalog. | Periksa nama, gambar, dan harga produk. | Informasi produk ditampilkan sesuai dengan data yang tersedia. | Positive |
| TC-008 | TS-005 | Menggunakan pagination. | Buka katalog, klik halaman berikutnya, kemudian kembali ke halaman sebelumnya. | Daftar produk berubah sesuai halaman yang dipilih. | Positive |

### 3.3 Product Search

| Test Case ID | Scenario ID | Test Case | Test Steps | Test Data | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-009 | TS-007 | Pencarian dengan kata kunci yang tidak tersedia. | Masukkan kata kunci dan jalankan pencarian. | xyz123abc | Sistem menampilkan informasi bahwa produk tidak ditemukan tanpa error. | Negative |
| TC-010 | TS-007 | Pencarian dengan input kosong. | Kosongkan kolom pencarian dan jalankan pencarian. | Empty | Sistem menangani input kosong tanpa error. | Negative |
| TC-011 | TS-007 | Pencarian menggunakan karakter khusus. | Masukkan karakter khusus dan jalankan pencarian. | @#$% | Sistem menangani input tanpa mengalami error. | Negative |
| TC-012 | TS-006 | Pencarian menggunakan nama produk valid. | Masukkan nama produk dan jalankan pencarian. | Lemari | Produk yang relevan dengan kata kunci ditampilkan. | Positive |
| TC-013 | TS-006 | Pencarian menggunakan sebagian nama produk. | Masukkan sebagian nama produk dan jalankan pencarian. | Lem | Produk yang memiliki kata kunci terkait ditampilkan. | Positive |

### 3.4 Product Category

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-014 | TS-008 | Memilih kategori produk. | Buka daftar kategori dan pilih salah satu kategori. | Produk ditampilkan sesuai kategori yang dipilih. | Positive |
| TC-015 | TS-008 | Memilih subkategori produk. | Buka kategori yang memiliki subkategori dan pilih salah satunya. | Produk ditampilkan sesuai subkategori yang dipilih. | Positive |
| TC-016 | TS-008 | Berpindah kategori produk. | Pilih satu kategori, kemudian pindah ke kategori lainnya. | Daftar produk diperbarui sesuai kategori terakhir yang dipilih. | Positive |

### 3.5 Filter & Sorting

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-017 | TS-009 | Filter harga yang tidak menghasilkan produk. | Pilih rentang harga yang tidak memiliki produk. | Sistem menampilkan kondisi produk tidak ditemukan tanpa error. | Negative |
| TC-018 | TS-009 | Filter menggunakan rentang harga valid. | Tentukan harga minimum dan maksimum, kemudian terapkan filter. | Produk ditampilkan sesuai rentang harga. | Positive |
| TC-019 | TS-009 | Filter menggunakan nilai batas harga. | Gunakan harga salah satu produk sebagai batas minimum atau maksimum. | Produk pada batas harga ditampilkan sesuai aturan filter. | Positive |
| TC-020 | TS-010 | Mengurutkan harga dari terendah. | Pilih opsi pengurutan harga terendah ke tertinggi. | Produk diurutkan dari harga terendah ke tertinggi. | Positive |
| TC-021 | TS-010 | Mengurutkan harga dari tertinggi. | Pilih opsi pengurutan harga tertinggi ke terendah. | Produk diurutkan dari harga tertinggi ke terendah. | Positive |

### 3.6 Product Detail

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-022 | TS-011 | Mengakses detail produk. | Pilih salah satu produk dari katalog. | Halaman detail produk berhasil ditampilkan. | Positive |
| TC-023 | TS-011 | Memeriksa kesesuaian informasi produk. | Bandingkan nama, gambar, dan harga pada katalog dengan halaman detail. | Informasi produk ditampilkan secara konsisten. | Positive |
| TC-024 | TS-012 | Memeriksa galeri gambar produk. | Buka produk yang memiliki beberapa gambar dan pilih gambar lainnya. | Gambar produk berhasil ditampilkan. | Positive |
| TC-025 | TS-012 | Memilih variasi produk. | Buka produk yang memiliki variasi dan pilih salah satu variasi. | Informasi produk diperbarui sesuai variasi yang dipilih. | Positive |

### 3.7 Wishlist

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-026 | TS-013 | Menambahkan produk yang sama secara berulang. | Tambahkan satu produk ke wishlist, kemudian ulangi tindakan pada produk yang sama. | Sistem menangani penambahan berulang tanpa error atau duplikasi yang tidak semestinya. | Negative |
| TC-027 | TS-013 | Menambahkan produk ke wishlist. | Pilih produk, klik tombol wishlist, kemudian buka daftar wishlist. | Produk berhasil ditambahkan ke wishlist. | Positive |
| TC-028 | TS-013 | Menghapus produk dari wishlist. | Buka wishlist dan hapus salah satu produk. | Produk berhasil dihapus dari wishlist. | Positive |

### 3.8 Compare Product

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-029 | TS-014 | Membuka daftar perbandingan kosong. | Pastikan tidak ada produk dalam daftar, kemudian buka halaman compare. | Sistem menampilkan kondisi daftar kosong tanpa error. | Negative |
| TC-030 | TS-014 | Membandingkan dua produk. | Tambahkan dua produk berbeda dan buka daftar perbandingan. | Informasi kedua produk ditampilkan untuk dibandingkan. | Positive |
| TC-031 | TS-014 | Menghapus produk dari daftar perbandingan. | Buka daftar perbandingan dan hapus salah satu produk. | Produk berhasil dihapus dari daftar perbandingan. | Positive |

### 3.9 Language, Company Information & Contact

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-032 | TS-015 | Mengubah bahasa website. | Pilih bahasa Inggris, kemudian kembali ke bahasa Indonesia. | Konten yang mendukung perubahan bahasa ditampilkan sesuai pilihan. | Positive |
| TC-033 | TS-016 | Mengakses halaman informasi perusahaan. | Klik menu Tentang Kami. | Informasi perusahaan berhasil ditampilkan. | Positive |
| TC-034 | TS-017 | Mengakses halaman kontak. | Klik menu Kontak Kami. | Informasi kontak perusahaan berhasil ditampilkan. | Positive |
| TC-035 | TS-017 | Mengakses tautan WhatsApp. | Klik tombol WhatsApp tanpa mengirim pesan. | Pengguna diarahkan ke kontak WhatsApp yang sesuai. | Positive |

### 3.10 Error Handling

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-036 | TS-018 | Mengakses URL yang tidak tersedia. | Akses https://mutoh2000.com/halaman-tidak-ditemukan-xyz/. | Sistem menampilkan halaman 404 atau informasi bahwa halaman tidak tersedia tanpa internal server error. | Negative |

### 3.11 Non-Functional Testing

| Test Case ID | Scenario ID | Test Case | Test Steps | Expected Result | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-037 | TS-019 | Menguji responsivitas website. | Buka homepage dan katalog pada resolusi desktop, tablet, dan smartphone menggunakan DevTools. | Konten dapat ditampilkan dan fitur utama tetap dapat digunakan pada setiap resolusi. | Non-Functional |
| TC-038 | TS-020 | Menguji kompatibilitas browser. | Jalankan navigasi, pencarian, dan akses detail produk pada Chrome, Edge, dan Firefox. | Fitur utama berjalan dengan baik pada setiap browser. | Non-Functional |
| TC-039 | TS-021 | Mengukur waktu pemuatan halaman. | Ukur waktu loading homepage, katalog, dan detail produk menggunakan DevTools sebanyak tiga kali per halaman. | Rata-rata waktu pemuatan setiap halaman maksimal 3,5 detik. | Non-Functional |
| TC-040 | TS-022 | Memeriksa penggunaan HTTPS. | Akses website dan periksa informasi koneksi serta sertifikat melalui browser. | Website menggunakan HTTPS dengan sertifikat yang valid. | Non-Functional |

## 4. Ringkasan Test Case

| Type | Jumlah |
| :--- | ---: |
| Positive | 29 |
| Negative | 7 |
| Non-Functional | 4 |
| **Total** | **40** |

## 5. Catatan Pengujian

- Test case disusun berdasarkan fitur yang telah diidentifikasi pada System Inventory.
- Test data dapat disesuaikan dengan kondisi produk yang tersedia saat pengujian.
- Jika fitur tidak tersedia, test case dicatat sebagai N/A.
- Jika terdapat kendala yang menyebabkan pengujian tidak dapat dilanjutkan, test case dicatat sebagai Blocked.
- Actual result, status pengujian, dan evidence akan dicatat pada dokumen hasil pengujian.
- Pengujian dilakukan tanpa mengganggu operasional website.

## 6. Referensi

- System Inventory
- Test Plan
- Test Scenario
- Quality Metrics
- ISO/IEC/IEEE 29119-3:2021
- ISO/IEC/IEEE 29119-4:2021
- ISO/IEC 25010:2023
