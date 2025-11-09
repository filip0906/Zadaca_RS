vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def count_vowels_consonants(tekst):
    broj_samoglasnika = 0
    broj_suglasnika = 0

    for char in tekst:
        if char in vowels:
            broj_samoglasnika += 1
        elif char in consonants:
            broj_suglasnika += 1

    return broj_samoglasnika, broj_suglasnika

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan"
print("Broj samoglasnika i suglasnika u tekstu:", count_vowels_consonants(tekst))