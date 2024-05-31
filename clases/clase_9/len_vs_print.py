# Que tanto impacta lo que voy a imprimir versus la operación de impresión propiamente

import time
import statistics

if __name__ == '__main__':

    palabra_100 = "a" * 100
    palabra_1000 = "a" * 1000

    time_0 = []
    time_100 = []
    time_1000 = []

    for i in range(100):

        tic0 = time.perf_counter()
        print()
        toc0 = time.perf_counter()

        tic100 = time.perf_counter()
        print(str(palabra_100))
        toc100 = time.perf_counter()

        tic1000 = time.perf_counter()
        print(str(palabra_1000))
        toc1000 = time.perf_counter()

        time_0.append(toc0 - tic0)
        time_100.append(toc100 - tic100)
        time_1000.append(toc1000 - tic1000)

    tiempo_0 = statistics.median(time_0)
    tiempo_100 = statistics.median(time_100)
    tiempo_1000 = statistics.median(time_1000)

    print(f"El tiempo de ejecución para la función print es de {tiempo_0*1e6} us")
    print(f"El tiempo de ejecución para imprimir 100 caracteres es de {tiempo_100*1e6} us")
    print(f"El tiempo de ejecución para imprimir 1000 caracteres es de {tiempo_1000*1e6} us")
