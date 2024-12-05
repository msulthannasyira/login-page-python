## Sistem Login dengan Phyton Flask dan MySQL

>>  **Saat ingin membuat kontribusi, harap uji kode anda sebelum mengirimkan Pull Request (PR).** 

```python 
>>> python unit_test.py
```

### Yang Harus Dilakukan

1. Unduh dan install Phyton, disini kamu menggunakan Python 3.7.2. Patikan untuk mencentang kotak **Add Python to PATH** pada layar pengaturan instalasi. </p>
2. Unduh dan install MySQL Community Server and MySQL Workbench.

### Operasi Utama yang Ditangani
1). Desain Formulir — Membuat desain formulir login dan resgitrasi dengan HTML5 and CSS3.<br>
2). Template — Membuat template Flask dengan HTML an Phyton.<br>
3). Validasi Dasar — Memvalidasi data formulir yang dikirim ke server (username, password, dan email).<br>
4). Manajemen Sesi — Menginisialisasi sesi dan menyimpan hasil yang diambil dari database.<br>
5). Query MySQL — Memilih dan memasukkan data ke/dari tabel database.<br>
6). Rute — Menentukan URL yang mengarah ke fungsi-fungsi tertentu.<br>

### Persyaratan, Paket yang Digunakan, dan Instalasi
Unduh dan instal Python (dalam tutorial ini menggunakan Python 3.7.2). Pastikan untuk mencentang kotak **Add Python to PATH** pada layar pengaturan instalasi.

 
### Instalasi
Arahkan ke direktori proyek Anda, dalam kasus ini **Login-System-with-Python-Flask-and-MySQL**. <br>

### 1. Fork Repositori dan Clone ke Mesin Lokal Anda
```csharp
git clone https://github.com/{your-Github-Username }/Login-System-with-Python-Flask-and-MySQL.git
```
          
### 2. Buat Lingkungan Virtual
> Pastikan Anda berada di direktori yang sama di mana Anda melakukan git clone. Jika tidak, navigasikan ke direktori tersebut.

Tergantung pada sistem operasi Anda, buat lingkungan virtual untuk menghindari mengubah dependensi utama mesin Anda.
          
**Windows**
          
```csharp
cd Login-System-with-Python-Flask-and-MySQL
py -3 -m venv venv

```
          
**macOS/Linux**
          
```csharp
cd Login-System-with-Python-Flask-and-MySQL
python3 -m venv venv

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
