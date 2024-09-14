#Heat delivered to a house
galon = float(input("berapa galon minyak yang digunakan? "))
efis = float(input("berapa persenkah efisiensinya? "))
BTU = (efis / 100.0) * (galon * 5800000.0 / 42.0)
print("panas yang dialirkan menuju rumah dalam BTU adalah" ,round(BTU, 2) ,"BTU")