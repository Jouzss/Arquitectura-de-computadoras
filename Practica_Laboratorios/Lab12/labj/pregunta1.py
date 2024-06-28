import multiprocessing
import time

N = 80_000

# N = 10

def factorial_serial(n):
    factorial = 1
    for i in range(n): 
        factorial = factorial * (i+1)

    if n == 0:
        return 1
    
    return factorial

def factorial_paralell(start, end):
    a = start
    b = end
    factorial = 1
    for i in range(a,b):
        factorial = factorial * (i+1)

    if (end == 0) or (start == 0):
        return 1

    return factorial

if __name__ == '__main__':

    end_1 = N//2

    tupla_fact = [(1, end_1),(end_1, N)]

    tic_paralell = time.perf_counter()

    with multiprocessing.Pool(processes=2) as p:
        resultado = p.starmap(factorial_paralell, tupla_fact)

    factorial_paralell_r = resultado[0]*resultado[1]

    toc_paralell = time.perf_counter()

    tic_serial = time.perf_counter()
    factorial_serial_r = factorial_serial(N)
    toc_serial = time.perf_counter()

    t_paralell = toc_paralell - tic_paralell
    t_serial = toc_serial - tic_serial

    speed_Up = t_serial/t_paralell

    assert factorial_paralell_r == factorial_serial_r
    print("Las funciones son iguales según la verificación.")
    print(f"Tiempo serial: {t_serial}")
    print(f"Tiempo paralelo: {t_paralell}")
    print(f"El SpeedUp: {speed_Up}")