n = int(input("Masukkan jumlah deret: "))
a, b = 1, 2
jumlah = 0

for i in range(n):
    print(a)
    jumlah += a
    a, b = b, a + b

print("Jumlah total:", jumlah)