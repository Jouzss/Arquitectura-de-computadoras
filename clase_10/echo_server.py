#cualquier interaccion fuera del CPU y memoria es una operacion entrada/salida.
#el CPU espera mientras la operacion E/S se reaLiza, lo cual toma mucho tiempo.
#socket: estructura logica que empareja una direccion IP con un puerto. Agrupacion de esa sola IP (multiples IPs por cada interfaz)
#topologia: cliente - servidor. El servidor esta constantemente escuchando. 
#Cliente: abre socket y envía datos -> Servidor: hace eco de lo que recibe (retorna los mismos datos)
# 1 sola IP, 65535 puertos posibles
import socket

SOCK_BUFFER = 1024

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
                    conn.sendall(dato)
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