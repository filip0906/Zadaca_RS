import asyncio

async def secure_data(data):
    await asyncio.sleep(3)

    enkriptirani_podaci = {
        'prezime': data['prezime'],
        'broj_kartice': hash(data['broj_kartice']),
        'cvv': hash(data['cvv']),
    }

    return enkriptirani_podaci

async def main():
    podaci_korisnika = [
        {'prezime': 'Marić', 'broj_kartice': '1234-5678-9012-3456', 'cvv': '123'},
        {'prezime': 'Horvat', 'broj_kartice': '9876-5432-1098-7654', 'cvv': '456'},
        {'prezime': 'Kovač', 'broj_kartice': '5555-6666-7777-8888', 'cvv': '789'}
    ]

    print("Osjetljivi podaci prije enkripcije:")
    for podatak in podaci_korisnika:
        print(podatak)

    zadaci = [asyncio.create_task(secure_data(podatak)) for podatak in podaci_korisnika]

    rezultati = await asyncio.gather(*zadaci)

    print("\nEnkriptirani podaci:")
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())