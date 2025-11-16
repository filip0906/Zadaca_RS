from proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        detalji = ", ".join(
            [f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi]
        )
        print(f"Naručeni proizvodi: {detalji}, Ukupna cijena: {self.ukupna_cijena} eur")

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        print("Greška: naruceni_proizvodi mora biti lista!")
        return None
    
    if len(naruceni_proizvodi) == 0:
        print("Greška: Lista ne smije biti prazna!")
        return None
    
    for proizvod in naruceni_proizvodi:
        if not isinstance(proizvod, dict):
            print("Greška: Svaki element mora biti rječnik!")
            return None
        
        if not all(key in proizvod for key in ['naziv', 'cijena', 'narucena_kolicina']):
            print("Greška: Svaki rječnik mora sadržavati ključeve 'naziv', 'cijena' i 'narucena_kolicina'!")
            return None
    
    for proizvod in naruceni_proizvodi:
        pronadjen = False
        
        for p_skladiste in skladiste:
            if p_skladiste['naziv'] == proizvod['naziv']:
                pronadjen = True
                
                if p_skladiste['dostupna_kolicina'] < proizvod['narucena_kolicina']:
                    print(f"Proizvod {proizvod['naziv']} nije dostupan!")
                    return None
                break
        
        if not pronadjen:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None
    
    ukupna_cijena = sum(p['cijena'] * p['narucena_kolicina'] for p in naruceni_proizvodi)
    
    nova_narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append(nova_narudzba)
    
    return nova_narudzba
