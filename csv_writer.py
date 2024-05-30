# CSV: Comma Separated Values
# Es un tipo de archivo de texto plano (muy simple). 
# El archivo csv trata de modelar una tabla. 
# Es muy ineficiente, pero si es una cantidad de data pequeña, es bastante simple de utilizar
# En la tabla las columnas se separan con "," y las filas con saltos de línea "\n".
# La ventaja es que se puede hacer muy fácil un csv de forma manual o mediante código.

import random
import time
import statistics

if __name__ == '__main__':
    codigo_base = 20240001
    contenido = f"codigo,{','.join(f'lab{i + 1}' for i in range(12))},e1,e2\n"
    
    for i in range(200):
        fila = f"{codigo_base + i},{','.join(str(random.randint(0,20)) for _ in range(14))}\n"
        # ','.join(str(random.randint(0,20)) for _ in range(14))}\n: es un generador y es más rápido que usar otro for
        contenido += fila
    
    contenido = contenido[:-1] 
    # slicing: de esto sale el porque del :-1. Los : separan de donde quiero empezar y donde
    # quiero terminar. Elimina el último salto de línea.

    time_list = []

    for idx in range(10000):
        tic = time.perf_counter()
        with open("notas.csv", "w+") as f:
            f.write(contenido)
        toc = time.perf_counter()
        tiempo_ejecucion = (toc - tic)*1e6
        time_list.append(tiempo_ejecucion)

    tiempo_mediana = statistics.median(time_list)
    print(f"El tiempo de ejecución es de: {tiempo_mediana} us")