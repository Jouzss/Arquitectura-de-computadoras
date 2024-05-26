import random
import time
import statistics

if __name__ == '__main__':
    codigo = 20210001
    contenido = f"Codigo,{','.join(f'lab{i + 1}' for i in range(6))},Ex1,Ex2,Nota_Final,Estado_del_curso\n"

    for i in range(19):

        notas = [random.randint(0,20) for i in range(8)]
        promedio_labs = sum(notas[:6])/6
        nota_final = (promedio_labs + notas[6] + notas[7])/3
        estado = "Aprobó" if nota_final >= 10.5 else "Reprobó"

        fila = f"{codigo + i},{','.join(str(nota) for nota in notas)},{round(nota_final)},{estado}\n"
        
        contenido += fila

    contenido = contenido[:-1]

    with open("notas.csv", "w+") as f:
        f.write(contenido)

    