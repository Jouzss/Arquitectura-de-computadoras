import time

if __name__ == '__main__':
    inicio = time.perf_counter()
    print("Este es un print para evaluar")
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio)*1e6} us")

# Que tanto impacta lo que voy a imprimir versus la operación de impresión propiamente
