# Socket: Elemento que utiliza software para establecer una conexión de red basada en un protocolo IP.
# 2 elementos: Dirección IP y el puerto que se utilizara para transportar el paquete

# Un servidor establece una puerta de entrada y salida. Tenemos distintos pasos
# Servidor: socket() -> bind() -> listen() -> accept() [call block] [wait for connection] [connection established] -> recv() [process request] -> send()  [response] -> recv()
# Cliente:  socket()                       -> connect() [call block] [establish connection]                        -> send() [request]                               -> recv()

######### Servidor #########

# socket():     Un nodo atiende a los requerimientos de otro nodo. Un servidor levanta un socket. Socket es una combinación de dirección de red y puerto.
#               Es decir establece una puerta de entrada y salida
# bind():       Asocia este socket con un recurso físico. La tarjeta ethernet de este equipo. Bind toma este socket y lo dispone al exterior.
# listen():     Coloca toda esta construcción y luego escucha. El servidor "escucha" conexiones entrantes.
# accept():     Pone todo esto en modo blocking (modo blocking quiere decir que el sistema se queda esperando a que algo suceda). Aquí se detiene el script
#               que va a correr en el servidor esperando conexiones entrantes.

######### Cliente #########

# socket():     Lo que el cliente va a hacer es levantar un socket.
# connect():    Lo que va a hacer el cliente será conectarse a un servidor. Es decir connect tendrá como atributos los datos del servidor al que se quiere
#               conectar. Cuando llega esa conexion, el metodo accept se rompe y es aceptada. Se activa un modo blocking, hasta que el servidor acepta esta
#               conexión.

######### Servidor #########

# accept():     Ahora el servidor conoce el socket que ha accedido y lo registra. Ahora puede enviarle información. 

# Ahora puedo realizar 2 cosas: El cliente puede enviar información o puede recibir y de igual manera el servidor.

# recv():       Siempre esta función es una función blocking. Esto quiere decir que si yo invoco recv(), estoy esperando algo del otro lado enviado con send().
# send():       Se usa con el servidor o el cliente. Se usa para enviar el paquete de información.

# No son procesos en paralelo, cuando solicita algo, espera a que sea recibido para continuar.