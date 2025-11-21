import asyncio

async def dohvati_podatke():
    await asyncio.sleep(3)
    korisnici = [
        {"id": 1, "ime": "Ana", "godine": 25},
        {"id": 2, "ime": "Marko", "godine": 30},
        {"id": 3, "ime": "Ivana", "godine": 28}
    ]
    print("Dohvaćeni korisnici")
    return korisnici

async def dohvati_proizvode():
    await asyncio.sleep(5)
    proizvodi = [
        {"id": 101, "naziv": "Laptop", "cijena": 7500},
        {"id": 102, "naziv": "Pametni telefon", "cijena": 4500},
        {"id": 103, "naziv": "Tablet", "cijena": 3000}
    ]
    print("Dohvaćeni proizvodi")
    return proizvodi

async def main():
    rezultati = await asyncio.gather(dohvati_podatke(), dohvati_proizvode())
    korisnici, proizvodi = rezultati
    print(f"Korisnici: {korisnici}\n")
    print(f"Proizvodi: {proizvodi}\n")

asyncio.run(main())