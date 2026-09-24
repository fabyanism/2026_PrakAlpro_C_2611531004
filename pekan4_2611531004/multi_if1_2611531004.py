# Buat file dengan nama multi_if1_261531004.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1004
# Program ini menggunakan fungsi input()

umur_1004 = int(input("Input umur anda: "))
sim_1004 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_1004 >= 17 and sim_1004 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_1004 >= 17 and sim_1004 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_1004 < 17 and sim_1004 == 'y':
    print("Anda Belum Cukup Umur punya sim")

if umur_1004 < 17 and sim_1004 != 'y':
    print("Anda Belum Cukup Umur bawa motor")