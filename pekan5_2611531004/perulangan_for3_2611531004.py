# Buat file dengan nama perulangan_for3_2611531004.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1004
# Program ini menggunakan fungsi input()

ulang_1004 = int(input("Masukkan jumlah perulangan: "))

jumlah_1004 = 0
for i_1004 in range(1, ulang_1004 + 1):
    print(i_1004, end=" ")
    jumlah_1004 = jumlah_1004 + i_1004

    if i_1004 < ulang_1004:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_1004, end=" ")
print()
print("Jumlah =", jumlah_1004)
