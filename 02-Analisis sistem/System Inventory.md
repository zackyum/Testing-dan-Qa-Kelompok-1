
# System Inventory - Mutoh2000

## 1. Informasi Sistem

| Parameter | Deskripsi |
| :--- | :--- |
| Nama Sistem | Mutoh2000 |
| URL | https://mutoh2000.com/ |
| Jenis Sistem | Website Katalog Produk |
| Platform | Web Application |
| Environment | Production |
| Target Pengguna | Masyarakat umum, perusahaan, dan instansi pendidikan |
| Metode Pengujian | Black Box Testing |

## 2. Deskripsi Sistem

Mutoh2000 merupakan website yang menyediakan katalog produk furnitur kantor dan sekolah. Pengguna dapat mencari produk, melihat kategori, membandingkan produk, serta memperoleh informasi harga dan spesifikasi produk yang tersedia.

## 3. Identifikasi Fitur

| Module ID | Modul | Fitur | Prioritas |
| :--- | :--- | :--- | :--- |
| MOD-01 | Homepage | Tampilan beranda, banner, kategori, dan promosi produk. | High |
| MOD-02 | Navigation | Menu, submenu, header, dan footer. | High |
| MOD-03 | Product Catalog | Daftar produk dan pagination. | High |
| MOD-04 | Product Search | Pencarian produk berdasarkan kata kunci. | High |
| MOD-05 | Product Category | Pemilihan kategori dan subkategori produk. | High |
| MOD-06 | Filter & Sorting | Filter harga dan pengurutan produk. | High |
| MOD-07 | Product Detail | Informasi harga, gambar, spesifikasi, dan variasi produk. | High |
| MOD-08 | Wishlist | Menambahkan dan menghapus produk dari wishlist. | Medium |
| MOD-09 | Compare Product | Menambahkan dan membandingkan produk. | Medium |
| MOD-10 | Language | Pilihan bahasa Indonesia dan Inggris. | Medium |
| MOD-11 | Company Information | Informasi perusahaan. | Low |
| MOD-12 | Contact | Informasi kontak dan tautan komunikasi. | Medium |

## 4. Kategori Produk

Kategori produk yang tersedia pada website:

- Brankas
- Filing Cabinet
- Lemari Arsip
- Lemari Pakaian
- Locker
- Kursi Kantor
- Meja Kantor
- Meja Kursi Siswa
- Rak Buku
- White Board

## 5. Alur Penggunaan Website

1. Pengguna membuka halaman utama.
2. Pengguna memilih kategori atau mencari produk.
3. Pengguna menggunakan filter atau pengurutan produk.
4. Pengguna memilih dan membuka detail produk.
5. Pengguna dapat menyimpan atau membandingkan produk.
6. Pengguna dapat menghubungi pihak Mutoh2000 untuk informasi lebih lanjut.

## 6. Batasan Pengujian

Pengujian dilakukan pada fitur yang dapat diakses secara publik tanpa akses administrator, kode sumber, dan database.

Pengujian tidak mencakup transaksi pembelian secara nyata, pengiriman pesan, maupun pengujian keamanan aktif tanpa izin pemilik website.

## 7. Referensi

- https://mutoh2000.com/
- https://mutoh2000.com/shop/

## 8. Identifikasi Aktor Sistem

| Aktor | Deskripsi Aktivitas |
| :--- | :--- |
| Visitor | Mengakses website dan melihat informasi produk |
| Customer | Mencari, melihat, menyimpan, dan membandingkan produk |
| Admin / Customer Service | Melayani pertanyaan dan komunikasi pelanggan |
| Website Administratror | Mengelola informasi, katalog, dan konten website |

## 9. Kebutuhan Fungsional

| ID | Kebutuhan | Deskripsi |
| :--- | :--- | :--- |
| FR-01 | Homepage | Sistem menampilkan halaman utama website |
| FR-02 | Navigation | Sistem menyediakan navigasi antarhalaman |
| FR-03 | Product Catalog | Sistem menampilakn daftar produk |
| FR-04 | Product Search | Sistem menyediakan pencarian produk |
| FR-05 | Product Category | Sistem menyediakan kategori dan subkategori |
| FR-06 | Price Filter | Sistem menyediakan penyaringan produk berdasarkan harga |
| FR-07 | Product Sorting | Sistem menyediakan pengurutan produk |
| FR-08 | Product Detail | Sistem menampilkan informasi detail produk |
| FR-09 | Wishlist | Sistem memungkinkan pengguna menyimpan produk favorit |
| FR-10 | Compare Product | Sistem memungkinkan pengguna membandingkan produk |
| FR-11 | Product Availability | Sistem menampilkan informasi ketersediaan produk |
| FR-12 | Contact | Sistem menyediakan informasi kontak perusahaan |
| FR-13 | Language | Sistem menyediakan pilihan bahasa apabila fitur tersedia pada halaman yang diuji |

