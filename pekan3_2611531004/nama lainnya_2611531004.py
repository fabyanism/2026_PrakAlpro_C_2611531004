# Buat file dengan nama lainnya_2611531004.py
# Buat variabel ditambah 4 digit nim terakhir contoh: angka1_1004
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("===================================")
print("1. OPERATOR KEANGGOTAAN")
print("===================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1004 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1004 = [int(angka_1004.strip()) for angka_1004 in input_data_1004.split(",")]

nilai_dicari_1004 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1004 = nilai_dicari_1004 in data_1004
print("\nOperator keanggotaan IN")
print(nilai_dicari_1004, "in", data_1004, "=", hasil_1004)

# Operator not in
hasil_1004 = nilai_dicari_1004 not in data_1004
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1004, "not in", data_1004, "=", hasil_1004)


print("\n===================================")
print("2. OPERATOR IDENTITAS")
print("===================================")

# objek1 menggunakan list dari input pengguna
objek1_1004 = data_1004

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1004 = objek1_1004

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1004 = data_1004.copy()

print("objek1 =", objek1_1004)
print("objek2 =", objek2_1004)
print("objek3 =", objek3_1004)

# Operator is
hasil_1004 = objek1_1004 is objek2_1004
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_1004)

# Operator is not
hasil_1004 = objek1_1004 is not objek3_1004
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_1004)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai:")
print("objek1 is objek 3 = ", objek1_1004 is objek3_1004)
print("objek1 == objek 3 = ", objek1_1004 == objek3_1004)