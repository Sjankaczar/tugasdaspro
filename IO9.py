#Time required to cut grass
halaman = float(input("panjang halaman (ft): ")) * float(input("lebar halaman (ft): "))
rumah = float(input("panjang rumah di dalam halaman (ft): ")) * float(input("lebar rumah di dalam halaman (ft): "))
rumput = halaman - rumah
waktu = rumput / 2
print("waktu yang dibutuhkan untuk memotong rumput adalah" ,waktu ,"detik atau" ,waktu / 60.0 , "menit")