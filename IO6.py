grade = input("masukkan nilai yang diinginkan: ")
min = float(input("masukkan minimal rata-rata yang dibutuhkan: "))
NilaiSkrg = float(input("masukkan rata-rata ujian anda: "))
persen = int(input("masukkan berapa persen penilaian ujian akhir terhadap seluruh nilai: "))

jumlah = 100 // persen
penilaian = min*jumlah - NilaiSkrg*(jumlah-1)

print(f"anda membutuhkan skor {penilaian:.2f} pada ujian akhir untuk mendapat nilai {grade}.")