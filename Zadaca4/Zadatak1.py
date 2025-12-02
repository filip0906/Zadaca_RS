import asyncio
import aiohttp
import time

async def fetch_url(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()
    
async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        zadaci = [fetch_url(session) for _ in range(5)]
        rezultati = await asyncio.gather(*zadaci)

    users = rezultati[0]

    imena = [user['name'] for user in users]
    emails = [user['email'] for user in users]
    usernames = [user['username'] for user in users]

    end_time = time.time()

    print("Imena korisnika:", imena)
    print("Email adrese korisnika:", emails)
    print("Korisnička imena:", usernames)
    print(f"Ukupno vrijeme izvršavanja: {end_time - start_time:.2f} sekundi")

asyncio.run(main())