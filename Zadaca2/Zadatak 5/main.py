from narudzbe import napravi_narudzbu

naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

narudzba = napravi_narudzbu(naruceni_proizvodi)

if narudzba:
    narudzba.ispis_narudzbe()