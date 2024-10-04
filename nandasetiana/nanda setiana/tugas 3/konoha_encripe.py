class Konoha:
   # constructor    
   def __init__(self, nama, angka):
      self.nama = nama
      self.angka = angka

def dekripsi(input_str):
    # Menjumlahkan semua angka
    total_pergeseran = sum(int(char) for char in input_str if char.isdigit())  
    hasil = []

    for char in input_str:
        # Jika karakter adalah alfabet
        if char.isalpha(): 
            geser = chr((ord(char.lower()) - ord('a') + total_pergeseran) % 26 + ord('a'))
            hasil.append(geser)

    return ''.join(hasil)

# Contoh penggunaan
input_str = "n2an1d1a"
output = dekripsi(input_str)
print(output)