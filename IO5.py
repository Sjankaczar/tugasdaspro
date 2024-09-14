#Laju penginfusan
volum = float(input("volume infus (ml) ... "))
mnt = float(input("waktu penginfusan (menit) ... "))
laju_infus =  volum / mnt * 60.0
print("volume infus:" ,round(volum) , "ml")
print("Laju infus: " ,round(laju_infus) ,"ml/jam")