# 10. Kebutuhan Nonfungsional

| ID | Aspek | Kebutuhan | 
| :--- | :--- | :--- |
| NFR-01 | Usability | Website mudah dipahami dan digunakan |
| NFR-02 | Performance | Halaman dapat dimuat dengan waktu respons yang wajar |
| NFR-03 | Reliability | Fungsi website berjalan secara konsisten |
| NFR-04 | Compatibility | Website dapat diakses melalui browser yang umum digunakan |
| NFR-05 | Responsiveness | Tampilan menyesuaikan ukuran layar perangkat |
| NFR-06 | Security | Website melindungi komunikasi dan data pengguna |
| NFR-07 | Availability | Website dapat diakses ketika dibutuhkan |
| NFR-08 | Maintainability | Informasi produk dan konten dapat diperbarui oleh pengelola |

## 11. Alur Proses Bisnis

Alur penggunaan website MUTOH2000:
1. Pengguna membuka website MUTOH2000.
2. Sistem menampilkan halaman homepage.
3. Pengguna memilih kategori atau memasukkan kata kunci pencarian.
4. Sistem menampilkan daftar produk yang sesuai.
5. Pengguna melakukan filter atau sorting produk.
6. Pengguna memilih salah satu produk.
7. Istem menampilkan detail produk, harga, spesifikasi, dan ketersediaan.
8. Pengguna dapat menambahkan produk ke wishlist atau compare.
9. Pengguna menghubungi admin melalui WhatsApp untuk mendapatkan informasi lebih lanjut.

## 12. Test Environment

| Parameter | Keterangan |
| :--- | :--- |
| Application | Website MUTOH2000 |
| URL | https://mutoh2000.com/ |
| Environment | Production |
| Testing Type | Manual BlackBox Testing |
| Browser | Google Chrome |
| Operating System | Windows 10/11 |
| Device | Desktop dan Mobile | 
| Network | nternet connection |
| Test Data | Kata kunci pencarian, kategori, rentang harga, dan data produk | 

## 13. Risiko Pengujian 

| ID | Risiko | Dampak | Prioritas |
| :--- | :--- | :--- | :--- |
| R-01 | Pencarian tidak menampilkan produk yang sesuai | Pengguna kesulitan menemukan produk | High | 
| R-02 | Filter harga tidak berfungsi | Hasil produk tidak sesuai kriteria | High |
| R-03 | Informasi harga tidak konsisten | Kesalahan informasi kepada pelanggan | High |
| R-04 | Detail produk tidak tampil sempurna | Informasi produk tidak lengkap | High | 
| R-05 | Wishlist tidak menyimpan produk | Produk favorit tidak tercatat | Medium |
| R-06 | Compare tidak menampilkan produk dengan benar | Perbandingan produk terganggu | Medium | 
| R-07 | Navigasi mengalami kesalahan | Pengguna kesulitan berpindah halaman | Medium | 
| R-08 | Tampilan mobile tidak responsif | Pengalaman pengguna terganggu | Medium |

## 14. Asumsi dan Batasan Analisis

1. Analisis dilakukan berdasarkan fitur yang dapat diakses melalui website publik.
2. Pengujian tidak menggunakan akun administrator internal.
3. Database dan source code internal tidak menjadi objek pemeriksaan.
4. Data produk yang ditampilkan dapat berubah sewaktu-waktu.
5. Ketersediaan produk dan harga mengikuti informasi yang ditampilkan website saat pengujian.
6. Pengujian tidak melakukan transaksi pembelian nyata.
7. Fitur yang tidak dapat diakses atau diverifikasi tidak dinyatakan telah memenuhi kebutuhan sistem.

## 15. Kesimpulan Analisis Sistem

Berdasarkan hasil identifikasi, MUTOH2000 merupakan website katalog produk yang menyediakan berbagai fitur untuk membantu pengguna mencari dan memperoleh informasi produk furnitur kantor dan sekolah.

Fitur utama yang menjadi perhatian meliputi homepage, navigasi, katalog produk, pencarian, kategori, filter harga, sorting, detail produk, wishlist, compare product, dan informasi kontak.

Hasil analisis ini akan digunakan sebagai dasar bagi tahapan pengujian selanjutnya, khususnya dalam menentukan prioritas modul, ruang lingkup pengujian, serta identifikasi risiko pada website MUTOH2000.
