#Evaluar tiempo de ejecución para un programa en distintos escenarios
# Nuestro archivo simula una base de datos. 
# JSON: Java Script Object notetion
# {
#     'codigo': <valor_codigo>
#     'modo'  : <valor> --> 'cliente', 'servidor' 
# }
# Evaluamos tiempo de ejecución del cliente, porque el servidor es una caja negra. 

# @Jouzss ➜ /workspaces/Arquitectura-de-computadoras/clase_10 (main) $ python
# Python 3.10.13 (main, May 14 2024, 22:40:16) [GCC 9.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> data_bytes = b'{"codigo": "20210001", "modo": "cliente"}'
# >>> data_bytes
# b'{"codigo": "20210001", "modo": "cliente"}'
# >>> import json
# >>> json.loads(data_bytes)
# {'codigo': '20210001', 'modo': 'cliente'}
# >>> d = json.loads(data_bytes)
# >>> d
# {'codigo': '20210001', 'modo': 'cliente'}
# >>> d["codigo"]
# '20210001'
# >>> d["modo"]
# 'cliente'
# >>> d["extra"] = "hola mundo"
# >>> d
# {'codigo': '20210001', 'modo': 'cliente', 'extra': 'hola mundo'}
# >>> type(d)
# <class 'dict'>
# >>> json.dumps(d)
# '{"codigo": "20210001", "modo": "cliente", "extra": "hola mundo"}'
# >>> s = json.dumps(d)
# >>> type(s)
# <class 'str'>
# >>> s.encode("utf-8")
# b'{"codigo": "20210001", "modo": "cliente", "extra": "hola mundo"}'
# >>> exit()

#                                                                           TAREA
# Evaluar tiempos de ejecución. calculo de la nota. cuanto tarda el calcular la nota, respecto a la operación a entrada y salida, pero que tan distinto? Creamos dos modos de operación,
# servidor y cliente. servidor nos dará tiempos completos. Tiempos totales de ejecución del mensaje de ida, cálculo y el mensaje de vuelta. Tambien queremos los tiempos solo de ida y solo
# de vuelta. El tiempo de ida es un poco más grande, en cambio en el retorno, si el modo es cliente, el retorno es más grande y si el modo es servidor, el valor de retorno debe ser más corto
# no basta con una prueba, debemos probar varias veces y sacar valores estadísticos para poder sacar valores exactos. Ya tenemos el código del programa y ahora debemos definir y diseñar bien
# el experimento. 