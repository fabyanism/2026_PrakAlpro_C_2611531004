# Buat file dengan nama nested_for1_2611531004.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1004
# Program ini menggunakan fungsi input()''

batas_1004 = int(input("Masukkan nilai batas: "))
for line_1004 in range(1, batas_1004 + 1):
    for j_1004 in range(1, (-1 * line_1004 + batas_1004) + 1):
        print(".", end=" ")
    print(line_1004)