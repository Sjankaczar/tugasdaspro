# Constants
GRAVITASI = 9.80 
EFISIENSI = 0.90  
MASSA_JENIS = 1000  
MEGAWATT = 1e6  

tinggi = float(input("Masukkan tinggi bendungan dalam meter: "))
debit = float(input("masukkan debit air dalam meter kubik per sekon: "))

daya = MASSA_JENIS * debit * GRAVITASI * tinggi * EFISIENSI
daya_megawatts = daya / MEGAWATT

print(f"Daya yang dihasilkan adalah {daya_megawatts:.2f} Megawatt.")
