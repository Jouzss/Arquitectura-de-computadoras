import asyncio
import time

async def count(orden: int):
    print(f"[{orden}] Uno")
    await asyncio.sleep(1)
    print(f"[{orden}] Dos")

# async def main():
#     await asyncio.gather(count(1), count(2), count(3))

async def main():
    await asyncio.gather(*(count(i + 1) for i in range(3)), count(4))
    # El * desempaca lo que ingreso ahí

if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()
    t_ejecucion = fin - inicio

    print(f"El tiempo de ejecucion: {t_ejecucion:0.5f} us")