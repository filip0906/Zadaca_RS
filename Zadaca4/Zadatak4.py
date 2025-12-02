import aiohttp
import asyncio

korisnici = {
    "korisnik1" : "lozinka1",
    "korisnik2" : "lozinka2",
    "korisnik3" : "lozinka3",
    "korisnik4" : "lozinka4",
    "korisnik5" : "lozinka5"
}

async def autentifikacija(korisnicko_ime, lozinka):
    print(f"Autentifikacija korisnika {korisnicko_ime}...")
    await asyncio.sleep(2)  
    
    if korisnicko_ime not in korisnici:
        raise ValueError(f"Korisnik {korisnicko_ime} ne postoji.")
    elif korisnici[korisnicko_ime] != lozinka:
        raise ValueError(f"Pogrešna lozinka za korisnika {korisnicko_ime}.")
    
    print(f"Korisnik {korisnicko_ime} je uspješno autentificiran.")
    return True
    
async def main():
    zahtjevi = [
        ("korisnik1", "lozinka1"),
        ("korisnik2", "pogresna_lozinka"),
        ("nepostojeci_korisnik", "lozinka"),
        ("korisnik3", "lozinka3"),
        ("korisnik4", "lozinka4")
    ]
    
    zadaci = [
        asyncio.wait_for(autentifikacija(korisnicko_ime, lozinka), timeout=3)
        for korisnicko_ime, lozinka in zahtjevi
    ]

    rezultati = await asyncio.gather(*zadaci, return_exceptions=True)

    print("\n" + "="*70)
    print("REZULTATI AUTENTIFIKACIJE:")
    print("="*70)
    for i, (korisnicko_ime, lozinka) in enumerate(zahtjevi):
        rezultat = rezultati[i]
        if isinstance(rezultat, Exception):
            print(f"{korisnicko_ime}: {type(rezultat).__name__} - {rezultat}")
        else:
            print(f"{korisnicko_ime}: Uspješno autentificiran")

asyncio.run(main())