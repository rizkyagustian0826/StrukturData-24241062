# Meminta nama customer
nama_customer = str(input("Masukkan nama customer: "))

# Dictionary untuk menyimpan data customer
data_belanja = {}

# Menginput data untuk setiap customer
for i in range(nama_customer):
    print(f"\nbarang ke-{i+1}:")
    nama = input("  Masukkan Nama Barang: ")
    harga = input("  Masukkan Harga: ")
    jumlah = input(" Masukkan Total: ")
    
    daftar_blnj = int(input("  Masukkan daftar Belanja: "))
    daftar_blnj = []

    for j in range(daftar_blnj):
        barang = input(f"    Daftar Belanja Ke-{j+1}: ")
        harga = float(input(f"    Nilai untuk {blnj}: "))
        daftar_blnj.append((barang, harga, daftar_blnj))
    
    data_belanja[barang] = {
        "harga": harga,
        "daftar blnj": daftar_blnj
    }

# Menampilkan daftar belanja dan semua data customer
print("\nData customer dan daftar belanja:")
for barang, info in data_belanja.items():
    harga = info["harga"]
    daftar_blnj = info["daftar_bblnj"]
    rata_rata = sum([nilai for _, nilai in jumlah]) / len(jumlah)
    
    print(f"\nbarang: {barang}")
    print(f"harga: {harga}")
    print("customer dan jumlah belanja:")
    for blnj, jumlah in daftar_blnj:
 print(f"  - {blnj}: {blnj}")
    print(f"daftar_blnj: {jumlah:.2f}")