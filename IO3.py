#Estimasi temperatur dalam kulkas setelah mati listrik
jam = float(input("kulkas mati selama ... jam "))
menit = float(input("dan ... menit "))

menits = menit / 60.0
waktu = jam + menits
Temperatur = (4.0 * (waktu ** 2.0) / (waktu + 2.0)) - 20.0

print("Estimasi temperatur setelah kulkas mengalami mati listrik adalah", round(Temperatur, 1), "C")