Nama : Muhamad Hakim Nizami<br/>
NPM : 2406399485<br/>
Kelas : PBP E

Link Deployment: https://muhamad-hakim41-adidaru.pbp.cs.ui.ac.id

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Untuk membuat proyek baru Django, saya mengikuti seluruhnya dari **Tutorial 0**, alasannya supaya sesuai dengan alur deployment yang sudah terdefine untuk pws. Tentu ada beberapa adjustment yang saya tambahkan supaya sesuai dengan kriteria tugas individu, seperti penambahan skema `tugas_individu` dalam env variables.
- Untuk membuat aplikasi bernama `main`, saya juga mostly mengikuti **Tutorial 1**, dan alasan utamanya juga supaya sesuai dengan alur development yang viable untuk deployment ke pws.
- Untuk routing, saya cukup mendefinisikan beberapa path/endpoint ke dalam list urlpatterns dalam file `urls.py`. Masing-masing endpoint akan me-render page-page tertentu yang sesuai dengan kebutuhan.
- Saya mendefinisikan model sesuai dengan cara pendefinisian model pada umumnya seperti pada ORM-ORM populer (Prisma, GORM, Drizzle, etc.), dan format mengacu kepada **Tutorial 1** yang menjelaskan langkah-langkahnya secara runtut. Saya juga mendefinisikan constants dalam variabel bernama `PRODUCTS` untuk mencontohkan penggunaan model.
- Saya jadinya membuat beberapa fungsi di dalam `views.py` untuk menampilkan beberapa page dengan tujuan tertentu, yaitu `home`, `product_detail`, `cart`, dan `checkout`. Masing-masing menjelaskan tujuan dari pagenya.
- Saya mengikuti langkah deployment PWS seperti pada **Tutorial 0**.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![bagan](https://cdn.discordapp.com/attachments/1277292036709548065/1415195089256317008/bagan_django.png?ex=68c252a2&is=68c10122&hm=0bf720e5ba3c08d20d085930ec18546af7daba1c1f8a5efffc2f1e1d82de1e8c)

- `urls.py`
  Menentukan routing: URL mana diarahkan ke view function mana. Contoh: path('cart/', cart, name='cart') artinya /cart/ akan dijalankan oleh fungsi cart di views.py.

- `views.py`
  Menjadi penghubung utama, menerima request, memproses logika (mengambil data dari models.py), lalu mengirimkan context ke template. Contoh: fungsi cart() membuat daftar produk dan menghitung total harga.

- `models.py`
  Berisi struktur data/tabel database (di sini contoh pakai mock list PRODUCTS). View mengambil data dari **Product** untuk ditampilkan di halaman. HTML Templates Menampilkan data kepada pengguna. Data dari **views.py** dikirim dalam bentuk context, lalu dirender di file HTML (misalnya store/cart.html).

## 3. Jelaskan peran settings.py dalam proyek Django!

- Menghubungkan proyek Django dengan database server
- Menghubungkan proyek Django dengan semua template HTML yang terdefinisi
- Menangani file-file statis (tidak berubah) pada proyek Django seperti contohnya file `.css`
- Menggunakan middleware pada proyek Django
- Menghubungkan proyek Django dengan aplikasi-aplikasiyang dibbuat

## 4. Bagaimana cara kerja migrasi database di Django?

Migrasi database di Django adalah proses untuk menyamakan struktur database dengan definisi model di `models.py`. Saat developer membuat atau mengubah model, Django menghasilkan file migrasi menggunakan perintah `makemigrations` yang berisi instruksi perubahan database (seperti membuat tabel atau menambah kolom). File ini kemudian dijalankan dengan perintah `migrate`, sehingga Django mengeksekusi perintah SQL yang sesuai pada database dan mencatat status migrasi di tabel khusus django_migrations. Dengan cara ini, pengelolaan perubahan skema database menjadi otomatis, teratur, konsisten, dan tidak perlu menulis SQL manual.

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Karena proyek Django menggunakan bahasa Python sebagai main language nya. Python adalah bahasa pemrograman yang paling mudah dipahami oleh manusia untuk saat ini sehingga learning curve untuk belajar Web Programming dengan Django dapat lebih landai dibanding framework-framework lainnya yang kebanyakan menggunakan bahasa pemrograman yang lebih low level seperti javascript ataupun php

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Mungkin lebih perjelas lagi langkah-langkahnya secara verbal, karena kebanyakan teman saya mengerjakan tutorial bermodalkan copas-copas saja.
