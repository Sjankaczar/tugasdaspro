Vtakeoff = float(input("Masukkan kecepatqan Jet saat takeoff dalam km/h: "))
jarak = float(input("Masukkan jarak ketapel mengakselerasikan jet dalam meter: "))

KecepatanTakeoff = Vtakeoff * (1000 / 3600)

# v^2 = 2as
Akselerasi = (KecepatanTakeoff ** 2) / (2 * jarak)

#  v = at
time = KecepatanTakeoff / Akselerasi

print(f"Akselerasi: {Akselerasi:.2f} m/s^2")
print(f"Waktu untuk takeoff: {time:.2f} sekon")
