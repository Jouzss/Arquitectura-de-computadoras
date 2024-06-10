import socket
from threading import Thread
import json

SOCK_BUFFER = 1024

def  busca_info(codigo: str) -> list[str]:
    with open("notas.csv", "r") as f:
        contenido = f.read()
    contenido = contenido.split("\n")

    for fila in contenido:
        if codigo in fila:
            return fila.split(",")
        
    return list()

def empaqueta_datos(notas: list[str], modo: str) -> dict:
    match modo:
        case"cliente":
            r_dict = dict()
            for idx in range(6):
                r_dict[f"lab{idx + 1}"] = int(notas[idx + 1])
            r_dict["e1"] = int(notas[7])
            r_dict["e2"] = int(notas[8])
            r_dict["estado"] = "éxito"
        case"servidor":
            notas_lab = 0
            for idx in range(6):
                notas_lab += int(notas[idx + 1])
            notas_lab = notas_lab / 6

            nota = ((notas_lab) + int(notas[7]) + int(notas[8])) / 3

            r_dict = {"estado": "éxito", "nota": nota}

        case _:
            r_dict = {"estado": "error", "mensaje": "modo seleccionado no es valido"}

    return r_dict

def client_handler():
    ...

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000) #o se puede usar ("localhost") en vez de los 0s. El primero es la IP y el segundo el puerto
    
    print(f"Levantando el servidor en {server_address[0]}, con puerto {server_address[1]}")
    
    sock.bind(server_address)

    sock.listen(5) #cuantos clientes van a escuchar

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept() #mi codigo no va a avanzar mas de esta linea hasta que el cliente acceda
        print(f"Conexion de {client_address[0]}:{client_address[1]}")

        t = Thread(target = client_handler, args = ())