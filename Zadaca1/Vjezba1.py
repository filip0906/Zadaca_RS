a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /): ")

if operator == "+":
    rezultat = a + b
    print("Rezultat zbrajanja je: ", rezultat)
elif operator == "-":
    rezultat = a - b
    print("Rezultat oduzimanja je: ", rezultat)
elif operator == "*":
    rezultat = a * b
    print("Rezultat množenja je: ", rezultat)
elif operator == "/":
    if b != 0:
        rezultat = a / b
        print("Rezultat dijeljenja je: ", rezultat)
    else:
        print("Greška: Dijeljenje s nulom nije dozvoljeno.")
else:
    print("Nepodržani operator!")