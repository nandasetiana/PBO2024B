class Person:
    def __init__(self, name, gender, ipk):
        self.name = name
        self.gender = gender
        self.ipk = ipk

    def myfunc(self):
        print("Mahasiswa PBO kelas B adalah " + self.name + " dan memiliki jenis kelamin " + self.gender)
        print("dengan IPK " + str(self.ipk))
    
p1 = Person("Nanda imoettt", "ciwi", 4)
p1.myfunc()
