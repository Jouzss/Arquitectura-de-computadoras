from multiprocessing import process
import time

N = 70_000_000

def cuenta(n):
    while n>0:
        n -= 1


if __name__ == '__main__':
    N_2 = N//2
    p1 = process(target=cuenta, args=(N_2, ))
    p2 = process(target=cuenta, args=(N_2, ))

    inicio = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.5f} segundos")