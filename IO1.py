#Menghitung ongkos taksi
odo_awal = float(input("masukkan angka odometer awal "))
odo_akhir = float(input("masukkan angka odometer akhir "))
jarak = odo_akhir - odo_awal
biaya = 1.5 * jarak
print("anda telah menempuh jarak sejauh", round(jarak, 1), "mil.", "pada harga $1.50 per mil, tagihan anda adalah $", round(biaya, 2))