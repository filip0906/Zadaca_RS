lista=[1,2,3,2,1,5,5,7]

def ukloni_duplicirane(brojevi):
    jedinstveni_brojevi = []
    for broj in brojevi:
        if broj not in jedinstveni_brojevi:
            jedinstveni_brojevi.append(broj)
    return jedinstveni_brojevi

print("Lista bez dupliciranih elemenata:", ukloni_duplicirane(lista))