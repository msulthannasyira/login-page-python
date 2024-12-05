## Sistem Login dengan Phyton Flask dan MySQL

Untuk membuat sistem login menggunakan Python Flask dan MySQL dengan menggunakan XAMPP sebagai server lokal, berikut adalah langkah-langkah rinci yang perlu diikuti:

1. Unduh dan Instal XAMPP
Unduh XAMPP:

Kunjungi situs resmi XAMPP: XAMPP Downloads.
Pilih installer XAMPP sesuai dengan sistem operasi yang kamu gunakan (Windows, macOS, atau Linux).
Setelah mengunduh, jalankan installer dan ikuti langkah-langkah instalasi.
Instal XAMPP:

Pilih lokasi untuk menginstal XAMPP (misalnya, C:\xampp untuk Windows).
Setelah instalasi selesai, buka XAMPP Control Panel.
Menjalankan MySQL dan Apache:

Di XAMPP Control Panel, klik tombol Start di sebelah MySQL untuk menjalankan server database.
Klik tombol Start di sebelah Apache untuk menjalankan server web (untuk aplikasi PHP atau lain-lain yang berbasis web, namun tidak diperlukan untuk Flask).
Akses phpMyAdmin:

Akses phpMyAdmin dengan membuka browser dan mengunjungi: http://localhost/phpmyadmin/.
phpMyAdmin adalah alat GUI untuk mengelola database MySQL, yang disediakan oleh XAMPP.

### Persyaratan, Paket yang Digunakan, dan Instalasi
Unduh dan instal Python (dalam tutorial ini menggunakan Python 3.7.2). Pastikan untuk mencentang kotak **Add Python to PATH** pada layar pengaturan instalasi.

### Instalasi
Arahkan ke direktori proyek Anda, dalam kasus ini **Login-Page-Python**. <br>

### 1. Fork Repositori dan Clone ke Mesin Lokal Anda
```csharp
git clone https://github.com/msulthannasyira/login-page-python.git
```
          
### 2. Buat Lingkungan Virtual
> Pastikan Anda berada di direktori yang sama di mana Anda melakukan git clone. Jika tidak, navigasikan ke direktori tersebut.

Tergantung pada sistem operasi Anda, buat lingkungan virtual untuk menghindari mengubah dependensi utama mesin Anda.
          
**Windows**
          
```csharp
cd https://github.com/msulthannasyira/login-page-python
```
          
**macOS/Linux**
          
```csharp
cd https://github.com/msulthannasyira/login-page-python
```

### 3. Aktifkan Lingkungan
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
atau
```source venv/bin/activate```

### 4. Install Persyaratan

Berlaku untuk Windows/macOS/Linux

```csharp
pip install -r requirements.txt
```


### 5. Buat Basis Data dan Tabel 

```sql
-- Create the  database named "loginapp"
CREATE DATABASE loginapp;


-- Switch to 'loginapp' database; 
USE loginapp; 


-- Create 'account' table with id, username,email, password columns. 
CREATE TABLE accounts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
); 
```

### 6. Jalankan Aplikasi

**Untuk linux dan macOS**
Jadikan file run dapat dieksekusi dengan kode berikut:

```chmod 777 run```

Kemudian mulai aplikasi dengan menjalankan file run:

```./run```

**Pada Windows**
```
set FLASK_APP=main
flask run

```
### Alur Aplikasi. 

**Register Page:**

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-57.png?raw=true)  

**Log In Page:** 

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-52.png?raw=true)

**Home Page After Log In:**

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-28.png?raw=true)
