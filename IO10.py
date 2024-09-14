def HitungGradien(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def HitungTitikTengah(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def TegakLurus(x1, y1, x2, y2):
    m = HitungGradien(x1, y1, x2, y2)
    
    midpoint = HitungTitikTengah(x1, y1, x2, y2)
    
    gradien = -1 / m
    
    # y = mx+c
    intersep = midpoint[1] - gradien * midpoint[0]
    
    return gradien, intersep

x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

gradien, intersep = TegakLurus(x1, y1, x2, y2)

print(f"titik-titik asli adalah ({x1}, {y1}) dan ({x2}, {y2}).")
print(f"persamaan garis tegak lurusnya adalah y = {gradien:.2f}x + {intersep:.2f}")
