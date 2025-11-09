rjecnik = {"ime": "Ivan", "prezime": "Ivić", "godine": 25}

def obrni_rjecnik(rjecnik):
    novi_rjecnik = {}
    for ključ, vrijednost in rjecnik.items():
        novi_rjecnik[vrijednost] = ključ
    return novi_rjecnik 

print("Obrnuti rječnik:", obrni_rjecnik(rjecnik))