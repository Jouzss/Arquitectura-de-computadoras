import time

N = 200_000_000

def count(n):
    while n>0:
        n -=1

if __name__ == '__main__':
    inicio = time.perf_counter()

    count(N)

    fin = time.perf_counter()

    print(f"Tiempo de ejecición: {(fin - inicio):0.3} s")