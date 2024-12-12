Apa itu Polimorfisme dalam Python?

Istilah polimorfisme mengacu pada fungsi atau metode yang mengambil bentuk berbeda dalam konteks berbeda. Karena Python adalah bahasa bertipe dinamis, polimorfisme dalam Python sangat mudah diimplementasikan.

Jika suatu metode pada kelas induk ditimpa dengan logika bisnis yang berbeda pada berbagai kelas anaknya, metode kelas dasar adalah metode polimorfik.

Cara menerapkan Polimorfisme dalam Python
Ada empat cara untuk mengimplementasikan polimorfisme di Python −
•	Duck Typing
     >Duck Typing adalah konsep yang  menganggap tipe atau kelas suatu objek kurang penting daripada metode yang didefinisikannya. Dengan konsep ini, Anda dapat memanggil metode apa pun pada suatu objek tanpa memeriksa tipenya, selama metode tersebut ada.
     Istilah ini didefinisikan oleh kutipan yang sangat terkenal yang menyatakan: Misalkan ada seekor burung yang berjalan seperti bebek, berenang seperti bebek, tampak seperti bebek, dan gemetar seperti bebek, maka kemungkinan besar itu adalah bebek.
     >Contoh
     Dalam kode yang diberikan di bawah ini, kami secara praktis mendemonstrasikan konsep duck typing.

     class Duck:
         def sound(self):
             return "Quack, quack!"
  
     class AnotherBird:
         def sound(self):
             return "I'm similar to a duck!"

     def makeSound(duck):
         print(duck.sound())

     When you execute this code# creating instances
     duck = Duck()
     anotherBird = AnotherBird()
     # calling methods
     makeSound(duck)   
     makeSound(anotherBird) 

     Output :
     Quack, quack!
     I'm similar to a duck!

•	Operator Overloading
     >Misalkan Anda telah membuat kelas Vector untuk merepresentasikan vektor dua dimensi, apa yang terjadi ketika Anda menggunakan operator plus untuk menambahkannya? Kemungkinan besar Python akan membentak Anda.
     Namun, Anda bisa mendefinisikan__menambahkan__metodedi kelas Anda untuk melakukan penjumlahan vektor dan kemudian operator plus akan berperilaku sesuai harapan −
     >Contoh :
      class Vector:
         def __init__(self, a, b):
             self.a = a
             self.b = b

         def __str__(self):
             return 'Vector (%d, %d)' % (self.a, self.b)
   
         def __add__(self,other):
             return Vector(self.a + other.a, self.b + other.b)

      v1 = Vector(2,10)
      v2 = Vector(5,-2)
      print (v1 + v2)

      Output:
      Vector(7,8)

•	Method Overloading
     >Ketika suatu kelas memuat dua atau lebih metode dengan nama sama tetapi jumlah parameter berbeda maka skenario ini dapat disebut sebagai kelebihan beban metode.
     Python tidak mengizinkan kelebihan muatan metode secara default, namun, kita dapat menggunakan teknik seperti daftar argumen dengan panjang variabel, beberapa dispatch dan parameter default untuk mencapainya.
     >Contoh:
      Dalam contoh berikut, saya menggunakan daftar argumen dengan panjang variabel untuk mencapai kelebihan beban metode.

      def add(*nums):
         return sum(nums)

     # Call the function with different number of parameters
     result1 = add(10, 25)
     result2 = add(10, 25, 35)

     print(result1)  
     print(result2) 

     Output:
     35
     70

•	Method Overriding
     >Di dalam method overriding, suatu metode yang didefinisikan di dalam subkelas mempunyai nama yang sama dengan metode di superkelasnya tetapi mengimplementasikan fungsionalitas yang berbeda.
     >Contoh
      Sebagai contoh polimorfisme yang diberikan di bawah ini, kita memilikimembentukyang merupakan kelas abstrak. Kelas ini digunakan sebagai induk oleh dua kelas yaitu circle dan rectangle. Kedua kelas tersebut mengganti metode draw() induknya dengan cara yang berbeda.

      from abc import ABC, abstractmethod
      class shape(ABC):
         @abstractmethod
         def draw(self):
             "Abstract method"
             return

      class circle(shape):
         def draw(self):
             super().draw()
             print ("Draw a circle")
             return

      class rectangle(shape):
         def draw(self):
             super().draw()
             print ("Draw a rectangle")
             return

      shapes = [circle(), rectangle()]
      for shp in shapes:
         shp.draw()

      Output :
      Draw a circle
      Draw a rectangle   

      Variabel shp first merujuk ke objek lingkaran dan memanggil metode draw() dari kelas lingkaran. Pada iterasi berikutnya, merujuk ke objek persegi panjang dan memanggil metode draw() dari kelas persegi panjang. Oleh karena itu metode draw() dalam kelas shape bersifat polimorfik.


