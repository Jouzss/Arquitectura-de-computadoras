import multiprocessing
import random

N = 10_000_000

def muestras_dentro(x1, x2, y1, y2, n):
    contador = 0
    for i in range(n):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)
        if((x**2 + y**2) <= 1):
            contador += 1

    return contador

if __name__ == '__main__':

    tuple_arr = [(-1, 0, -1, 0, N), (-1, 0, 0, 1, N), (0, 1, 0, 1, N), (0, 1, -1, 0, N)]

    with multiprocessing.Pool(processes=4) as p:
        resultado = p.starmap(muestras_dentro, tuple_arr)

    n_muestras_dentro = resultado[0] + resultado[1] + resultado[2] + resultado[3]
    pi = (n_muestras_dentro/N)
    print(f"Pi: {pi}")