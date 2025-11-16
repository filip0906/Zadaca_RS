#1
"""from datetime import datetime
class Automobil:
    
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Starost automobila: {starost} godina")

auto = Automobil("Toyota", "Corolla", 2015, 75000)
auto.ispis()
auto.starost()"""

#2
"""class Kalkulator:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno."
        
    def potenciranje(self):
        return self.a ** self.b 
    
    def korijen(self):
        if self.a >= 0:
            return self.a ** 0.5
        else:
            return "Nije moguće izračunati korijen negativnog broja."   
        
kalkulator = Kalkulator(16, 4)
print("Zbroj:", kalkulator.zbroj())
print("Oduzimanje:", kalkulator.oduzimanje())
print("Množenje:", kalkulator.mnozenje())
print("Dijeljenje:", kalkulator.dijeljenje())
print("Potenciranje:", kalkulator.potenciranje())
print("Korijen:", kalkulator.korijen())"""

#3
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5,4,3,5,2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3,4,5,2,3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5,5,5,5,5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2,3,2,4,3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4,4,4,3,5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5,5,5,5,5]}
]

#4
"""class Student:
    def __init__(self, ime, prezime, godine, ocjene=[]):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        if len(self.ocjene) == 0:
            return 0
        return sum(self.ocjene) / len(self.ocjene)
    
studenti_objekt = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]

najbolji_student = max(studenti_objekt, key=lambda s: s.prosjek())
print(f"Najbolji student je {najbolji_student.ime} {najbolji_student.prezime} s prosjekom ocjena {najbolji_student.prosjek():.2f}.")"""

#5
"""class Krug:
    def __init__(self,r):
        self.r = r

    def povrsina(self):
        return 3.14 * self.r ** 2
    
    def opseg(self):
        return 2 * 3.14 * self.r
    
objekt_krug = Krug(5)
print(f"Površina kruga: {objekt_krug.povrsina():.2f}")
print(f"Opseg kruga: {objekt_krug.opseg():.2f}")    """

#6
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    
    def work(self):  # ← Dodaj self
        print(f"Radim na poziciji {self.pozicija}")  # ← Dodaj f

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, departman):
        super().__init__(ime, pozicija, placa)
        self.departman = departman

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.departman}")

    def give_raise(self, radnik, iznos):  # Dodaj 'radnik' parametar
        radnik.placa += iznos
        print(f"Placa radnika {radnik.ime} je povecana za {iznos}. Nova placa je {radnik.placa}.")

radnik1 = Radnik("Ivan", "Programer", 5000)
manager1 = Manager("Marko", "Menadžer", 8000, "IT")

radnik1.work()
manager1.work()
manager1.give_raise(radnik1, 1000)
