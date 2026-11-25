
# Analisis Pengujian Website Mutoh2000

![Version](https://img.shields.io/badge/Version-2.2.0-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Method](https://img.shields.io/badge/Method-Black%20Box%20Testing-green)

## 1. Informasi Proyek

| Parameter | Deskripsi |
| :--- | :--- |
| Judul Proyek | Analisis Kualitas dan Fungsionalitas Website Mutoh2000 Menggunakan Metode Black Box Testing Berdasarkan Standar ISO/IEC 25010:2023 |
| Objek Pengujian | Website Mutoh2000 |
| URL | https://mutoh2000.com/ |
| Mata Kuliah | Testing & Quality Assurance (QA) |
| Program Studi | Teknik Informatika |
| Universitas | Universitas Pamulang |
| Semester | 7 |
| Versi | 2.2.0 |
| Tanggal Penyusunan | 21 November 2026 |
| Terakhir Diperbarui | 25 November 2026 |
| Status | In Progress |

## 2. Anggota Kelompok

| No. | Nama | NIM |
| :--- | :--- | :--- |
| 1 | Ariel Modjo Satriawan | 231011403476 |
| 2 | Azacky Habibilah Syahlan | 231011402531 |
| 3 | Artha Mauludani | 231011401756 |
| 4 | Akhmad Maulana Fadil | 231011401337 |

## 3. Deskripsi Proyek

Mutoh2000 merupakan website katalog produk perlengkapan kantor dan sekolah yang menyediakan berbagai fitur, seperti pencarian produk, kategori, filter harga, detail produk, wishlist, dan compare product.

Pengujian dilakukan menggunakan metode Black Box Testing dengan mengacu pada standar ISO/IEC/IEEE 29119 dan ISO/IEC 25010:2023 untuk mengetahui kualitas website, kesesuaian fungsi, serta kendala yang ditemukan selama pengujian.

## 4. Tujuan Pengujian

- Memastikan fitur website berjalan sesuai dengan fungsi yang diharapkan.
- Mengidentifikasi bug atau defect pada website.
- Mengevaluasi kualitas website berdasarkan ISO/IEC 25010:2023.
- Melaksanakan pengujian manual dan otomatis.
- Memberikan rekomendasi perbaikan berdasarkan hasil pengujian.

## 5. Standar Acuan

| Standar | Keterangan |
| :--- | :--- |
| ISO/IEC/IEEE 29119-1:2022 | General Concepts |
| ISO/IEC/IEEE 29119-2:2021 | Test Processes |
| ISO/IEC/IEEE 29119-3:2021 | Test Documentation |
| ISO/IEC/IEEE 29119-4:2021 | Test Techniques |
| ISO/IEC 25010:2023 | Product Quality Model |

Referensi standar ISO dan jurnal pendukung tersedia pada folder `01-Referensi`.

## 6. Metode dan Tools Pengujian

### Metode Pengujian

- Black Box Testing
- Equivalence Partitioning
- Boundary Value Analysis
- Error Guessing
- Exploratory Testing

### Tools Pengujian

| Tools | Kegunaan |
| :--- | :--- |
| Web Browser | Manual Testing |
| Chrome DevTools | Pemeriksaan tampilan dan responsivitas |
| Playwright | Automated Testing |
| Lighthouse | Performance Testing |
| GitHub | Dokumentasi pengujian |
| GitHub Issues | Defect Tracking |

## 7. Ruang Lingkup Pengujian

Pengujian mencakup beberapa fitur dan aspek berikut:

- Homepage dan navigasi
- Katalog produk
- Pencarian produk
- Kategori dan subkategori
- Filter dan pengurutan produk
- Detail produk
- Wishlist
- Compare Product
- Perubahan bahasa
- Informasi perusahaan dan kontak
- Error Handling
- Responsivitas dan kompatibilitas browser
- Performance
- Pemeriksaan dasar HTTPS

Pengujian terbatas pada fitur yang dapat diakses secara publik, tanpa akses administrator, kode sumber, maupun database. Pengujian tidak mencakup transaksi nyata atau aktivitas yang dapat mengganggu operasional website.

## 8. Timeline dan Progress Pengerjaan

| No. | Tahapan | PIC | Target Mulai | Target Selesai | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01 | Referensi ISO dan Jurnal | Azacky Habibilah Syahlan | 16 Nov 2026 | 22 Nov 2026 | Completed |
| 02 | Analisis Sistem | Artha Mauludani | 16 Nov 2026 | 22 Nov 2026 | Completed |
| 03 | Dokumen Pengujian | Ariel Modjo Satriawan | 21 Nov 2026 | 25 Nov 2026 | Completed |
| 04 | Skenario dan Test Case | Akhmad Maulana Fadil | 23 Nov 2026 | 25 Nov 2026 | Completed |
| 05 | Pengujian Manual | Artha Mauludani | 26 Nov 2026 | 4 Des 2026 | Pending |
| 06 | Pengujian Otomatis | Ariel Modjo Satriawan | 30 Nov 2026 | 8 Des 2026 | Pending |
| 07 | Wawancara QA Engineer | Azacky Habibilah Syahlan | 30 Nov 2026 | 6 Des 2026 | Pending |
| 08 | Laporan Akhir | Akhmad Maulana Fadil | 7 Des 2026 | 12 Des 2026 | Pending |

PIC bertanggung jawab untuk mengoordinasikan dan memastikan setiap tahapan selesai sesuai target. Seluruh anggota tetap terlibat dalam pelaksanaan pengujian, review, dan penyusunan laporan.

### Target Penyelesaian

| Agenda | Target |
| :--- | :--- |
| Pengumpulan Laporan | 12 Desember 2026 |
| Persiapan Presentasi | 13-18 Desember 2026 |
| Presentasi UAS | 19 Desember 2026 |

Timeline dapat disesuaikan dengan kondisi pengerjaan dan jadwal perkuliahan.

## 9. Ringkasan Pengujian

| Parameter | Jumlah |
| :--- | ---: |
| Modul Teridentifikasi | 12 |
| Test Scenario | 22 |
| Total Test Case | 40 |
| Positive Test Case | 28 |
| Negative Test Case | 8 |
| Non-Functional Test Case | 4 |
| Executed | 0 |
| Not Run | 40 |
| Pass | 0 |
| Fail | 0 |
| Defect | Belum diketahui |

Hasil pengujian akan diperbarui setelah tahap Test Execution dilakukan.

## 10. Struktur Repository

    Testing-dan-QA-Kelompok-1/
    ├── README.md
    ├── 01-Referensi/
    │   ├── ISO-Standards.md
    │   └── Journal-References.md
    ├── 02-Analisis-Sistem/
    │   └── System-Inventory.md
    ├── 03-Dokumen/
    │   ├── Test-Plan.md
    │   └── Quality-Metrics.md
    └── 04-Skenario-dan-Test-Case/
        ├── Test-Scenario.md
        └── Test-Case.md

Folder berikutnya akan ditambahkan sesuai dengan tahapan pengerjaan.

## 11. Riwayat Revisi

| Versi | Tanggal | Keterangan |
| :--- | :--- | :--- |
| 2.1.0 | 21 November 2026 | Penyusunan Test Plan dan penentuan ruang lingkup pengujian berdasarkan standar ISO. |
| 2.2.0 | 25 November 2026 | Penambahan referensi, System Inventory, Quality Metrics, Test Scenario, Test Case, serta penyusunan timeline dan struktur dokumentasi. |

## 12. Kesimpulan Sementara

Tahap persiapan pengujian telah selesai dengan menghasilkan 22 test scenario dan 40 test case berdasarkan hasil identifikasi fitur website Mutoh2000.

Tahap selanjutnya adalah pelaksanaan Manual Testing. Seluruh hasil pengujian, dokumentasi evidence, dan temuan defect akan dicatat sebagai bahan evaluasi kualitas website dan penyusunan laporan akhir.
