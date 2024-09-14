population = int(input("Enter the community's population: "))

JumlahToilet = population / 3
AirHarianAwal = JumlahToilet * 15 * 14
AirHarianAkhir = JumlahToilet * 2 * 14
AirDihemat = AirHarianAwal - AirHarianAkhir
TotalHarga = JumlahToilet * 150

print(f"Air yang dihemat per hari: {AirDihemat:.2f} liter")
print(f"Total biaya untuk memasang semua toilet: ${TotalHarga:.2f}")
