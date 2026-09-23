"""
Tugas Praktikum 3 - Algoritma Pemrograman
Studi Kasus: Sistem Simulasi Transaksi dan Validasi Akses Toko
NIM        : 2611531004
Catatan    : Seluruh variabel utama diakhiri dengan 4 digit terakhir NIM (_1004)
"""

# =========================================================
# DAFTAR PROMO YANG TERSEDIA DI TOKO
# =========================================================
daftar_promo_1004 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

print("=== SISTEM TRANSAKSI TOKO ===")

# =========================================================
# 1. INPUT DATA PELANGGAN (bukan nilai hardcode)
# =========================================================
nama_1004 = input("Masukkan Nama Pelanggan : ")
status_1004 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_1004 = float(input("Masukkan Total Belanja : "))
jumlah_1004 = int(input("Masukkan Jumlah Barang : "))
promo_1004 = input("Masukkan Kode Promo : ").strip().upper()

# =========================================================
# 2. OPERATOR PERBANDINGAN (comparison operator)
#    Menentukan apakah pelanggan memenuhi syarat diskon/promo
# =========================================================
syarat_belanja_1004 = total_1004 >= 200000      # True/False
syarat_barang_1004 = jumlah_1004 >= 3           # True/False
adalah_member_1004 = status_1004 == "member"    # True/False

# =========================================================
# 3. OPERATOR KEANGGOTAAN (membership operator: in / not in)
#    Mengecek apakah kode promo pelanggan valid
# =========================================================
promo_tersedia_1004 = promo_1004 in daftar_promo_1004
promo_tidak_dikenal_1004 = promo_1004 not in daftar_promo_1004

# =========================================================
# 4. OPERATOR LOGIKA (and, or, not)
#    Menggabungkan beberapa syarat sekaligus
# =========================================================
# Diskon member: pelanggan berstatus member DAN total belanja memenuhi syarat minimum
diskon_member_1004 = adalah_member_1004 and syarat_belanja_1004

# Promo didapat jika: (diskon member ATAU jumlah barang memenuhi syarat) DAN kode promo valid
dapat_promo_1004 = (diskon_member_1004 or syarat_barang_1004) and promo_tersedia_1004

# Contoh penggunaan "not": pelanggan non-member ditandai lewat negasi status member
bukan_member_1004 = not adalah_member_1004

# =========================================================
# 5. OPERATOR ARITMATIKA (+, -, *, /, %)
#    Menghitung besaran transaksi
# =========================================================
persen_diskon_1004 = 0.10 if dapat_promo_1004 else 0.0   # 10% jika dapat promo
diskon_1004 = total_1004 * persen_diskon_1004             # perkalian
subtotal_1004 = total_1004 - diskon_1004                  # pengurangan
ratarata_1004 = subtotal_1004 / jumlah_1004                # pembagian
sisabagi_1004 = jumlah_1004 % 3                            # modulus (sisa bagi jumlah barang oleh 3)

# =========================================================
# 6. OPERATOR PENUGASAN (assignment & augmented assignment)
#    Menghitung poin loyalitas dan ongkos kirim
# =========================================================
poin_1004 = 0
poin_1004 += jumlah_1004 * 10          # augmented assignment: tambah poin dari jumlah barang
if adalah_member_1004:
    poin_1004 += 20                    # bonus poin khusus member

ongkir_1004 = 15000
if promo_1004 == "GRATISONGKIR" and promo_tersedia_1004:
    ongkir_1004 -= 15000               # augmented assignment: ongkir jadi gratis

bayar_1004 = subtotal_1004
bayar_1004 += ongkir_1004              # augmented assignment: total akhir + ongkir

# =========================================================
# 7. OPERATOR IDENTITAS (is / is not)
#    Membedakan identitas objek vs kesamaan nilai (==)
# =========================================================
keranjang_a_1004 = [nama_1004, promo_1004]
keranjang_b_1004 = [nama_1004, promo_1004]   # objek baru, isi sama persis dengan keranjang_a
keranjang_c_1004 = keranjang_a_1004          # merujuk ke objek yang SAMA dengan keranjang_a

identitas_beda_objek_1004 = keranjang_a_1004 is keranjang_b_1004      # False -> objek berbeda
identitas_sama_objek_1004 = keranjang_a_1004 is keranjang_c_1004      # True  -> objek sama
nilai_sama_1004 = keranjang_a_1004 == keranjang_b_1004                # True  -> isi/nilai sama

# =========================================================
# 8. OPERATOR BITWISE (&, |, ^, <<)
#    Menyusun kode status transaksi 4-bit:
#    0001 = member | 0010 = belanja>=200rb | 0100 = barang>=3 | 1000 = promo tersedia
# =========================================================
bit_member_1004 = 0b0001 if adalah_member_1004 else 0b0000
bit_belanja_1004 = 0b0010 if syarat_belanja_1004 else 0b0000
bit_barang_1004 = 0b0100 if syarat_barang_1004 else 0b0000
bit_promo_1004 = 0b1000 if promo_tersedia_1004 else 0b0000

