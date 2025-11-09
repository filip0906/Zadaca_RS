def provjer_lozinke(lozinka):
    if not (8 <= len(lozinka) <=15):
        print("Lozinka mora imati između 8 i 15 znakova.")
        return False
    lower_pass = lozinka.lower()
    if "password" in lower_pass or "lozinka" in lower_pass:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")
        return False
    
    has_upper = False
    has_digit = False

    for char in lozinka:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        
        if has_upper and has_digit:
            break

    if not (has_upper and has_digit):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jednu znamenku.")
        return False
    
    print("Lozinka je jaka!")
    return True

def main():
    while True:
        lozinka = input("Unesite lozinku za provjeru: ")
        
        jaka_je = provjer_lozinke(lozinka)

        if jaka_je:
            break
if __name__ == "__main__":
    main()