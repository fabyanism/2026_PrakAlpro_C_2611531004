# Buat file dengan nama latihan5_2611531004.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1004
# Program ini menggunakan fungsi input()

tinggi_1004 = int(input("Masukkan tinggi segitiga: "))

for i_1004 in range(1, tinggi_1004 + 1):
    print(" " * (tinggi_1004 - i_1004), end="")
    print("* " * i_1004)