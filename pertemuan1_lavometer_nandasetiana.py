import random
print("SELAMAT DATANG DI LAVOMETER")
nama_dia = "Kayra Rahmadhini"
cocok = random.random()
print("Kecocokan anda", cocok * 100, "%")
if cocok > 0.8:
    print("Anda sangat cocok dengan " + nama_dia + nama_dia + "!")
elif 0.5 <= cocok <= 0.8:
    print("Anda lumayan cocok dengan " + nama_dia + nama_dia + "!")
else:
    print("Anda tidak cocok dengan " + nama_dia + nama_dia + "!")