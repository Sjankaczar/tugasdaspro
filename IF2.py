berat = float(input("masukkan berat dalam pon "))
tinggi = float(input("masukkan tinggi dalam inchi"))
BMI = 703*berat/(tinggi**2)
BMI = round(BMI, 1)

if BMI < 18.5:
    print("kurus")
elif BMI > 18.5 and BMI < 24.9:
    print("normal")
elif BMI > 25.0 and BMI < 29.9:
    print("gemuk")
else:
    print("obesitas")