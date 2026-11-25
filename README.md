
# Analisis Pengujian Website Mutoh2000

![Version](https://img.shields.io/badge/Version-2.2.0-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Method](https://img.shields.io/badge/Method-Black%20Box%20Testing-green)

## 1. Informasi Proyek

| Parameter | Deskripsi |
| :--- | :--- |
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

Proyek ini dilakukan untuk menganalisis kualitas dan fungsionalitas website Mutoh2000 menggunakan metode Black Box Testing dengan mengacu pada standar ISO/IEC/IEEE 29119 dan ISO/IEC 25010:2023.

Mutoh2000 merupakan website katalog produk perlengkapan kantor dan sekolah yang menyediakan berbagai fitur, seperti pencarian produk, kategori, filter harga, detail produk, wishlist, dan compare product.

Pengujian dilakukan untuk mengetahui kesesuaian fungsi website, mengidentifikasi defect, serta memberikan rekomendasi berdasarkan hasil pengujian.

## 4. Tujuan Pengujian

- Memastikan fitur website berjalan sesuai dengan fungsi yang diharapkan.
- Mengidentifikasi bug atau defect pada website.
- Mengevaluasi kualitas website berdasarkan ISO/IEC 25010:2023.
- Melaksanakan pengujian manual dan otomatis.
- Mendokumentasikan proses dan hasil pengujian.

## 5. Standar Acuan

| Standar | Keterangan |
| :--- | :--- |
| ISO/IEC/IEEE 29119-1:2022 | General Concepts |
| ISO/IEC/IEEE 29119-2:2021 | Test Processes |
| ISO/IEC/IEEE 29119-3:2021 | Test Documentation |
| ISO/IEC/IEEE 29119-4:2021 | Test Techniques |
| ISO/IEC 25010:2023 | Product Quality Model |

Referensi standar dan jurnal pendukung tersedia pada folder `01-Referensi`.

## 6. Metode dan Tools Pengujian

### Metode Pengujian

- Black Box Testing
- Equivalence Partitioning
- Boundary Value Analysis
- Error Guessing
- Exploratory Testing

### Tools

| Tools | Kegunaan |
| :--- | :--- |
| Web Browser | Manual Testing |
| Chrome DevTools | Pemeriksaan tampilan dan responsivitas |
| Playwright | Automated Testing |
| Lighthouse | Performance Testing |
| GitHub | Dokumentasi pengujian |
| GitHub Issues | Defect Tracking |

## 7. Ruang Lingkup Pengujian

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

Pengujian terbatas pada fitur yang dapat diakses secara publik dan tidak mencakup transaksi nyata maupun pengujian yang dapat mengganggu operasional website.

## 8. Progress Pengerjaan

| No. | Tahapan | Status |
| :--- | :--- | :--- |
| 01 | Referensi ISO dan Jurnal | Completed |
| 02 | Analisis Sistem | Completed |
| 03 | Test Plan dan Quality Metrics | Completed |
| 04 | Test Scenario dan Test Case | Completed |
| 05 | Pengujian Manual | Pending |
| 06 | Laporan Bug | Pending |
| 07 | User Acceptance Testing | Pending |
| 08 | Pengujian Otomatis | Pending |
| 09 | Pengujian Non-Fungsional | Pending |
| 10 | Pengujian API | Pending |
| 11 | Pengujian Regresi | Pending |
| 12 | Wawancara QA Engineer | Pending |
| 13 | Log Aktivitas | Pending |
| 14 | Laporan Akhir dan Presentasi | Pending |

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
    ├── 02-Analisis-Sistem/
    ├── 03-Dokumen/
    └── 04-Skenario-dan-Test-Case/

Struktur repository akan diperbarui mengikuti tahapan pengerjaan.

## 11. Riwayat Revisi

| Versi | Tanggal | Keterangan |
| :--- | :--- | :--- |
| 2.1.0 | 21 November 2026 | Penyusunan dokumen Test Plan berdasarkan standar ISO. |
| 2.2.0 | 25 November 2026 | Penambahan referensi, System Inventory, Quality Metrics, Test Scenario, dan Test Case serta pembaruan struktur dokumentasi. |

## 12. Kesimpulan Sementara

Tahap persiapan pengujian telah selesai, meliputi identifikasi sistem, penyusunan rencana pengujian, penentuan parameter kualitas, serta penyusunan skenario dan test case.

Tahap berikutnya adalah pelaksanaan Manual Testing berdasarkan test case yang telah disusun. Hasil pengujian dan temuan defect akan didokumentasikan secara bertahap.
