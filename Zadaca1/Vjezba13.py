lista1=[1,2,3,4,5,6,7,8,9,10]

def prvi_i_zadnji(lista1):
    if len(lista1) < 2:
        return lista1
    return [lista1[0], lista1[-1]]

print("Prvi i zadnji element liste:", prvi_i_zadnji(lista1))

lista2 = [5,10,20,50,100,11,250,50,80]

def min_i_max(lista2):
    return min(lista2), max(lista2)

print("Minimalni i maksimalni element liste:", min_i_max(lista2))

skup_1 = {1,2,3,4,5}
skup_2 = {4,5,6,7,8}

def presjek(skup_1, skup_2):
    return skup_1.intersection(skup_2)

print("Presjek skupova:", presjek(skup_1, skup_2))