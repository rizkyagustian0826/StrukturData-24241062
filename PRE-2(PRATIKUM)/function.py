# membuat function sederhana
def sapa():
    print("Halo, selamat datang!")

sapa()  # Memanggil fungsi ke 1 
sapa()  # Memanggil fungsi ke 2
sapa()  # Memanggil fungsi ke 3

# function dengan 1 parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

# Pemanggilan Function
sapa_nama("azian")
sapa_nama("febri")

# function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)

# Pemanggilan Function
luas_segitiga(4, 6)


# fungsi digunakan di dalam fungsi lainnya
# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
vol_persegi = volume_persegi(6)
print(f"Volume Persegi = {vol_persegi}")

def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')
    # pemanggilan function, dengan 1 argumen
student("Wallberg")

# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')  

nama = "azian"  # variabel global

def sapa():
    print("Halo,", nama)

# memanggil function
sapa()


# Fungsi untuk menampilkan semua data buku
def show_data():
    if len(buku) <=0 :
        print("DATA BUKU BELUM ADA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))
def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)        
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID Buku : "))
    if(indeks > len(buku)):
        print("ID Buku Tidak Ditemukan")
    else:
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID Buku : "))
    if(indeks > len(buku)):
        print("ID Buku Tidak Ditemukan")
    else:
        buku.remove(buku[indeks])
        print(f"Buku dengan ID {indeks} Terhapus")                