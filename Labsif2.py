#DTF

# Fungsi untuk mengonversi string waktu ke jam, menit, dan detik
def jadikan_HMS(waktu):
    h, m, s = map(int, waktu.split(':'))
    return h, m, s

# Fungsi untuk menghitung selisih waktu dalam detik
def HitungSelisihWaktu(WaktuAcara, WaktuSkrg):
    # Konversi waktu acara dan waktu saat ini ke jam, menit, dan detik
    J_Event, M_Event, D_event = jadikan_HMS(WaktuAcara)
    J_Skrg, M_Skrg, D_Skrg = jadikan_HMS(WaktuSkrg)
    
    # Konversi waktu acara dari GMT+2 ke GMT+7
    J_Event = (J_Event + 5) % 24
    
    # Hitung total detik untuk waktu acara dan waktu saat ini
    DetikEvent = J_Event * 3600 + M_Event * 60 + D_event
    DetikSkrg = J_Skrg * 3600 + M_Skrg * 60 + D_Skrg
    
    # Hitung selisih waktu dalam detik
    SelisihWaktu = DetikEvent - DetikSkrg
    
    # Jika selisih waktu negatif, Ali telah melewatkan acara
    if SelisihWaktu < 0:
        return "See you on the next Pear Event!"
    
    # Konversi selisih waktu ke jam, menit, dan detik
    BedaJam = SelisihWaktu // 3600
    BedaMenit = (SelisihWaktu % 3600) // 60
    BedaDetik = SelisihWaktu % 60
    
    return f"{BedaJam:02}:{BedaMenit:02}:{BedaDetik:02}"

# input
WaktuAcara = input("masukkan waktu acara (HH:MM:SS) =>")
WaktuSkrg = input("masukkan waktu sekarang (HH:MM:SS) =>")

# Hitung dan cetak waktu tunggu
print(HitungSelisihWaktu(WaktuAcara, WaktuSkrg))
