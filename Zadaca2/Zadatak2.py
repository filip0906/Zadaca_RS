nizovi = ["jabuka", "krška", "banana", "naranča"]

kvadrirane_duljine = list(map(lambda x: len(x)**2, nizovi))
print(kvadrirane_duljine)

brojevi = [1,21,33,45,2,2,1,-32,9,10]
veci_od_5 = list(filter(lambda x: x>5, brojevi))
print(veci_od_5)

brojevi = [10,5,12,15,20]
transform = dict(map(lambda x: (x, x**2), brojevi))
print(transform)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_studenti = all(map(lambda g: g["godine"] > 17, studenti))
print(svi_studenti)

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelji", "auto", "čokolada", "ples", "pjesma", "otorinolaringolog"]
min_duljina = input("Unesite minimalnu duljinu riječi: ")
duge_rijeci = list(filter(lambda r: len(r) >= int(min_duljina), rijeci))
print(duge_rijeci)