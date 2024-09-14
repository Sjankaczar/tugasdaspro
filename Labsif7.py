#STN
def check_number(N):
    # Memeriksa keberadaan digit 4 dalam string
    if '4' in N:
        return "SEVER"
    else:
        return "UNITE"

# Contoh input
N = input("Masukkan angka: ")

# Output hasil
print(check_number(N))