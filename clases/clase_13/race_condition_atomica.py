import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, nombre):
        print(f"Thread [{nombre}]: iniciando actualización")
        local_copy = self.value
        local_copy += 1
        self.value = local_copy
        time.sleep(0.1)
        print(f"Thread [{nombre}]: finalizando la actualización")

if __name__ == '__main__':
    workers = 5
    tasks = workers

    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    with concurrent.futures.ThreadPoolExecutor(max_workers = workers) as executor:
        for index in range(tasks):
            executor.submit(db.update, index)

    print(f"Valor final de la base de datos: {db.value}")