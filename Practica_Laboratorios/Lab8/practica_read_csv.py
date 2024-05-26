# Queremos que a partir de la lista de notas:
# Cuente cuantos aprobaron
# Cuente cuantos reprobaron
# Imprima los códigos de quienes aprobaron y con cuanto aprobaron

import random
import time
import statistics
from typing import Union

def carga_lista() -> list[str]:
    with open("notas.csv", "r") as f:
        contenido = f.read()
    datos = contenido.split("\n")

    return datos

def cuenta_aprobados(lista_alumnos: list[str]) -> Union[int, list[str]]:
    contador = 0
    codigo = []
    for i in range(len(lista_alumnos)):
        fila = lista_alumnos[i].split(",")
        estado = fila[-1]
        if(estado == "Aprobó"):
            contador += 1
            codigo.append(fila[0])
    return contador, codigo

def cuenta_jalados(lista_alumnos: list[str]) -> int:
    contador = 0
    for i in range(len(lista_alumnos)):
        fila = lista_alumnos[i].split(",")
        estado = fila[-1]
        if(estado == "Reprobó"):
            contador += 1
    return contador

if __name__ == '__main__':
    print("Bienvenido al curso de Diseño Electrónico 2\n")
    datos = carga_lista()
    cantidad_aprobados, codigos = cuenta_aprobados(datos)
    cantidad_jalados = cuenta_jalados(datos)
    print(f"La estadística del curso indica que:\n\tAprobaron: {cantidad_aprobados}\n\tReprobaron: {cantidad_jalados}\n\tCódigos de los que aprobaron:")
    for _ in range(len(codigos)):
        print(f"\t\t\t\t\t{codigos[_]}")
