# Buat file dengan nama logika_2611531004.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1004
# Program ini menggunakan fungsi input()
# Program operator logika dalam Phyton

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1004 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_1004 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_1004)
print("A2 =", a2_1004)

# Konjungsi: bernilai True jika keduanya True
hasil_1004 = a1_1004 and a2_1004
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1004)

# Disjungsi: bernilai True jika salah satunya True
hasil_1004 = a1_1004 or a2_1004
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_1004)

# Negasi A1: membalikkan nilai A1
hasil_1004 = not a1_1004
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1004)

# Negasi A2: membalikkan nilai A2
hasil_1004 = not a2_1004
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1004)

#XOR: bernilai True jika kedua nilai berbeda
hasil_1004 = a1_1004 != a2_1004
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1004)