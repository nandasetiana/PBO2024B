Python - Enkapsulasi

Enkapsulasi adalah proses menggabungkan atribut dan metode dalam satu unit. Ini adalah salah satu pilar utama yang mendasaripemrograman berorientasi objekparadigma didasarkan.

Menurut prinsip enkapsulasi data, anggota data yang menggambarkan suatu objek disembunyikan dari lingkungan di luar kelas. Anggota data tersebut hanya dapat diakses melalui metode dalam kelas yang sama. Metode itu sendiri di sisi lain dapat diakses dari luar konteks kelas. Oleh karena itu, data objek dikatakan dienkapsulasi oleh metode. Dengan cara ini, enkapsulasi mencegah akses langsung ke data objek.

Menerapkan Enkapsulasi dalam Python

Bahasa seperti C++ dan Java menggunakan pengubah akses untuk membatasi akses ke anggota kelas (misalnya, variabel dan metode). Bahasa-bahasa ini memiliki kata kunci publik, terlindungi, dan pribadi untuk menentukan jenis akses.

Seorang anggota kelas dikatakan publik jika dapat diakses dari mana saja dalam program. Anggota pribadihanya dapat diakses dari dalam kelas. Biasanya, metode didefinisikan sebagai publik, dan variabel instan bersifat privat. Susunan variabel instan privat dan metode publik ini memastikan penerapan enkapsulasi.

Tidak seperti bahasa-bahasa ini,Python  tidak memiliki ketentuan untuk menentukan jenis akses yang dapat dimiliki oleh anggota kelas. Secara default, semua variabel dan metode dalam kelas Python bersifat publik, seperti yang ditunjukkan oleh contoh berikut.
Di sini, kita memiliki kelas Student dengan variabel instan,nama dan usia. Sebuah objek dari kelas ini memiliki dua hal ini atribut. Mereka dapat diakses langsung dari luar kelas, karena bersifat publik.
class Student:
   def __init__(self, name="Rajaram", marks=50):
      self.name = name
      self.marks = marks

s1 = Student()
s2 = Student("Bharat", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))

Output:
Name: Rajaram marks: 50
Name: Bharat marks: 25

Dalam contoh di atas, variabel instan diinisialisasi di dalam kelas. Namun, tidak ada pembatasan dalam mengakses nilai variabel instan dari luar kelas, yang bertentangan dengan prinsip enkapsulasi.
Meskipun tidak ada kata kunci untuk menegakkan visibilitas, Python memiliki konvensi penamaan variabel instan dengan cara yang unik. Dalam Python, awalan nama variabel/metode dengan garis bawah tunggal atau ganda untuk meniru perilaku pengubah akses protected dan private.
Jika sebuah variabel diawali dengan satu garis bawah ganda (seperti "__usia"), variabel instan bersifat pribadi, sama halnya jika nama variabel diawali dengan satu garis bawah (seperti "_gaji")


Apa itu Name Mangling?

Python tidak sepenuhnya memblokir akses ke data pribadi. Ia hanya menyerahkannya pada kebijaksanaan programmer, untuk tidak menulis kode apa pun yang mengaksesnya dari luar kelas. Anda masih dapat mengakses anggota pribadi dengan teknik manipulasi nama Python.

Pengacauan nama adalah proses mengubah nama anggota dengan garis bawah ganda ke bentukobjek._kelas__variabel. Jika memang diperlukan, akses tersebut masih dapat dilakukan dari luar kelas, tetapi praktik tersebut sebaiknya dihindari.

Dalam contoh, variabel instance pribadi "__name" diubah dengan mengubahnya ke format

obj._class__privatevar

Jadi, untuk mengakses nilai variabel instan "__marks" dari objek "s1", ubahlah menjadi "s1._Student__marks".
Ubah pernyataan print() dalam program di atas menjadi −

print (s1._Student__marks)

Sekarang mencetak 50, tanda s1.

Oleh karena itu, kita dapat menyimpulkan bahwa Python tidak mengimplementasikan enkapsulasi secara persis sesuai teori pemrograman berorientasi objek. Ia mengadaptasi pendekatan yang lebih matang terhadap hal tersebut dengan menetapkan konvensi nama dan membiarkan programmer menggunakan manipulasi nama jika benar-benar diperlukan untuk memiliki akses ke data pribadi dalam lingkup publik.


TUGAS 3 :

Dalam kode, prinsip enkapsulasi diterapkan melalui penggunaan data internal yang disembunyikan dalam atribut kelas Konoha. Atribut-atribut seperti encoded_str, sum_digits, dan letters dikelola secara privat, dan akses serta manipulasi data dilakukan melalui metode internal yang dikendalikan oleh kelas.

