import asyncio

# Para definir funciones se pone async antes de def.

async def prueba(n):
    # con el comando await asuncio.sleep(n), doy un retardo de n segundos
    print(f"[{n}] inicio")
    await asyncio.sleep(3)
    print(f"[{n}] final")

async def main():
    # con el comando await asyncio.gather(prueba(0), prueba(1), ..., prueba(n))
    # podemos correr en paralelo todas las funciones ingresadas
    await asyncio.gather(prueba(1), prueba(2), *(prueba(i + 3) for i in range(2)))

if __name__ == '__main__':
    # Con el comando asyncio.run(funcion()) podemos correr las funciones async
    asyncio.run(main())
