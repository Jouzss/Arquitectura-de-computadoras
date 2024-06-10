import asyncio
import json
import socket

SOCKET_BUFFER = 1024  

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

def procesa_mensaje(dato: bytes) -> dict:
    try:
        msg_cliente = json.loads(dato)
        if "Codigo" in msg_cliente.keys() and "modo" in msg_cliente.keys():
            notas = busca_info(d["Codigo"])
            if len(notas) > 0:
                msg_dict = empaqueta_datos(notas, msg_cliente["modo"])
            else:
                msg_dict = {"estado": "error", "mensaje": "No existen registros para el codigo indicado"}
        else:
            msg_dict = {"estado": "error", "mensaje": "Solicitud enviada en formato incorrecto"}
    except json.decoder.JSONDecodeError:
        msg_dict = {"estado": "error", "mensaje": "No se pudo codificar el mensaje JSON"}

    return msg_dict

async def handle_client(reader, writer):
    print("Cliente conectado")
    msg_bytes = await reader.read(SOCKET_BUFFER) #equivalente al conn.recv
    print(f"Recibi {msg_bytes}")
    if msg_bytes:
        msg_respuesta = procesa_mensaje(msg_bytes)
        msg_respuesta_str = json.dumps(msg_respuesta)

        await writer.write(msg_respuesta_str.encode("utf-8"))
        await writer.drain() 

    writer.close()
    await writer.wait_closed()
    print("conexion cerrada")

async def main():
    server_address = ("0.0.0.0", 5000)

    server = await asyncio.start_server(handle_client, server_address[0], server_address[1])

    async with server:
        print("Empezando servidor...")
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())