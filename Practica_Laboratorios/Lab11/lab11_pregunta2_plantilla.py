import asyncio
import time

rutas_posibles = [
	"LPC",
	"LPAHC",
	"LPAOHC",
	"LOAPC", 
	"LOAHC",
	"LOHC",
	"LOHAPC", 
	"LAPC",
	"LAOHC",
	"LAHC"
]

distancias = {
	"LP": 14,
	"LA": 10,
	"LO": 8,
	"PC": 18,
	"PA": 3,
	"OA": 25,
	"OH": 5,
	"AP": 3,
	"AO": 25,
	"AH": 2,
	"HA": 2,
	"HC": 10
}

async def Tiempo_ruta(rutas):
	
	lista_char = list(rutas)
	pares_char = []
	dis_count = 0

	for idx in range(len(lista_char) - 1):
		par = lista_char[idx] + lista_char[idx + 1]
		pares_char.append(par)

	for u_par in pares_char:
		if u_par in distancias:
			distancia = distancias[u_par]
			dis_count += distancia
			await asyncio.sleep(distancia * (1e-3))

	print(f"Tiempo en ruta {rutas}: {dis_count}")
	
	return dis_count, rutas

async def main():

	tic = time.perf_counter()
	resultados = await asyncio.gather(*(Tiempo_ruta(rutas) for rutas in rutas_posibles))
	toc = time.perf_counter()

	lista = [res[0] for res in resultados] 
	ruta = [res[1] for res in resultados]

	for idx in range(len(lista)):
		if (idx == 0):
			s_ruta_dis = lista[idx]
			s_ruta_name = ruta[idx]
		elif (s_ruta_dis > lista[idx]):
			s_ruta_dis = lista[idx]
			s_ruta_name = ruta[idx]
	
	print(f"La ruta más corta es {s_ruta_name} con una duración de {s_ruta_dis} horas.")
	print(f"Tiempo de ejecución: {toc - tic} s")

if __name__ == "__main__":
	asyncio.run(main())
