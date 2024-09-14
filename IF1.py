TotalBelanja = float(input("berapa dollar total belanja anda? "))
Pelajar = input("apakah anda pelajar atau tidak? ")
Pelajar = Pelajar.lower()

print(f"Total Belanja           ${TotalBelanja:.2f}")
if 'y' in Pelajar:
    DisPel = TotalBelanja / 5
    DisPelTotal = TotalBelanja - DisPel
    Pajak = DisPelTotal / 20
    Total = Pajak + DisPelTotal
    print(f"Diskon pelajar (20%)      {DisPel:.2f}")
    print(f"Total Terdiskon           {DisPelTotal:.2f}")
    print(f"Pajak Belanja              {Pajak:.2f}")
    print(f"Total                   ${Total:.2f}")
elif 'ak' in Pelajar:
    Pajak = TotalBelanja / 20
    Total = Pajak + TotalBelanja
    print(f"Pajak Belanja             {Pajak:.2f}")
    print(f"Total                   ${Total:.2f}")
