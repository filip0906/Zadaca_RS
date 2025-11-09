import random

ciljani_broj = random.randint(1,100)
pokusaji = 0

print("Dobrodošli u igru pogađanja broja!")
print("Pokušajte pogoditi broj između 1 i 100.")

while True:
    try:
        pokusaji += 1
        unos = input("Unesite vaš pokušaj:")
        pogadanje = int(unos)

    except ValueError:
        print("Molimo unesite valjani cijeli broj.")
        continue
    
    if pogadanje < ciljani_broj:
        print("Previše nisko! Pokušajte ponovo.")
    elif pogadanje > ciljani_broj:
        print("Previše visoko! Pokušajte ponovo.")
    else:
        print(f"Čestitamo! Pogodili ste broj {ciljani_broj} u {pokusaji} pokušaja.")
        break