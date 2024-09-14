def calculate_charges(data_usage):
    if data_usage <= 0:
        return "Data salah. Penggunaan data harus lebih dari 0"
    elif data_usage <= 1:
        charges = 250
    elif data_usage <= 2:
        charges = 500
    elif data_usage <= 5:
        charges = 1000
    elif data_usage <= 10:
        charges = 1500
    else:
        charges = 2000

    return f"Biaya: {charges}"

# Example usage
try:
    data_usage = float(input("Masukkan data yang digunakan (Gbs): "))
    result = calculate_charges(data_usage)
except ValueError:
    result = "Data Salah. Mohon berikan angka yang benar"

print(result)