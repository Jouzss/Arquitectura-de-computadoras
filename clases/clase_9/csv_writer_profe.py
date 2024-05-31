import random
import time
import statistics

if __name__ == '__main__':
    inicio_cpu = time.perf_counter()
    codigo_base = 20240001
    contenido = f"codigo,{','.join(f'lab{i + 1}' for i in range(12))},e1,e2\n"
    
    for i in range(200):
        fila = f"{codigo_base + i},{','.join(str(random.randint(0,20)) for _ in range(14))}\n"
        # ','.join(str(random.randint(0,20)) for _ in range(14))}\n: es un generador y es más rápido que usar otro for
        contenido += fila
    
    # contenido += '\n'.join(f"{codigo_base + i},{','.join(str(random.randint(0,20)) for _ in range(14))}" for i in range(200))

    contenido = contenido[:-1] 

    fin_cpu = time.perf_counter()

    tic = time.perf_counter()
    with open("notas.csv", "w+") as f:
        f.write(contenido)
    toc = time.perf_counter()

    print(f"El tiempo de CPU es de: {fin_cpu - inicio_cpu} segundos \nEl tiempo de IO: {toc - tic} segundos")