# OR (|) menggabungkan seluruh kondisi menjadi satu kode status transaksi
kode_status_1004 = bit_member_1004 | bit_belanja_1004 | bit_barang_1004 | bit_promo_1004

# AND (&) memeriksa apakah bit tertentu aktif (dipakai untuk hak akses)
cek_member_1004 = kode_status_1004 & 0b0001
cek_promo_1004 = kode_status_1004 & 0b1000

# XOR (^) membandingkan kode transaksi pelanggan dengan kode referensi toko
kode_referensi_1004 = 0b1011  # kode acuan: member + barang cukup + promo, tanpa syarat belanja
selisih_status_1004 = kode_status_1004 ^ kode_referensi_1004

# Bonus: left shift, menaikkan "level" kode status untuk keperluan logging internal
kode_shift_1004 = kode_status_1004 << 1

# Hak akses pelanggan ditentukan dari hasil operator bitwise di atas
member_access_1004 = cek_member_1004 != 0
promo_access_1004 = cek_promo_1004 != 0
free_shipping_access_1004 = (promo_1004 == "GRATISONGKIR") and promo_tersedia_1004

# =========================================================
# CETAK HASIL
# =========================================================
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan   : {nama_1004}")
print(f"Status Pelanggan : {status_1004}")
print(f"Total Belanja    : Rp{total_1004:.0f}")
print(f"Jumlah Barang    : {jumlah_1004}")
print(f"Kode Promo       : {promo_1004}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000       : {syarat_belanja_1004}")
print(f"Jumlah Barang >= 3        : {syarat_barang_1004}")
print(f"Status Member             : {adalah_member_1004}")
print(f"Kode Promo Tersedia       : {promo_tersedia_1004}")
print(f"Mendapatkan Diskon Member : {diskon_member_1004}")
print(f"Mendapatkan Promo         : {dapat_promo_1004}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                 : Rp{diskon_1004:.0f}")
print(f"Ongkos Kirim            : Rp{ongkir_1004:.0f}")
print(f"Total Pembayaran        : Rp{bayar_1004:.0f}")
print(f"Rata-rata Harga Barang  : Rp{ratarata_1004:.0f}")
print(f"Sisa Bagi (jumlah % 3)  : {sisabagi_1004}")
print(f"Poin Loyalitas          : {poin_1004}")

print("\n=== OPERATOR IDENTITAS (DEMO) ===")
print(f"keranjang_a is keranjang_b (objek beda)  : {identitas_beda_objek_1004}")
print(f"keranjang_a is keranjang_c (objek sama)  : {identitas_sama_objek_1004}")
print(f"keranjang_a == keranjang_b (nilai sama)  : {nilai_sama_1004}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{bin(bit_member_1004)[2:].zfill(4)} | {bin(bit_belanja_1004)[2:].zfill(4)} | "
      f"{bin(bit_barang_1004)[2:].zfill(4)} | {bin(bit_promo_1004)[2:].zfill(4)}")
print(f"Kode Biner  : {bin(kode_status_1004)[2:].zfill(4)}")
print(f"Kode Desimal: {kode_status_1004}")

print("\n=== Pemeriksaan Status (AND) ===")
print("Cek Member")
print(f"{bin(kode_status_1004)[2:].zfill(4)} & 0001")
print(f"Hasil Biner  : {bin(cek_member_1004)[2:].zfill(4)}")
print(f"Hasil Desimal: {cek_member_1004}")

print("\nCek Promo")
print(f"{bin(kode_status_1004)[2:].zfill(4)} & 1000")
print(f"Hasil Biner  : {bin(cek_promo_1004)[2:].zfill(4)}")
print(f"Hasil Desimal: {cek_promo_1004}")

print("\n=== Perbandingan Status (XOR) ===")
print(f"Kode Transaksi : {bin(kode_status_1004)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kode_referensi_1004)[2:].zfill(4)}")
print(f"{bin(kode_status_1004)[2:].zfill(4)} ^ {bin(kode_referensi_1004)[2:].zfill(4)}")
print(f"Hasil Biner  : {bin(selisih_status_1004)[2:].zfill(4)}")
print(f"Hasil Desimal: {selisih_status_1004}")

print("\n=== Shift (Bonus) ===")
print(f"{bin(kode_status_1004)[2:].zfill(4)} << 1")
print(f"Hasil Biner  : {bin(kode_shift_1004)[2:].zfill(5)}")
print(f"Hasil Desimal: {kode_shift_1004}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses       : {bin(kode_status_1004)[2:].zfill(4)}")
print(f"Member Access        : {member_access_1004}")
print(f"Promo Access         : {promo_access_1004}")
print(f"Free Shipping Access : {free_shipping_access_1004}")

print("\n=== SELESAI ===")