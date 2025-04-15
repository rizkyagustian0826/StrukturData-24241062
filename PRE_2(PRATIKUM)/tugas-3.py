n = int(input("Masukkan jumlah deret: "))
a, b = 1, 1
jumlah = 0

for i in range(10):
    print(a)
    jumlah += a
    a, b = b, a + b

print("Jumlah total:", jumlah)
