import asyncio
import json
import random 

async def recibe_nota(codigo: str) -> float:
    msg_envio = {"codigo": codigo, "modo": "servidor"}

    msg_envio_b = json.dumps(msg_envio).encode("utf-8")

    await asyncio.sleep(random.randint(1, 4))

    msg_recibido = {"estado": "exito", "nota": (random() * 20)}
    
    return msg_recibido["nota"]

async def main():
    codigo_base = 20240001
    codigos = [str(codigo_base + i) for i in range(10)]
    notas = await asyncio.gather(*(recibe_nota(codigo) for codigo in codigos))

    return notas

if __name__ == '__main__':
    notas_finales = asyncio.run(main())

    for nota_final in notas_finales:
        print(f"nota final: {nota_final:0.2f}")

    # nota_final = sum(notas_finales) / len(notas_finales)

    # print(f"Promedio de nota final del grupo: {nota_final:0.2f}")