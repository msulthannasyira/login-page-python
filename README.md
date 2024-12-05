# Login Page Python

## Penjelasan

Proyek ini bertujuan untuk membangun sebuah sistem login berbasis web menggunakan Python Flask, MySQL, dan XAMPP sebagai server lokal. Flask adalah framework web Python yang ringan dan mudah digunakan, yang memungkinkan pengembangan aplikasi web dengan cepat. Di sisi lain, MySQL adalah sistem manajemen basis data relasional yang sangat populer untuk penyimpanan data aplikasi, seperti akun pengguna dan kredensial login mereka.

Dalam proyek ini, API digunakan untuk menghubungkan antara aplikasi frontend (yang diakses melalui browser) dengan backend, yaitu Flask yang berfungsi untuk menangani logika aplikasi dan MySQL yang berperan sebagai penyimpan data. Penggunaan XAMPP sebagai server lokal memungkinkan pengelolaan database secara visual melalui phpMyAdmin, sehingga mempermudah manajemen dan pemeliharaan basis data.

## Langkah-Langkah

Untuk membuat sistem login menggunakan Python Flask dan MySQL dengan XAMPP sebagai server lokal di Windows, berikut adalah langkah-langkah rinci yang perlu diikuti:

### 1. Unduh dan Instal XAMPP

Unduh XAMPP:

Kunjungi situs resmi XAMPP Downloads.
Pilih installer XAMPP sesuai dengan sistem operasi Windows.
Install XAMPP:

Pilih lokasi untuk menginstal XAMPP (misalnya, `C:\xampp`).
Setelah instalasi selesai, buka XAMPP Control Panel.
Menjalankan MySQL dan Apache:

Di XAMPP Control Panel, klik tombol Start di sebelah MySQL untuk menjalankan server database.
Klik tombol Start di sebelah Apache untuk menjalankan server web (meskipun ini tidak diperlukan untuk Flask, tetap perlu untuk mengelola phpMyAdmin).
Akses phpMyAdmin:

Akses phpMyAdmin dengan membuka browser dan mengunjungi: `http://localhost/phpmyadmin/`.
phpMyAdmin adalah alat GUI untuk mengelola database MySQL yang disediakan oleh XAMPP.

### 2. Instalasi Python
Unduh dan instal Python 3.7.2 atau versi terbaru dari python.org.
Pastikan untuk mencentang kotak `Add Python to PATH` saat proses instalasi.

### 3. Mempersiapkan Proyek
Buat direktori proyek, misalnya Login-Page-Python, dan navigasikan ke dalamnya menggunakan Command Prompt:

```cmd
cd C:\path\to\your\project\Login-Page-Python
```

Jika menggunakan Git, jalankan perintah berikut untuk mengunduh repositori:

```cmd
git clone https://github.com/msulthannasyira/login-page-python.git
```

### 4. Instalasi Paket yang Dibutuhkan

Install semua dependensi yang dibutuhkan dengan perintah:

```cmd
pip install -r requirements.txt
```

### 5. Membuat Basis Data dan Tabel

Buka phpMyAdmin di browser: `http://localhost/phpmyadmin/`.
Buat database baru dengan nama `loginapp`.
Pilih database `loginapp`, kemudian buat tabel accounts dengan perintah SQL berikut di tab SQL:

```sql
CREATE DATABASE loginapp;

USE loginapp;

CREATE TABLE accounts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);
```

### 6. Jalankan Aplikasi
Setelah langkah-langkah di atas selesai, Anda dapat menjalankan aplikasi Flask dengan perintah berikut:

```python
python main.py
```

### Alur Aplikasi. 

**Register Page:**

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-57.png?raw=true)  

**Log In Page:** 

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-52.png?raw=true)

**Home Page After Log In:**

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-28.png?raw=true)
