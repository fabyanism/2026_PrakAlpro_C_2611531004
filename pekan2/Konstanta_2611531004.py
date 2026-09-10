# Buat file dengan nama Konstanta_2611531004.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1004

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_1004 = float(input('Masukkan nilai jari-jari: '))
luas_1004 = PI * jari_1004 * jari_1004
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1004, luas_1004))