import asyncio
import aiohttp

async def fetch_url(session, url, str) -> str:
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
        return await response.text()
    
async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        zadaci = [fetch_url(session, url, url) for url in urls]
        rezultati = await asyncio.gather(*zadaci)

    for url, content in zip(urls, rezultati):
        print(f"Fetched {len(content)} characters from {url}\n")

if __name__ == "__main__":
    asyncio.run(main())