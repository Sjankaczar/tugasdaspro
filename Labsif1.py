#TWR
def cat_jumps(a, b, c, index):
    # Jumlah lompatan efektif (karena pola akan berulang setiap 7 lompatan)
    effective_jumps = c % 7
    
    # Lakukan lompatan kucing
    for _ in range(effective_jumps):
        a = a[-b:] + a[:-b]
    
    # Ambil nilai pada indeks yang diminta
    result = [a[index[0]], a[index[1]], a[index[2]]]
    return result

a = list(map(int, input("masukkan 7 angka =>").split()))
b = int(input("masukkan jumlah kucing yang melompat =>"))
c = int(input("masukkan banyaknya kucing melompat =>"))
index = list(map(int, input("masukkan indeks =>").split()))
print(cat_jumps(a, b, c, index))  

# Contoh input
# angka = [1, 2, 3, 4, 5, 6, 7]
# jumlah kucing melompat = 3
# banyak lompatan = 3
# index = [0, 3, 5]

# Output
# print(cat_jumps(a, b, c, index))  # Output: [6, 2, 4]
