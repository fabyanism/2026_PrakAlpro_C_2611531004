# Buat file dengan nama nested_for4_2611531004.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1004
# Program ini menggunakan fungsi input()

tinggi_1004 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1004 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1004 = tinggi_1004
    c_1004 = a_1004
    lebar_1004 = (2 * tinggi_1004) - 2

    for i_1004 in range(1, tinggi_1004 + 1):
        b_1004 = c_1004 + 1

        for j_1004 in range(1, lebar_1004 + 1):

            # Baris atas atau bawah
            if i_1004 == 1 or i_1004 == tinggi_1004:
                if j_1004 == 1 or j_1004 == lebar_1004:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_1004 == 1 or j_1004 == lebar_1004:
                    print("|", end="")
                else:
                    if j_1004 == c_1004:
                        print("<", end="")
                    elif j_1004 == b_1004:
                        print(">", end="")
                    elif j_1004 == (lebar_1004 - c_1004):
                        print("<", end="")
                    elif j_1004 == (lebar_1004 - c_1004 + 1):
                        print(">", end="")
                    elif j_1004 > b_1004 and j_1004 < (lebar_1004 - c_1004):
                        print("-", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_1004 -= 2

        if a_1004 <= 0:
            c_1004 = (-a_1004) + 2
        else:
            c_1004 = a_1004