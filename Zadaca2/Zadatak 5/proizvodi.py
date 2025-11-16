class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}")
        print(f"Cijena: {self.cijena} EUR")
        print(f"Dostupna količina: {self.dostupna_kolicina} kom")

skladiste = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

def dodaj_proizvod(proizvod):
    skladiste.append({
        "naziv": proizvod.naziv,
        "cijena": proizvod.cijena,
        "dostupna_kolicina": proizvod.dostupna_kolicina
    })