print("Nama : Nanda Setiana")
print("Nim : 2355201031")

print("### MY TACTICAL DOLL###")
nama_tactical_doll = input("Masukkan Nama Tactical Doll mu : ")
firepower = int(input("Damage Firepower : "))
rate_of_fire = int(input("Jumlah Rate Of Fire : "))
accuracy = int(input("Jumlah Accuracy : "))
evasion = int(input("Masukkan Evasion : "))
damage_per_second = round(firepower * rate_of_fire/60,2)
combat_effectiveness = int(30 * float(firepower) + (40 * (float(rate_of_fire) **2)/120) + (15 *(accuracy+evasion)))

print ("### ENEMY TACTICAL DOLL ###")
nama_tactical_doll_2 = input("Masukkan Nama Tactical Doll 2 : ")
firepower_2 = input("Damage Firepower 2 : ")
rate_of_fire_2 = input("Jumlah Rate Of Fire 2 : ")
accuracy_2 = input("Jumlah Accuracy 2 : ")
evasion_2 = input("Masukkan Evasion 2 : ")
damage_per_second_2 = round(float(firepower_2) * float(rate_of_fire_2)/60,2)
combat_effectiveness_2 = int(30 * float(firepower_2) + (40 * (float(rate_of_fire_2)** 2)/120)
                                  + 15 * (float(accuracy_2) + float(evasion_2)))

power_doll = damage_per_second + combat_effectiveness
power_doll_2 = damage_per_second_2 + combat_effectiveness_2

print("### RESULT ###")
print(nama_tactical_doll)
print("Damage Per Second : " + str(damage_per_second))
print("Combat Effecttiveness : " + str(combat_effectiveness))
print(nama_tactical_doll_2)
print("Damage Per Second : " + str (damage_per_second_2 ))
print("Combat Effecttiveness : " + str(combat_effectiveness_2))

if power_doll > power_doll_2:
    print ("Keputusan : GOODJOB!!")
elif power_doll < power_doll_2: 
    print ("Keputusan : YUHUUUU")
else :
    print ("TETAP SEMANGATT")