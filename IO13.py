#Student batch
siswa = int(input("masukkan jumlah siswa yang terdaftar: "))
kelompok = siswa // 30
tersisa = siswa % 30

print("siswa yang terdaftar: ", siswa, "\nsesi yang dibutuhkan:", kelompok, "\nsiswa yang tersisa:", tersisa)