"""
Tugas Praktikum 4 - Algoritma Pemrograman
Studi Kasus: Sistem Loket Terpadu & Audit Transaksi Ekspedisi Wahana
Nama    : Fabian Alhadi Zalinov
NIM     : 2611531004
Kelas   : C
"""

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung & String Handling
nama_1004 = input("Masukkan Nama Pengunjung : ")
umur_1004 = int(input("Input umur anda : "))
sim_1004 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

# 2. Pemilihan Wahana menggunakan match-case (case 1-5 dan default _)
print("Pilihan Paket Wahana (1-5):")
print("1. Safari Rimba (Rp 50,000)")
print("2. Arung Jeram (Rp 75,000)")
print("3. Motor ATV Ekstrim (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP (Rp 220,000)")
paket_1004 = int(input("Masukkan nomor paket (1-5) : "))

match paket_1004:
    case 1:
        nama_wahana_1004 = "Wahana Safari Rimba"
        harga_satuan_1004 = 50000
    case 2:
        nama_wahana_1004 = "Wahana Arung Jeram"
        harga_satuan_1004 = 75000
    case 3:
        nama_wahana_1004 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1004 = 120000
    case 4:
        nama_wahana_1004 = "Wahana Roller Coaster Kilat"
        harga_satuan_1004 = 100000
    case 5:
        nama_wahana_1004 = "Wahana All-Access VIP"
        harga_satuan_1004 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

jumlah_tiket_1004 = int(input("Masukkan jumlah tiket : "))

# Validasi kelogisan jumlah tiket (if tunggal)
if jumlah_tiket_1004 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
    exit()

is_member_1004 = input("Apakah Anda member? (y/t) : ").strip().lower()
kode_promo_valid_1004 = input("Apakah kode promo valid? (y/t) : ").strip().lower()

# 3. Validasi Izin Kendali Wahana (if-elif-else dengan operator logika)
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_1004 == 3:
    if umur_1004 >= 17 and sim_1004 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_1004 >= 17 and sim_1004 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_1004 < 17 and sim_1004 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_1004 >= 10:
        print(f"Status Akses: Anda memenuhi syarat umur untuk mengikuti {nama_wahana_1004}.")
    else:
        print(f"Status Akses: Maaf, Anda belum memenuhi syarat umur minimal untuk {nama_wahana_1004}.")

# 4. Akumulasi Diskon Bertingkat menggunakan Multi-IF terpisah
subtotal_1004 = harga_satuan_1004 * jumlah_tiket_1004
total_diskon_persen_1004 = 0

if subtotal_1004 >= 200000:
    total_diskon_persen_1004 += 10  # Diskon Belanja Besar

if is_member_1004 in ['y', 'ya']:
    total_diskon_persen_1004 += 5  # Diskon Member

if kode_promo_valid_1004 in ['y', 'ya']:
    total_diskon_persen_1004 += 15  # Diskon Voucher Promo

if jumlah_tiket_1004 >= 5:
    total_diskon_persen_1004 += 5  # Diskon Tambahan Rombongan

nominal_diskon_1004 = subtotal_1004 * (total_diskon_persen_1004 / 100)
total_bayar_1004 = subtotal_1004 - nominal_diskon_1004

# 5. Evaluasi Kelulusan Audit (if-else)
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_1004:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_1004}% (Rp {nominal_diskon_1004:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_1004:,.0f}")

if total_bayar_1004 > 300000:
    print("Catatan Layanan : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan : Terima kasih telah berkunjung.")

print("Program Selesai")