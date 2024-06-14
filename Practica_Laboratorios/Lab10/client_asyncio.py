import asyncio

# - Esta función asíncrona toma un writer (que es un objeto de escritura de conexión) y un msg (mensaje) como parámetros.
# - Convierte el mensaje en una secuencia de bytes utilizando la codificación "utf-8".
# - Escribe el mensaje codificado en el flujo de salida (writer.write(msg_bytes)).
# - Usa await writer.drain() para asegurarse de que todos los datos se hayan enviado.

async def send(writer, msg):
    print(f"Enviando mensaje: {msg}")
    msg_bytes = msg.encode("utf-8")
    writer.write(msg_bytes)
    await writer.drain()

# Esta función asíncrona toma un reader (que es un objeto de lectura de conexión) como parámetro.
# Espera a recibir una línea de respuesta del servidor (await reader.readline()).
# Decodifica los bytes recibidos en una cadena usando "utf-8".
# Devuelve la cadena decodificada.

async def recv(reader):
    print("Esperando respuesta")
    result_bytes = await reader.readline()
    print(f"recibi en bytes {result_bytes}")
    result = result_bytes.decode("utf-8")

    return result

# Esta función asíncrona simula un cliente que se conecta a un servidor en localhost en el puerto 5500.
# Imprime un mensaje indicando que está intentando conectarse.
# Usa await asyncio.open_connection para abrir una conexión al servidor, obteniendo objetos reader y writer.
# Envia un mensaje al servidor usando la función send, pasando writer y un mensaje que incluye el índice del cliente (idx).
# Espera y recibe una respuesta del servidor usando la función recv.
# Cierra la conexión usando writer.close() y espera a que se cierre completamente con await writer.wait_closed().
# Devuelve la respuesta recibida del servidor.

async def client(idx):
    server_address = ("localhost", 5500)
    print(f"Conectando a {server_address[0]}:{server_address[1]}")
    reader, writer = await asyncio.open_connection(server_address[0], server_address[1])
    print("Conectado")
    await send(writer, f"Hola mundo! desde cliente {idx}")
    
    res = await recv(reader)

    print("cerrando la conexion")
    writer.close()
    await writer.wait_closed()

    return res

# Esta función asíncrona principal ejecuta 10 instancias de la función client concurrentemente usando asyncio.gather.
# asyncio.gather recoge las tareas asíncronas (las 10 llamadas a client) y espera a que todas se completen.
# Devuelve una lista de resultados de cada cliente.

async def main():
    res = await asyncio.gather(*(client(idx + 1) for idx in range(10)))

    return res

# Este bloque asegura que el script se ejecute solo si se invoca directamente, no si se importa como un módulo.
# Ejecuta la función main usando asyncio.run para iniciar el bucle de eventos y esperar a que todas las tareas se completen.
# Imprime el primer mensaje recibido por el primer cliente (indicando que todos los clientes recibirán sus mensajes, pero solo el primero se muestra aquí).

if __name__ == '__main__':
    mensajes = asyncio.run(main())

    print(f"Cliente recibio el mensaje: {mensajes[0]}")