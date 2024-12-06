Pewarisan Python

Pewarisan memungkinkan kita mendefinisikan kelas yang mewarisi semua metode dan properti dari kelas lain.

>Kelas induk adalah kelas yang diwarisi, disebut juga kelas dasar.

>Kelas anak adalah kelas yang mewarisi dari kelas lain, disebut juga kelas turunan.

>Buat Kelas Induk
Kelas apa pun bisa menjadi kelas induk, jadi sintaksnya sama dengan membuat kelas lainnya:

Contoh :
Buat kelas bernama Person, dengan properti dan firstnamemetode :lastnameprintname

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

>Buat Kelas Anak
Untuk membuat kelas yang mewarisi fungsionalitas dari kelas lain, kirimkan kelas induk sebagai parameter saat membuat kelas anak:

Contoh
Buat kelas bernama Student, yang akan mewarisi properti dan metode dari Personkelas:

class Student(Person):
  pass

Sekarang kelas Student memiliki properti dan metode yang sama dengan kelas Person.

Contoh
Gunakan Studentkelas untuk membuat objek, lalu jalankan printnamemetode:

x = Student("Mike", "Olsen")
x.printname()


>Tambahkan Fungsi __init__()
Sejauh ini kita telah membuat kelas anak yang mewarisi properti dan metode dari induknya.

Menambahkan __init__()fungsi ke kelas anak (bukan passkata kunci).

Catatan: Fungsi ini __init__()dipanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru.

Contoh
Tambahkan __init__()fungsi ke Studentkelas:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

Ketika Anda menambahkan __init__()fungsi tersebut, kelas anak tidak akan lagi mewarisi fungsi induknya __init__().

Untuk mempertahankan pewarisan __init__() fungsi induk, tambahkan panggilan ke fungsi induk __init__():

Contoh
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

Sekarang kita telah berhasil menambahkan __init__()fungsi tersebut, dan mempertahankan warisan kelas induk, dan kita siap untuk menambahkan fungsionalitas ke dalam __init__()fungsi tersebut.


>Gunakan Fungsi super()
Python juga memiliki super()fungsi yang akan membuat kelas anak mewarisi semua metode dan properti dari induknya:

Contoh
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

Dengan menggunakan super()fungsi tersebut, tidak perlu menggunakan nama elemen induk, maka secara otomatis akan mewarisi metode dan properti dari induknya.


>Tambahkan Properti
Contoh
Tambahkan properti yang disebut graduationyearke Studentkelas:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

Dalam contoh di bawah ini, tahun 2019harus berupa variabel, dan dimasukkan ke dalam Studentkelas saat membuat objek siswa. Untuk melakukannya, tambahkan parameter lain dalam __init__()fungsi:

Contoh
Tambahkan yearparameter, dan masukkan tahun yang benar saat membuat objek:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


>Tambahkan Metode
Contoh
Tambahkan metode yang dipanggil welcomeke Studentkelas:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
Jika Anda menambahkan metode di kelas anak dengan nama yang sama dengan fungsi di kelas induk, pewarisan metode induk akan ditimpa.


>Implementasi

Berikut adalah contoh sederhana yang menunjukkan implementasi inheritance berdasarkan penjelasan sebelumnya. Saya akan membuat dua kelas:

Kelas induk Person, yang memiliki properti dasar seperti nama depan dan nama belakang.
Kelas anak Student, yang mewarisi properti dan metode dari Person serta menambahkan fungsionalitas tambahan.
Contoh Kode dengan Inheritance

# Kelas induk
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"Nama lengkap: {self.firstname} {self.lastname}")

# Kelas anak
class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        # Mewarisi __init__() dari kelas induk
        super().__init__(fname, lname)
        self.graduationyear = graduationyear  # Properti tambahan

    def welcome(self):
        print(f"Selamat datang, {self.firstname} {self.lastname}. Anda akan lulus pada tahun {self.graduationyear}.")

# Contoh penggunaan
x = Student("John", "Doe", 2025)
x.printname()  # Menggunakan metode dari kelas induk
x.welcome()    # Menggunakan metode dari kelas anak

Penjelasan Kode
>Kelas Induk: Person
 -Konstruktor __init__ menerima fname (nama depan) dan lname (nama belakang).
 -Metode printname mencetak nama lengkap.
>Kelas Anak: Student
 -Menggunakan keyword super() untuk mewarisi properti dan metode dari kelas Person.
 -Menambahkan properti baru, graduationyear, yang tidak ada di kelas induk.
 -Menambahkan metode baru, welcome, untuk memberikan pesan selamat.
>Pewarisan
 -Student mewarisi semua metode dan properti dari Person, tetapi juga dapat memiliki properti atau metode tambahan yang spesifik.

Output
Jika kode di atas dijalankan, hasilnya akan seperti ini:

Nama lengkap: John Doe
Selamat datang, John Doe. Anda akan lulus pada tahun 2025.

Variasi Lain
Jika ingin menambahkan lebih banyak fungsionalitas ke kelas anak atau meng-override metode dari kelas induk, Anda dapat melakukannya seperti ini:

class Student(Person):
    def printname(self):
        # Override metode di kelas induk
        print(f"Saya adalah seorang siswa bernama {self.firstname} {self.lastname}.")

x = Student("Jane", "Smith", 2024)
x.printname()  # Akan memanggil versi metode yang di-override

Output:

Saya adalah seorang siswa bernama Jane Smith.

Dengan inheritance, Anda dapat membuat kode yang lebih modular, dapat digunakan kembali, dan fleksibel.