Cuplikan Enkapsulasi:

class Konoha:

    def __init__(self, encoded_str):
        # Atribut yang disembunyikan (privat) dalam kelas Konoha
        self.encoded_str = encoded_str  # string input yang akan di-decode
        self.sum_digits = 0            # Menyimpan jumlah total digit dari encoded_str
        self.letters = []              # Menyimpan huruf yang dikumpulkan dari encoded_str

    def calculate_sum_of_digits(self):
        """Menghitung jumlah total digit dalam encoded_str."""
        for char in self.encoded_str:
            if char.isdigit():
                self.sum_digits += int(char)

    def collect_letters(self):
        """Mengumpulkan semua huruf dari encoded_str."""
        for char in self.encoded_str:
            if char.isalpha():
                self.letters.append(char)

    def decrypt(self):
        """Melakukan dekripsi berdasarkan jumlah digit dalam encoded_str."""
        self.calculate_sum_of_digits()  # Menghitung jumlah digit

        # Pengecekan jika tidak ada digit
        if self.sum_digits == 0:
            print("Tidak memiliki angka")
            return ""

        self.collect_letters()  # Mengumpulkan huruf

        # Menghitung shift untuk dekripsi
        shift = self.sum_digits % 26  # Menghindari pergeseran lebih dari 26

        decrypted_letters = []

        # Proses dekripsi huruf
        for letter in self.letters:
            if letter.islower():
                # Geser huruf kecil
                new_char = chr((ord(letter) - ord('a') - shift) % 26 + ord('a'))
            else:
                # Geser huruf besar
                new_char = chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))

            decrypted_letters.append(new_char)

        return ''.join(decrypted_letters)  # Menggabungkan hasil dekripsi


# Contoh penggunaan
input_str = "N4nd4a"
decoder = Konoha(input_str)
output = decoder.decrypt()
print(output)

Penjelasan Penerapan Enkapsulasi:
1. Atribut Privat:
> sum_digits dan letters adalah atribut privat dalam kelas Konoha. Atribut ini digunakan untuk menyimpan nilai yang dihitung selama proses dekripsi, namun mereka tidak diakses langsung dari luar kelas.
> encoded_str disediakan sebagai parameter input untuk kelas, tetapi setelah itu hanya digunakan di dalam metode untuk pemrosesan lebih lanjut.

2. Metode Privat:
> Metode seperti calculate_sum_of_digits dan collect_letters bertanggung jawab untuk melakukan manipulasi data internal, tetapi tidak ada akses langsung ke data tersebut di luar kelas. Semua manipulasi data dilakukan di dalam kelas melalui metode ini.

3. Interaksi Melalui Metode Publik:
> Untuk melakukan dekripsi, decrypt adalah satu-satunya metode publik yang dapat dipanggil dari luar untuk memulai proses dekripsi. Metode ini mengakses atribut privat (sum_digits, letters) dan memodifikasi data internal tanpa memberikan akses langsung kepada objek luar.

4. Validasi dan Pengolahan Data:
> Dalam metode decrypt, proses validasi dilakukan untuk memastikan bahwa data yang diproses (seperti jumlah digit) valid sebelum melanjutkan ke langkah berikutnya. Ini menjaga kontrol atas bagaimana dan kapan data dimodifikasi, yang merupakan salah satu tujuan dari enkapsulasi.
 


TUGAS 4 : 

Cuplikan Enkapsulasi

class IOException:
    def __init__(self, filename):
        self.filename = filename              # Atribut publik untuk menyimpan nama file
        self.lines = []                        # Daftar untuk menyimpan baris file (privat)
        self.char_counts = []                  # Daftar untuk menyimpan jumlah karakter per baris (privat)
        self.min_chars = None                  # Nilai untuk menyimpan karakter minimum per baris (privat)
        self.max_chars = None                  # Nilai untuk menyimpan karakter maksimum per baris (privat)
        self.char_range = None                 # Rentang jumlah karakter (privat)

        try:
            self.read_file()                  # Metode untuk membaca file (akses melalui metode)
            if not self.lines:                # Menggunakan data internal dengan cek lines
                self.write_null()             # Menulis 'NULL' jika file kosong
            else:
                self.calculate_stats()        # Menghitung statistik (akses data privat)
                self.write_output()           # Menulis output ke file
        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        else:
            print(f"Output berhasil ditulis pada {self.filename}")
        finally:
            input("Program selesai. Tekan enter untuk keluar...")

    def read_file(self):
        # Membaca isi file dan menyimpan setiap baris ke dalam list self.lines.
        # Menghitung jumlah karakter per baris dan menyimpannya dalam self.char_counts.
        with open(self.filename, "r") as in_file:
            self.lines = in_file.readlines()
            self.char_counts = [len(line.rstrip('\n')) for line in self.lines]  # Menghapus \n

    def calculate_stats(self):
        # Menghitung nilai minimum, maksimum, dan rentang dari jumlah karakter per baris.
        self.min_chars = min(self.char_counts)   # Data privat
        self.max_chars = max(self.char_counts)   # Data privat
        self.char_range = self.max_chars - self.min_chars  # Data privat

    def write_output(self):
        # Menulis hasil perhitungan (min, max, range) ke dalam file yang sama tanpa menghilangkan isi sebelumnya.
        with open(self.filename, "a") as out_file:
            out_file.write("###########\n")
            out_file.write(f"Min: {self.min_chars} karakter\n")   # Akses data privat
            out_file.write(f"Max: {self.max_chars} karakter\n")   # Akses data privat
            out_file.write(f"Range: {self.char_range} karakter\n") # Akses data privat

    def write_null(self):
        # Menulis 'NULL' ke dalam file jika file kosong.
        with open(self.filename, "w") as out_file:
            out_file.write("NULL\n")
        print("File tidak berisi teks. Ditulis 'NULL' ke dalam file.")

