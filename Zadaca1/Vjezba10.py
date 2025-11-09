tekst="Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan"

def brojanje_rijeci(tekst):
    rijeci = tekst.lower().split()
    broj_ponavljanja = {}

    for rijec in rijeci:
        if rijec in broj_ponavljanja:
            broj_ponavljanja[rijec] += 1
        else:
            broj_ponavljanja[rijec] = 1

    return broj_ponavljanja

print("Broj ponavljanja riječi:", brojanje_rijeci(tekst))