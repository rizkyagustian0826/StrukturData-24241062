n = 3  # Jumlah baris

for i in range(n):
    # Cetak spasi di awal setiap baris
    for j in range(n - i - 1):
        print(" ", end="")
    # Cetak bintang
    for k in range(2 * i + 1):
        print("*", end="")
    # Pindah ke baris berikutnya
    print()