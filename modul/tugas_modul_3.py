class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, kapasitas):
        self.top = None
        self.kapasitas = kapasitas
        self.ukuran = 0

    def is_empty(self):
        return self.ukuran == 0

    def is_full(self):
        return self.ukuran == self.kapasitas

    def push(self, data):
        if self.is_full():
            return False
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.ukuran += 1
        return True

    def pop(self):
        if self.is_empty():
            return None
        removed = self.top.data
        self.top = self.top.next
        self.ukuran -= 1
        return removed

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def get_size(self):
        return self.ukuran

    def get_all_elements(self):
        current = self.top
        result = []
        while current:
            result.insert(0, current.data)  # Menambahkan ke depan agar urut dari bawah ke atas
            current = current.next
        return result

# ====== Fungsi Operasi Stack ======

def tambah_elemen(stack):
    while True:
        data = input("Masukkan isi stack : ")
        if not stack.push(data):
            print("Stack sudah penuh!")
            break
        print("Stack :", stack.get_all_elements())
        lanjut = input("\nMenambah isi Stack Pilih [Ya/Tidak] : ").lower()
        if lanjut != "ya":
            break

def hapus_elemen(stack):
    removed = stack.pop()
    if removed is None:
        print("Stack kosong, tidak bisa menghapus.")
    else:
        print(f"Elemen '{removed}' berhasil dihapus.")
        print("Stack :", stack.get_all_elements())

def cek_ukuran(stack):
    print("Ukuran stack saat ini :", stack.get_size())

def cek_puncak(stack):
    top = stack.peek()
    if top is None:
        print("Stack kosong.")
    else:
        print("Elemen puncak stack adalah :", top)

def cek_penuh(stack):
    if stack.is_full():
        print("Stack dalam kondisi penuh.")
    else:
        print("Stack masih memiliki ruang.")

# ====== Program Utama ======

def main():
    print("=====PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST=====")
    kapasitas = int(input("Tentukan berapa kapasitas stack : "))
    stack = Stack(kapasitas)

    while True:
        print("\nPilih menu berikut ini :")
        print("1. Menambah isi stack")
        print("2. Menghapus isi stack")
        print("3. Cek Ukuran Stack saat ini")
        print("4. Cek Puncak Stack")
        print("5. Cek Stack Full")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan anda : ")

        if pilihan == "1":
            tambah_elemen(stack)
        elif pilihan == "2":
            hapus_elemen(stack)
        elif pilihan == "3":
            cek_ukuran(stack)
        elif pilihan == "4":
            cek_puncak(stack)
        elif pilihan == "5":
            cek_penuh(stack)
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main ()