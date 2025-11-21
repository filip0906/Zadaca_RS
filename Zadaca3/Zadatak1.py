import asyncio

async def dohvati_podatke():
    print("Zahtjev primljen")
    podaci = [broj for broj in range(1, 11)]
    await asyncio.sleep(3)
    print("Dohvaćeni podaci")
    return podaci

async def main():
    rezultat = await dohvati_podatke()
    print(f"Rezultat: {rezultat}")

asyncio.run(main())