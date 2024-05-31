# E/S
# ¿Son necesarias? sí
# ¿Son deseables? 

# Tenemos un periferico conectado a un microcontrolador con un protocolo UART
# Uart tiene los siguientes datos:
# 9600, 8, N, 1
# 9600 baudios/segundo
# 8 longitud del mensaje
# N: Paridad nula
# 1 bit de parada
# ¿Cuanto tiempo le demora en enviar el mensaje?
# Para calcularlo necesitamos el tiempo que demora en enviar un bit

Tb = (1/9600)*1e6 #Tiempo en microsegundos
print(f"El tiempo por bit es {Tb} us")

# Luego necesitamos la cantidad de bits a transmitir

Nb = 10 # 1 bit de inicio + 8 bits de mensaje + 1 bit de parada

# Luego calculamos el tiempo total

T_tx = Tb * Nb

print(f"El tiempo en transmitir los datos es de {T_tx} us")