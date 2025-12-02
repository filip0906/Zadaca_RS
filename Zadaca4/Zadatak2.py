import asyncio
import aiohttp

async def fetch_url(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        return data['fact']
    
async def filter_cat_facts(facts):
    filtered = [fact for fact in facts if 'cat' in fact.lower() or 'cats' in fact.lower()]
    return filtered

async def main():
    async with aiohttp.ClientSession() as session:
        zadaci = [fetch_url(session) for _ in range(20)]
        facts = await asyncio.gather(*zadaci)

    filtered_facts = await filter_cat_facts(facts)

    print("Filtrirane činjenice o mačkama:\n")
    for fact in filtered_facts:
        print("-", fact)

asyncio.run(main())