import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())

"""
prvo se pokrece asyncio.run(main()), koji inicira glavni asinhroni program.
Kreira se funkcija task1 i zakazan je status pending
zatim je kreran task2 i on je takodjer u statusu pending
nakon toga se kreira task3 koji je isto u statusu pending
zatim se ulazi u funkciju main gdje se koristi await asyncio.gather(*timers)
ovo ce pokrenuti sve tri funkcije timer istovremeno
svaki timer ce ispisivati preostalo vrijeme svake sekunde
nakon sto timer dostigne 0, ispisat ce se poruka da je vrijeme isteklo
na kraju, nakon sto su svi timeri zavrsili, program ce se zavrsiti.
"""