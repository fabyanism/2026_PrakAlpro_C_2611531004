# Buat file dengan nama aritmatika_2611531004.py
# Buat program untuk operator aritmatika dalam Phyton
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1004
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1004 = int(input("Input angka-1: "))
angka2_1004 = int(input("Input angka-2: "))

# Penjumlahan
hasil_1004 = angka1_1004 + angka2_1004
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1004)

# Pengurangan
hasil_1004 = angka1_1004 - angka2_1004
print("\nOperator Pengurangan")
print("Hasil =", hasil_1004)

# Perkalian
hasil = angka1_1004 * angka2_1004
print("\nOperator Perkalian")
print("Hasil =", hasil_1004)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1004 != 0:
    hasil = angka1_1004 / angka2_1004
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1004)

    hasil = angka1_1004 // angka2_1004
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1004)

    hasil = angka1_1004 % angka2_1004
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1004)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil = angka1_1004 ** angka2_1004
print("\nOperator Pangkat")
print("Hasil =", hasil_1004)