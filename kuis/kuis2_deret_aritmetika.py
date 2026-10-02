print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi n
while n <= 0:
    print("Banyak suku harus lebih dari 0.")
    n = int(input("Banyak suku n: "))

# Menampilkan suku dan menghitung total
total = 0

for i in range(1, n + 1):
    suku = a + (i - 1) * d
    print(f"Suku ke-{i} = {suku}")
    total += suku

print(f"Jumlah = {total}")