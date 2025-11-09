cijeli_broj = -1
rezultat = 0

while cijeli_broj != 0:
    cijeli_broj = int(input("Unesite cijeli broj: "))
    
    rezultat += cijeli_broj
    if cijeli_broj == 0:
        print("Zbroj unesenih brojeva je:", rezultat)
        break
    