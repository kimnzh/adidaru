Nama : Muhamad Hakim Nizami<br/>
NPM : 2406399485<br/>
Kelas : PBP E

Link Deployment: https://muhamad-hakim41-adidaru.pbp.cs.ui.ac.id

# Tugas 2

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

# Tugas 3

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery merupakan salah satu aspek krusial dalam sebuah platform, karena peran dari sebuah aplikasi selain untuk memaparkan informasi kepada pengguna, juga harus bisa menerima masukan yang nantinya akan digunakan oleh pengguna ataupun orang lain.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, **JSON** lebih baik daripada **XML** karena data mentah **JSON** lebih mudah dibaca daripada **XML**. **JSON** (JavaScript Object Notation) lebih populer daripada **XML** karena lebih sederhana dan cenderung lebih kompatibel dengan web browser, karena kebanyakan web browser menggunakan **JavaScript** sebagai scripting languagenya.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Untuk memvalidasi bahwa data yang diperoleh dari form tidak memberikan error apapun. Methid akan mengembalikan nilai `True` jika tidak ada error dan akan mengembalikan nilai `False` jika terdapat error dalam form. Error dapat berupa data yang tidak kompatibel dengan nilai yang seharusnya ataupun melebihi batasan-batasan yang sudah ditentukan oleh program (tipe data, maksimal ukuran data, dll).

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` adalah token yang di generate aplikasi django dalam suatu session yang dimiliki user. Tujuan dari token ini adalah menghindari percobaan penyerangan oleh pengguna yang tidak memiliki otoritas untuk mengakses, memberi input, atau menerima data dari aplikasi django. Maka dari itu, forms memerlukan `csrf_token`

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Saya mulai dengan mengimplementasikan 4 function di dalam `views.py` sesuai dengan yang didefinisikan di dalam tutorial.
- Saya kemudian mengaitkan setiap views tersebut dengan path yang sesuai dengan dengan definisi functionnya dalam `views.py`.
- Berbeda dengan checklist, saya terlebih dahulu membuat halaman `form` untuk menambahkan barang baru ke database.
- Karena sebelumnya saya sudah membuat page untuk katalog barang-barang (mockup), saya hanya menambahkan menambahkan tombol untuk menambahkan barang baru di bagian bawah katalog yang akan meredirect halaman ke `form`.
- Untuk halaman yang menampilkan detail barang, sudah saya implementasikan dari minggu sebelumnya.
- Selanjutnya saya melanjutkan isi file `README.md` yang sudah ada dari minggu sebelumnya.
- Terakhir, saya menguji data delivery aplikasi menggunakan software **Postman**.

### `show_xml`

![show_xml](https://cdn.discordapp.com/attachments/1277292036709548065/1417127133343645839/image.png?ex=68c959fd&is=68c8087d&hm=4f78476075ef82f89ddce72fd5bcde7f3724e80bf6d9a3c52eb9f5773c606e7f)

### `show_xml_by_id`

![show_xml_by_id](https://cdn.discordapp.com/attachments/1277292036709548065/1417127328945017018/image.png?ex=68c95a2c&is=68c808ac&hm=6019c779243f77f5150bc2359b71a4934fdbe16089413e9a86d0351c9acf98bb)

### `show_json`

![show_json](https://cdn.discordapp.com/attachments/1277292036709548065/1417127513104060536/image.png?ex=68c95a58&is=68c808d8&hm=24fc9ba9e54f0070a5defb0a42b9c69d1dc2f64f80e5870c9fe89eda497d0ef7)

### `show_json_by_id`

![show_json_by_id](https://cdn.discordapp.com/attachments/1277292036709548065/1417127523233562675/image.png?ex=68c95a5a&is=68c808da&hm=cb12278a64e54750c4b77cd781a59da17e96c50bd21ac45113e7c03a52fef0f0)

## Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tetap mantap dan pertahankan saja :)

# Tugas 4

## Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.

`AuthenticationForm` di Django adalah sebuah built-in class untuk melakukan autentikasi user ke dalam aplikasi Django. Autentikasi di sini bermakna login dan akan menyimpan session user ke dalam aplikasi.

Referensi: [Django Documentation](https://docs.djangoproject.com/en/5.2/topics/auth/default/)

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

- **Autentikasi** adalah pemastian dan verifikasi identitas seorang pengguna menggunakan kredensial seperti email, username, password, dan lainnya.

- **Otorisasi** adalah pemberiasn akses terhadap suatu data, halaman atau fitur di dalam aplikasi untuk pengguna yang terautentikasi.

Referensi: [GeeksForGeeks](https://www.geeksforgeeks.org/computer-networks/difference-between-authentication-and-authorization/)

## Apa saja kelebihan dan kekurangan _session_ dan _cookies_ dalam konteks menyimpan _state_ di aplikasi web?

- **Session** memiliki kelebihan yaitu keamanan data autentikasi karena tersimpan di dalam server, kekurangannya adalah serrver akan cepat penuh jika terdapat banyak _session_ dalam satu waktu.

- **Cookie** memiliki kelebihan yaitu karena tersimpan di client-side, maka server tidak akan overload untuk menyimpan datanya. Kekurangannya adalah kurang aman karena bisa saja diakses oleh orang lain jika token cookies bocor.

Referensi: [GeeksForGeeks](https://www.geeksforgeeks.org/javascript/difference-between-session-and-cookies/)

## Apakah penggunaan _cookies_ aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

**Cookies** secara umum tidak aman karena ada beberapa jenis serangan siber seperti _Session hijacking_, _Cross-Site Request Forgery_ dan lainnya. Django menangani ini dengan menyimpan session di dalam server, bukan dari token yang disimpan di dalam cookies.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

- Mengikuti tahapan yang ada pada tutorial 3, dengan beberapa modifikasi dalam pembuatan template html dan strukturnya.
- Register 2 akun secara langsung di local kemudian push ke pws supaya database juga update.
- Menggunakan foreign key user_id yang diambil dari id pada model User bawaan Django.
- Menambahkan context ke dalam page home supaya tampil di bagian navbar (saat hover username).
