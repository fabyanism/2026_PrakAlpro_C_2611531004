# Nama      : Fabian Alhadi Zalinov
# NIM       : 2611531004
# Kelas     : Praktikum Algoritma dan Pemrograman C
# Tugas     : Pekan 2 - Tipe Data, Variabel, dan I/O
# Studi Kasus: Sistem Biodata dan Validasi Kelulusan Praktikan
# Catatan   : Seluruh nama variabel diakhiri 4 digit terakhir NIM (1004)

# ==========================================================
# 1. DEKLARASI KONSTANTA MENGGUNAKAN typing.Final
# ==========================================================
from typing import Final

BATAS_LULUS: Final[float] = 75.0

# ==========================================================
# 2. INPUT DATA PRAKTIKAN
# ==========================================================
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# Tipe data String, diambil dari input()
nama_1004 = input("Masukkan Nama Mahasiswa : ")

# Tipe data Char (di Python tetap str), memakai petik tunggal/ganda
jenis_kelamin_1004 = input("Masukkan Jenis Kelamin (L/P): ")

# Type casting ke Integer
umur_1004 = int(input("Masukkan Umur : "))

# Type casting ke Float
skor_1004 = float(input("Masukkan Skor Tes Awal : "))

# ==========================================================
# 3. DATA TETAP (ALAMAT MULTILINE & TOKEN KOMPLEKS)
# ==========================================================
# Tipe data String multiline menggunakan tanda petik tiga
alamat_1004 = """
Garegeh,
Kec. Mandiangin Koto Selayan,
Kota Bukittinggi"""

# Tipe data Complex sebagai token identifikasi praktikan
token_1004 = 100 + 3j

# ==========================================================
# 4. PROSES EVALUASI BOOLEAN
# ==========================================================
# Operator perbandingan menghasilkan nilai True atau False
status_lulus_1004 = skor_1004 >= BATAS_LULUS

# ==========================================================
# 5. OUTPUT DATA DISERTAI PENGECEKAN TIPE DATA type()
# ==========================================================
print()
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_1004, "| Tipe:", type(nama_1004))
print("Jenis Kelamin  :", jenis_kelamin_1004, "| Tipe:", type(jenis_kelamin_1004))
print("Alamat Domisili:", alamat_1004, "| Tipe:", type(alamat_1004))
print("Umur           :", umur_1004, "tahun | Tipe:", type(umur_1004))
print("Skor Tes Awal  :", skor_1004, "| Tipe:", type(skor_1004))
print("ID Token Sinyal:", token_1004, "| Tipe:", type(token_1004))

print()
print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", status_lulus_1004, "| Tipe:", type(status_lulus_1004))