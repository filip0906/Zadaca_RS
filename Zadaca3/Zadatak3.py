import asyncio

baza_korisnika = [{"korisnicko_ime": "mirko123", "email": "mirko123@gmail.com"},
                      {"korisnicko_ime": "ana_anic", "email": "ana_anic@gmail.com"},
                      {"korisnicko_ime": "maja_0x", "email": "maja_0x@gmail.com"},
                      {"korisnicko_ime": "zdeslav032", "email": "zdeslav032@gmail.com"}]

baza_lozinaka = [{"korisnicko_ime": "mirko123", "lozinka": "lozinka123"},
                      {"korisnicko_ime": "ana_anic", "lozinka": "super_teska_lozinka"},
                      {"korisnicko_ime": "maja_0x", "lozinka": "s324SDFfdsj234"},
                      {"korisnicko_ime": "zdeslav032", "lozinka": "deso123"}]

async def autorizacija(korisnik_iz_baze, lozinka):
    print(f"Provjera lozinke u tijeku... {korisnik_iz_baze['korisnicko_ime']}")
    await asyncio.sleep(2)

    for k in baza_lozinaka:
        if k["korisnicko_ime"] == korisnik_iz_baze["korisnicko_ime"] and k["lozinka"] == lozinka:
            print(f"Korisnik {korisnik_iz_baze['korisnicko_ime']} uspješno autoriziran.")
            return True
    
    print(f"Neuspjela autorizacija za korisnika {korisnik_iz_baze['korisnicko_ime']}.")
    return False

async def autentifikacija_korisnika(korisnik):
    print(f"Provjera korisnika u tijeku... {korisnik['korisnicko_ime']}")

    await asyncio.sleep(3)

    for k in baza_korisnika:
        if k['korisnicko_ime'] == korisnik['korisnicko_ime'] and k['email'] == korisnik['email']:
            rezultat = await autorizacija(k, korisnik['lozinka'])
            return rezultat
    
    print(f"Korisnik {korisnik['korisnicko_ime']} nije pronađen.")
    return None

async def main():
    korisnik1 = {"korisnicko_ime": "mirko123", "email": "mirko123@gmail.com", "lozinka": "lozinka123"}
    rezultat1 = await autentifikacija_korisnika(korisnik1)
    print(rezultat1)

    
    korisnik2 = {"korisnicko_ime": "marko456", "email": "marko@example.com", "lozinka": "kriva_lozinka"}
    rezultat2 = await autentifikacija_korisnika(korisnik2)
    print(rezultat2)
    
    korisnik3 = {"korisnicko_ime": "zdeslav032", "email": "zdeslav032@gmail.com", "lozinka": "desi123"}
    rezultat3 = await autentifikacija_korisnika(korisnik3)
    print(rezultat3)

asyncio.run(main())