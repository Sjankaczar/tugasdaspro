
def identify_substance(temperatur):
    # Dictionary of substances and their normal boiling points
    boiling_points = {
        "Water": 100,
        "Mercury": 357,
        "Copper": 1187,
        "Silver": 2193,
        "Gold": 2660
    }

    # Check each substance to see if the observed boiling point is within 5% of the expected boiling point
    for substance, normal_boiling_point in boiling_points.items():
        lower_bound = normal_boiling_point * 0.95
        upper_bound = normal_boiling_point * 1.05
        if lower_bound <= temperatur <= upper_bound:
            return f"zat tersebut adalah {substance}."

    return "zat tidak diketahui"

banyak = int(input("berapa banayk zat yang ingin diidentifikasi"))
for i in range(0, banyak):
    titikdidih = (float(input("masukkan titik didih yang diamati (C)")))
    print(identify_substance(titikdidih))
# Example usage
#try:

    #result = identify_substance(obs, banyak)
    #print(result)
#except ValueError:
    #print("Input Invalid")
