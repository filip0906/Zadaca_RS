lista=[1,2,3,4,5,6,7,8,9,10]

def filtriraj_parne(brojevi):
    nova_lista = []
    for broj in brojevi:
        if broj % 2 == 0:
            nova_lista.append(broj)
    return nova_lista

print("Parni brojevi iz liste:", filtriraj_parne(lista))