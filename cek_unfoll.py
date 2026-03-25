import re
import time
import sys
import os
from datetime import datetime

# === TEMA PROJECT DEMORA ===
SCARLET = '\033[38;5;196m'
WHITE_BOLD = '\033[1;37m'
DARK_GRAY = '\033[1;30m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
RESET = '\033[0m'

def ketik_pelan(teks, kecepatan=0.01):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()

def bersihkan_layar():
    os.system('clear' if os.name == 'posix' else 'cls')

def ekstrak_demora(nama_file):
    if not os.path.exists(nama_file):
        print(f"{SCARLET}[X] Gagal: File '{nama_file}' tidak ditemukan di sistem!{RESET}")
        return None
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            teks = f.read()
        
        usernames = set()
        # Jurus Ekstraksi Lapis 3 (Bypass /_u/ dan laci JSON)
        usernames.update(re.findall(r'"value"\s*:\s*"([^"]+)"', teks))
        usernames.update(re.findall(r'instagram\.com\\?/(?:_u\\?/)?([^/\"\'\?\>\s]+)', teks))
        usernames.update(re.findall(r'"title"\s*:\s*"([^"]+)"', teks))
        
        # Filter Kata Sampah Sistem
        kata_sampah = {'profile_pic_url', 'instagram', 'stories', 'p', 'reel', 'tv', 'explore', 'about', 'help', 'legal', 'directory', 'blog', '_u'}
        
        hasil_bersih = set()
        for u in usernames:
            u_bersih = u.replace('\\', '').split('?')[0]
            if u_bersih.lower() not in kata_sampah and len(u_bersih) > 1:
                hasil_bersih.add(u_bersih.lower())
                
        return hasil_bersih
    except Exception as e:
        print(f"{SCARLET}[X] Demora gagal membedah {nama_file}: {e}{RESET}")
        return None

def main():
    bersihkan_layar()
    # === IDENTITAS ASCII ART ===
    print(f"{SCARLET}")
    print(r"""
 ____  _____ __  __  ___  ____      _    
|  _ \| ____|  \/  |/ _ \|  _ \    / \   
| | | |  _| | |\/| | | | | |_) |  / _ \  
| |_| | |___| |  | | |_| |  _ <  / ___ \ 
|____/|_____|_|  |_|\___/|_| \_\/_/   \_\ 
    """)
    print(f"{CYAN}=================================================={RESET}")
    print(f"{WHITE_BOLD}      🎯  DEMORA_TRACKER : UNFOLL TRACKER  🎯      {RESET}")
    print(f"{CYAN}=================================================={RESET}\n")

    ketik_pelan(f"{DARK_GRAY}[*] Menginisialisasi modul pelacakan...{RESET}")
    
    # === SISTEM INPUT DINAMIS ===
    print(f"\n{YELLOW}[?] Masukkan nama file JSON Anda (Tekan ENTER jika memakai nama default){RESET}")
    in_followers = input(f"{WHITE_BOLD}File Followers [default: followers_1.json]: {RESET}") or "followers_1.json"
    in_following = input(f"{WHITE_BOLD}File Following [default: following.json]: {RESET}") or "following.json"

    ketik_pelan(f"\n{DARK_GRAY}[*] Menjalankan pemindaian tingkat tinggi...{RESET}")
    
    followers = ekstrak_demora(in_followers)
    following = ekstrak_demora(in_following)

    # Hentikan jika file tidak ada
    if followers is None or following is None:
        sys.exit()

    if len(following) == 0:
        print(f"\n{SCARLET}[!] Operasi Dibatalkan: Data following kosong.{RESET}")
        sys.exit()

    # Logika Penentu
    pengkhianat = following - followers

    print(f"\n{DARK_GRAY}--------------------------------------------------{RESET}")
    print(f"{WHITE_BOLD}Total Following Terbaca : {GREEN}{len(following)}{WHITE_BOLD} akun{RESET}")
    print(f"{WHITE_BOLD}Total Followers Terbaca : {GREEN}{len(followers)}{WHITE_BOLD} akun{RESET}")
    print(f"{DARK_GRAY}--------------------------------------------------{RESET}")

    if len(pengkhianat) == 0:
        ketik_pelan(f"\n{GREEN}[+] LUAR BIASA! Semua yang Anda follow telah follback Anda.{RESET}\n")
    else:
        ketik_pelan(f"\n{YELLOW}[!] Demora mengunci {len(pengkhianat)} target operasi:{RESET}\n")
        
        # === SISTEM AUTO-LOGGING ===
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nama_file_log = f"Demora_Result_{waktu_sekarang}.txt"
        
        with open(nama_file_log, 'w', encoding='utf-8') as f_log:
            f_log.write("==================================================\n")
            f_log.write("        PROJECT DEMORA - HASIL PELACAKAN\n")
            f_log.write("==================================================\n")
            f_log.write(f"Waktu Scan : {waktu_sekarang}\n")
            f_log.write(f"Total Tidak Follback: {len(pengkhianat)} akun\n")
            f_log.write("--------------------------------------------------\n\n")
            
            # Tampilkan ke layar DAN simpan ke file
            for i, user in enumerate(sorted(pengkhianat), 1):
                link_ig = f"https://instagram.com/{user}"
                
                # Cetak ke layar Termux (berwarna)
                print(f" {DARK_GRAY}[{SCARLET}{i:03d}{DARK_GRAY}]{RESET} {WHITE_BOLD}{user}{RESET} {DARK_GRAY}->{RESET} {CYAN}{link_ig}{RESET}")
                
                # Tulis ke file log (tanpa warna agar teks tidak rusak)
                f_log.write(f"[{i:03d}] {user} -> {link_ig}\n")
        
        print(f"\n{GREEN}[+] Hasil pelacakan berhasil diamankan ke file: {WHITE_BOLD}{nama_file_log}{RESET}")

    print(f"{CYAN}=================================================={RESET}")
    ketik_pelan(f"{WHITE_BOLD}Misi selesai. Keputusan ada ditanganmu!{RESET}\n")

if __name__ == "__main__":
    main()
