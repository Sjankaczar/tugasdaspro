#MA
def LampuMerah(M, N, T):
    # Durasi lampu lalu lintas
    red_duration = 20
    yellow_duration = 5
    green_duration = 60
    SiklusDurasi = red_duration + yellow_duration + green_duration
    
    # Hitung berapa banyak mobil yang bisa lewat dalam waktu T detik
    green_time = T % SiklusDurasi
    if green_time > red_duration + yellow_duration:
        green_time -= (red_duration + yellow_duration)
    else:
        green_time = 0
    
    SiklusHijau = 0
    if T//SiklusDurasi>0:
        SiklusHijau += (T // SiklusDurasi) * green_duration

    cars_passed = ((SiklusHijau + green_time) // 5) 
    
    # Hitung jumlah mobil yang tersisa
    remaining_cars = M - cars_passed + 1
    if remaining_cars <= 0:
        return f"YES! {max(0, N + remaining_cars)}"
    else:
        return f"NO! {N + remaining_cars}"

# Contoh input
M, N, T = map(int, input("masukkan M, N, T (angka hanya dipisah spasi) =>").split())
print(LampuMerah(M, N, T))  