import random

N = 10_000_000

def muestras_dentro(n):
    contador = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if((x**2 + y**2) <= 1):
            contador += 1

    return contador

if __name__ == '__main__':
    n_muestras_dentro = muestras_dentro(N)
    pi = (n_muestras_dentro/N)*4
    print(f"Pi: {pi}")