def main():
    in_filename = input("Masukkan nama file input: ")
    IOException(in_filename)  # Menggunakan kelas IOException untuk memproses file

if __name__ == "__main__":
    main()

Penerapan Enkapsulasi:
1. Atribut Privat dan Data Tersembunyi:
> Atribut seperti lines, char_counts, min_chars, max_chars, dan char_range digunakan secara internal dalam kelas IOException. Mereka disimpan sebagai data privat dan hanya dimodifikasi atau dibaca melalui metode internal.
> Atribut-atribut ini tidak diakses langsung oleh objek dari luar kelas, yang menjaga kontrol atas data dan memastikan bahwa nilai-nilai ini hanya dapat dimodifikasi melalui metode yang sudah disediakan.
2. Metode Publik untuk Berinteraksi dengan Data:
> Semua interaksi dengan data dilakukan melalui metode yang ditentukan, seperti read_file(), calculate_stats(), write_output(), dan write_null(). Program luar tidak dapat mengakses atau mengubah data pribadi kelas IOException secara langsung; sebaliknya, akses ke data dilakukan hanya melalui metode yang dapat memastikan integritas dan kontrol atas operasi yang dilakukan.
3. Penyembunyian Implementasi:
> Bagian-bagian kode yang berkaitan dengan proses internal, seperti membaca file, menghitung statistik, dan menulis output, disembunyikan di dalam metode kelas dan tidak langsung terlihat oleh pemanggil luar. Ini memungkinkan kelas IOException untuk mengontrol cara data diproses dan dipresentasikan tanpa memberi akses langsung kepada pengguna untuk mengubah implementasinya.


TUGAS 5 :
Dalam contoh kode, enkapsulasi diterapkan melalui pengorganisasian data dan metode di dalam kelas. Enkapsulasi berarti bahwa data (misalnya, nama dan kapasitas) disembunyikan dari akses langsung dari luar kelas dan hanya dapat dimanipulasi melalui metode yang disediakan oleh kelas tersebut. Dengan kata lain, data internal objek dilindungi dan hanya dapat diubah atau diakses melalui metode yang sah.

Untuk memberikan contoh enkapsulasi dari kode, bisa melihat bagaimana kelas Keranjang dan DekDepe diimplementasikan. Sebagai tambahan, kita bisa memperkenalkan teknik pengacauan nama (name mangling) untuk memperjelas konsep enkapsulasi yang lebih ketat.

Penjelasan Enkapsulasi dalam Kode:

1. Enkapsulasi di dalam kelas Keranjang:
> Dalam kelas Keranjang, variabel nama dan kapasitas didefinisikan sebagai atribut publik, yang artinya dapat diakses langsung dari luar kelas. Namun, dalam penerapan enkapsulasi yang lebih baik, Anda bisa mempertimbangkan untuk menjadikan atribut-atribut ini "pribadi" dengan menambah awalan garis bawah pada nama variabel, seperti _nama dan _kapasitas, untuk menandakan bahwa mereka tidak dimaksudkan untuk diakses langsung dari luar kelas.
2. Metode DekDepe:
> Kelas DekDepe menyimpan daftar keranjang dalam atribut daftar_keranjang. Atribut ini juga bersifat publik dan dapat diakses secara langsung dari luar kelas, tetapi seharusnya metode seperti beli, jual, ubah_kapasitas, dan lainnya yang bertanggung jawab untuk mengubah atau mengambil data dari daftar_keranjang.