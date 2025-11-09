Lista = [1,2,3,4,5,6,7,8,9,10]

def grupiraj_po_parnosti(Lista):
    parni = []
    neparni = []
    for broj in Lista:
        if broj % 2 == 0:
            parni.append(broj)
        else:
            neparni.append(broj)
    return parni, neparni

print("Parni i neparni brojevi iz liste:", grupiraj_po_parnosti(Lista))