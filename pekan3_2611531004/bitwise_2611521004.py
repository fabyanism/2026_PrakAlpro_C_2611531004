# Buat file dengan nama bitwise_2611531004.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1004
# Program ini menggunakan fungsi input()

print("===================================")
print("1. OPERATOR BITWISE")
print("===================================")

angka1_1004 = int(input("Masukkan angka bitwise-1: "))
angka2_1004 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1004, "| biner =", bin(angka1_1004))
print("angka2 =", angka2_1004, "| biner =", bin(angka2_1004))

# Bitwise AND
hasil_1004 = angka1_1004 & angka2_1004
print("\nBitwise AND (&)")
print(angka1_1004, "&", angka2_1004, "=", hasil_1004)
print("Biner hasil =", bin(hasil_1004))
print("Biner hasil (8 bit) =", format(hasil_1004, '08b'))

# Bitwise OR
hasil_1004 = angka1_1004 | angka2_1004
print("\nBitwise OR (|)")
print(angka1_1004, "|", angka2_1004, "=", hasil_1004)
print("Biner hasil =", bin(hasil_1004))
print("Biner hasil (8 bit) =", format(hasil_1004, '08b'))

# Bitwise XOR
hasil_1004 = angka1_1004 ^ angka2_1004
print("\nBitwise XOR (^)")
print(angka1_1004, "^", angka2_1004, "=", hasil_1004)
print("Biner hasil =", bin(hasil_1004))
print("Biner hasil (8 bit) =", format(hasil_1004, '08b'))

# Bitwise NOT
hasil_1004 = ~angka1_1004
print("\nBitwise NOT (~)")
print("~", angka1_1004, "=", hasil_1004)
print("Biner hasil =", bin(hasil_1004))
print("Biner hasil (8 bit) =", format(hasil_1004, '08b'))

# Bitwise geser kiri
jumlah_geser_1004 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1004 = angka1_1004 << jumlah_geser_1004
print("\nBitwise geser kiri (<<)")
print(angka1_1004, "<<", jumlah_geser_1004, "=", hasil_1004)
print("Biner hasil =", bin(hasil_1004))
print("Biner hasil (8 bit) =", format(hasil_1004, '08b'))

# Bitwise geser kanan
hasil_1004 = angka1_1004 >> jumlah_geser_1004
print("\nBitwise geser kanan (>>)")
print(angka1_1004, ">>", jumlah_geser_1004, "=", hasil_1004)
print("Biner hasil =", bin(hasil_1004))
print("Biner hasil (8 bit) =", format(hasil_1004, '08b'))