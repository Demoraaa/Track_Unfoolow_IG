# 🎯 Track_Unfollow_IG / Melacak akun yang tidak mengikuti di IG
**Advanced Instagram Unfollower Tracker & OSINT Tool for Termux**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Termux](https://img.shields.io/badge/Termux-Optimized-green.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

## 📌 Deskripsi
**Track_Unfollow_IG** adalah *script* Python ringan namun berpresisi tinggi yang dirancang khusus untuk membedah data JSON Instagram. Alat ini secara otomatis melacak siapa saja akun yang Anda *follow* namun tidak melakukan *follback* (pengkhianat). 

Berbeda dengan aplikasi pihak ketiga yang rawan *phishing* atau pencurian *password*, Demora berjalan **100% secara lokal (offline)** di perangkat Anda menggunakan data resmi dari Instagram (Download Your Information), sehingga privasi Anda terjamin aman tanpa perlu *login*.

## 🔥 Fitur Utama (God-Mode)
* **X-Ray Extraction:** Mampu menembus enkripsi struktur JSON Instagram yang rumit.
* **/_u/ Anomaly Bypass:** Memiliki filter *Sniper* untuk membuang direktori `/_u/` yang sering membuat *script* tracker lain gagal (Bug teratasi!).
* **Deep Linking (App & Web):** Menyediakan tautan langsung untuk membuka profil target via Browser atau langsung ke Aplikasi Instagram (`instagram://user?...`).
* **Auto-Logging:** Hasil pelacakan otomatis disimpan rapi ke dalam file `.txt` dengan stempel waktu (*timestamp*).
* **CLI Interaktif:** Tampilan antarmuka *Command Line* yang garang, lengkap dengan ASCII Art dan warna.

## ⚙️ Instalasi (Termux / Linux)
Jalankan perintah berikut di terminal Anda:
```bash 
pkg update && pkg upgrade
pkg install python
pkg install git
git clone https://github.com/Demoraaa/Track_Unfollow_IG.git
cd Project-Demora
```

## 🚀 Cara Penggunaan
1. Buka aplikasi Instagram > **Pengaturan** > **Pusat Akun** > **Informasi dan izin Anda** > **Unduh informasi Anda**.
2. Request unduhan dengan format **JSON**.
3. Setelah file didownload dan diekstrak, pindahkan file `followers_1.json` dan `following.json` ke dalam folder yang sama dengan script.
4. Jalankan script:
```bash
python cek_unfoll.py
```
## ⚠️ Disclaimer / Peringatan
Alat ini dibuat murni untuk tujuan edukasi dan kemudahan analisis data pribadi (OSINT). Pengembang tidak bertanggung jawab atas penyalahgunaan *script* ini.
