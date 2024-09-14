#GP
def can_b_jump(distances):
    # Ambil nilai maksimum lompatan B dari input
    max_jump = distances[0]
    
    # Periksa setiap jarak antar pilar
    for distance in distances[1:]:
        if distance > max_jump:
            return "NO HE CAN'T"
    
    return "YES HE CAN"

# Ubah input menjadi daftar jarak
distances = list(map(int, input("masukkan input=>").split()))

# Panggil fungsi dan cetak hasilnya
print(can_b_jump(distances))

