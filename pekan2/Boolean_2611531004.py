# Buat file dengan nama Boolean_2611531004.py
# Buat variabel ditambah 4 digit nim terakhir contoh: nilai_1004
# Deklarasi variabel dengan tipe data Boolean
is_lulus = True
is_cumlaude = True

# Menggunakan Boolean
nilai = 85
batas_lulus = 75
# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai >= batas_lulus  # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai)
print("Apakah Lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat Cum laude!")