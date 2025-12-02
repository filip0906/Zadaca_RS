import asyncio
import random

async def fetch_weather_data(station_id):
    delay = random.uniform(1,5)
    print(f"Stanica {station_id}: Dohvaćam podatke... (čekanje {delay:.2f} sekundi)")
    await asyncio.sleep(delay)

    temperatura = random.uniform(20, 25)
    print(f"Stanica {station_id}: Dohvaćeni podaci - Temperatura: {temperatura:.2f}°C")

    return {
        "station_id": station_id,
        "temperature": temperatura,
        "delay": delay
    }

async def main():
    print("Pokretanje dohvaćanja podataka s vremenskih stanica...\n")

    Zadaci = [
        asyncio.create_task(fetch_weather_data(i+1))
        for i in range(10)
    ]

    rezultati = await asyncio.gather(*Zadaci)
    
    temperature = [result['temperature'] for result in rezultati]
    prosjecna_temp = sum(temperature) / len(temperature)

    print("Rezultati dohvaćanja podataka:\n")

    for result in rezultati:
        print(f"Stanica {result['station_id']}: Temperatura: {result['temperature']:.2f}°C (Dohvaćeno za {result['delay']:.2f} sekundi)")

    print(f"\nProsječna temperatura: {prosjecna_temp:.2f}°C")

asyncio.run(main())