servis = int(input("(1) Servis gratis pertama \n(2) Servis gratis kedua \nMasukkan nomor servis gratis>>"))
jarak = int(input("masukkan angka mil>>"))
if servis == 1:
    if jarak > 1500 and jarak <= 3000:
        print("kendaraan harus diservis")
    else:
        print("kendaraan tidak bisa diservis gratis pertama")
elif servis == 2:
    if jarak > 3000 and jarak <= 4500:
        print("kendaraan harus diservis")
    else:
        print("kendaraan tidak bisa diservis gratis kedua")
else:
    print("kendaraan tidak bisa diservis gratis")