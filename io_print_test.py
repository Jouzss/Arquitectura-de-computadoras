# Que tanto impacta lo que voy a imprimir versus la operación de impresión propiamente

import time

if __name__ == '__main__':
    base_str = "*"
    res = list()

    for idx in range(1000):
        str_completo = base_str * (idx + 1)
        inicio = time.perf_counter()
        print(str_completo)
        fin = time.perf_counter()

        print(f"[{idx + 1}] Tiempo total de ejecucion: {(fin - inicio)*1e6} us")
        res.append(fin - inicio)

    promedio = sum(res)/len(res)
    maximo = max(res)
    minimo = min(res)

    print("\n")
    print(f"Tiempo promedio de E/S {promedio*1e6} us\nmaximo: {maximo*1e6} us\nminimo: {minimo*1e6} us")