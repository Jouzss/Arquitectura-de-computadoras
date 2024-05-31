#cualquier interaccion fuera del CPU y memoria es una operacion entrada/salida.
#el CPU espera mientras la operacion E/S se reaLiza, lo cual toma mucho tiempo.
#socket: estructura logica que empareja una direccion IP con un puerto. Agrupacion de esa sola IP (multiples IPs por cada interfaz)
#topologia: cliente - servidor. El servidor esta constantemente escuchando. 
#Cliente: abre socket y envía datos -> Servidor: hace eco de lo que recibe (retorna los mismos datos)
# 1 sola IP, 65535 puertos posibles
import json
import socket

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

        try:
            while True:
                dato = conn.recv(SOCK_BUFFER)

                if dato:
                    print(f"Recibi: {dato}")
                    d = json.loads(dato)
                    if "Codigo" in d.keys() and "modo" in d.keys():
                        notas = busca_info(d["Codigo"])
                        if len(notas) > 0:
                            msg_dict = empaqueta_datos(notas, d["modo"])
                        else:
                            msg_dict = {"estado": "error", "mensaje": "No existen registros para el codigo indicado"}
                    else:
                        msg_dict = {"estado": "error", "mensaje": "Solicitud enviada en formato incorrecto"}
                    conn.sendall(json.dumps(msg_dict).encode("utf-8"))
                else:
                    print("No hay mas datos")
                    break
        except ConnectionResetError: #ecept exception: | eso chapa todas las excepciones, pero no es recomendable. Son constantes, no etiquetas.
            print("El cliente cerro la conexion de manera abrupta")
        finally:
            print("Cerrando la conexion")
            conn.close()

#python no compila, C si lo hace. Python llama a otro programa (interprete) el cual transforma a codigo maquina. Por esta razon, toma mucho tiempo.
#desventaja: hay errores que no se perciben hasta la ejecucion. En C esto si se ve