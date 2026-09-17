# Buat file dengan nama assignment_2611531004.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nama_1004
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Phyton

angka1_1004 = int(input("Input angka-1: "))
angka2_1004 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_1004)
print("Nilai awal angka2 =", angka2_1004)

# Assignment biasa
hasil_1004 = angka1_1004
print("\nAssignment biasa (=)")
print("Hasil =", hasil_1004)

# Assignment penambahan
hasil_1004 = angka1_1004
hasil_1004 += angka2_1004
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_1004)

# Assignment pengurangan
hasil_1004 = angka1_1004
hasil_1004 -= angka2_1004
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_1004)

# Assignment perkalian
hasil_1004 = angka1_1004
hasil_1004 *= angka2_1004
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_1004)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1004 != 0:
    hasil_1004 = angka1_1004
    hasil_1004 /= angka2_1004
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_1004)
    # Operator tambahan
    hasil_1004 = angka1_1004
    hasil_1004 //= angka2_1004
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_1004)
    hasil_1004 = angka1_1004
    hasil_1004 %= angka2_1004
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_1004)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_1004 = angka1_1004
hasil_1004 **= angka2_1004
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_1004)