print("=== PROGRAM KASIR SEDERHANA ===")

# Input data pembeli
nama_pembeli = input("Nama Pembeli : ")
jumlah_jenis = int(input("Jumlah jenis barang : "))

total_belanja = 0

# Perulangan untuk memasukkan data barang
for i in range(1, jumlah_jenis + 1):
    print(f"\nBarang ke-{i}")

    nama_barang = input("Nama   : ")
    harga = int(input("Harga  : "))
    jumlah = int(input("Jumlah : "))

    subtotal = harga * jumlah
    total_belanja += subtotal

# Menentukan diskon
if total_belanja >= 500000:
    diskon = 15
elif total_belanja >= 250000:
    diskon = 10
elif total_belanja >= 100000:
    diskon = 5
else:
    diskon = 0

# Menghitung potongan dan total bayar
potongan = total_belanja * diskon / 100
total_bayar = total_belanja - potongan

# Menampilkan struk
print("\n========== STRUK ==========")
print(f"Pembeli       : {nama_pembeli}")
print(f"Total Belanja : Rp{total_belanja:.0f}")
print(f"Diskon        : {diskon}%")
print(f"Potongan      : Rp{potongan:.0f}")
print(f"Total Bayar   : Rp{total_bayar:.0f}")
print("===========================")