Class Polymorphism

Polimorfisme sering digunakan dalam metode Kelas, di mana kita dapat memiliki beberapa kelas dengan nama metode yang sama.

Misalnya, kita memiliki tiga kelas:Car,Boat, Dan Plane, dan mereka semua memiliki metode yang disebut bergerak():

Contoh
Kelas yang berbeda dengan metode yang sama:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

Output:

Drive!
Sail!
Fly!  


TUGAS 3 :

Cuplikan polimorfisme dalam kode:

def decrypt(self):
    self.calculate_sum_of_digits()  # Memanggil metode calculate_sum_of_digits()
    ...
    self.collect_letters()  # Memanggil metode collect_letters()

    shift = self.sum_digits % 26  # Menghindari pergeseran lebih dari 26
    decrypted_letters = []

    for letter in self.letters:
        if letter.islower():  # Pengecekan apakah huruf kecil
            new_char = chr((ord(letter) - ord('a') - shift) % 26 + ord('a'))  # Geser huruf kecil
        else:  # Pengecekan apakah huruf besar
            new_char = chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))  # Geser huruf besar
        decrypted_letters.append(new_char)

    return ''.join(decrypted_letters)

Penjelasan terkait polimorfisme:
1. Polimorfisme dalam Metode decrypt:
> Metode decrypt bergantung pada dua metode lain yang didefinisikan di kelas yang sama, yaitu calculate_sum_of_digits dan collect_letters. Meskipun keduanya metode dengan nama yang berbeda, keduanya berkontribusi pada proses dekripsi yang sama. Dalam hal ini, polimorfisme terlihat dalam cara berbagai metode menangani bagian yang berbeda dari proses dekripsi.
2. Penerapan Polimorfisme pada Pengolahan Karakter Huruf:
> Pada loop for letter in self.letters:, proses penggeseran huruf dilakukan berbeda tergantung apakah huruf tersebut huruf kecil (islower()) atau huruf besar. Ini adalah bentuk polimorfisme, di mana dua tipe data yang berbeda (islower() vs isupper()) diperlakukan dengan cara yang berbeda dalam satu blok kode yang sama. Meski cara perlakuannya berbeda, mereka tetap menggunakan nama metode yang sama (new_char = chr(...)) untuk menghasilkan hasil akhir.



TUGAS 4 :

Cuplikan Polimorfisme dalam Kode

try:
    self.read_file()  # Memanggil metode read_file
    if not self.lines:
        self.write_null()  # Jika file kosong, panggil write_null
    else:
        self.calculate_stats()  # Menghitung statistik jika file tidak kosong
        self.write_output()  # Menulis output ke file
except FileNotFoundError:
    print("File tidak ditemukan :(")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
else:
    print(f"Output berhasil ditulis pada {self.filename}")
finally:
    input("Program selesai. Tekan enter untuk keluar...")

Polimorfisme dalam Metode yang Sama
1. Metode read_file, write_null, write_output:
> Dalam kelas IOException, kita memanggil beberapa metode yang berbeda seperti read_file, write_null, calculate_stats, dan write_output. Polimorfisme di sini bisa dipahami sebagai penanganan situasi yang berbeda dengan menggunakan metode yang sesuai. Meskipun kita mengelola file yang sama, kita memanfaatkan berbagai metode untuk menangani file yang kosong atau berisi, serta untuk menulis output.
> Contoh:
  -Jika file kosong (if not self.lines), kita memanggil write_null, yang akan menulis 'NULL' ke dalam file.
  -Jika file tidak kosong, kita memanggil calculate_stats untuk menghitung statistik, kemudian menulis hasilnya dengan write_output.
Meskipun ini bukan contoh polimorfisme dalam arti pewarisan objek, ini adalah perbedaan perilaku tergantung kondisi, yang serupa dengan prinsip polimorfisme dalam cara menangani file atau data yang berbeda.

2. Polimorfisme dengan Exception Handling:
> Pada bagian try-except, terdapat penanganan kesalahan yang berbeda untuk berbagai jenis kesalahan. Ini bisa dianggap sebagai bentuk polimorfisme dalam penanganan pengecualian. Terdapat dua jenis pengecualian yang ditangani:
  - FileNotFoundError jika file tidak ditemukan.
  - Exception untuk kesalahan umum lainnya.
Setiap jenis pengecualian ditangani dengan cara yang berbeda, tetapi menggunakan struktur pengecualian yang sama, yaitu try-except. Ini juga bisa dianggap sebagai polimorfisme dalam penanganan kesalahan yang beragam.

