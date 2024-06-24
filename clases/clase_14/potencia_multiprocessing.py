from multiprocessing import Pool
import time

proc = 4
tareas = proc * 1

def potencia(n: int, div: int = tareas):
    pot = 1

    rango = n // div

    for _ in range(rango):
        pot = pot * n

    return pot

if __name__ == '__main__':
    inicio = time.perf_counter()
    args = [200_000] * tareas

    p = Pool(processes = proc)
    pl = p.map(potencia, args)

    p.close()
    p.join()

    pot_total = 1

    for i in range(len(pl)):
        pot_total *= pl[i]

    fin = time.perf_counter()

    print(f"Tiempo de ejecición: {(fin - inicio):0.3} s")