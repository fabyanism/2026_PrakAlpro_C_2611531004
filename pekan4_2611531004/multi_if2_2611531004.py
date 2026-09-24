# Buat file dengan nama multi_if1_261531004.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1004
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_1004 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1004 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_1004 = input_member_1004 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_1004 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1004 = input_promo_1004 in ["y", "ya"]

total_diskon_persen_1004 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi syarat sekaligus

if total_belanja_1004 > 1000000:
    total_diskon_persen_1004 += 10 # Diskon belanja besar

if is_member_1004:
    total_diskon_persen_1004 += 5 # Diskon member

if kode_promo_valid_1004:
    total_diskon_persen_1004 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_1004 = total_belanja_1004 * (total_diskon_persen_1004 / 100)
total_bayar_1004 = total_belanja_1004 - nominal_diskon_1004

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon    : {total_diskon_persen_1004}% (Rp {nominal_diskon_1004:,.0f})")
print(f"Total Bayar     : Rp {total_bayar_1004:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_1004}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid