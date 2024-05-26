import time
import gzip
import bz2
import os
import random

def generate_text_file(file_path, size_kb):
  
  for _ in range(10):
    file_name = f"{file_path}{size_kb[_]}KB.txt"
    chars = f"{''.join(chr(random.randint(32,126)) for i in range(size_kb[_] * 1024))}"
    with open(file_name, "w+") as f:
      f.write(chars)

def generate_binary_file(file_path, size_kb):
   
   for _ in range(10):
    file_name = f"{file_path}{size_kb[_]}KB.bin"
    fila = os.urandom(size_kb[_] * 1024)
    with open(file_name, "wb") as f:
      f.write(fila)  

def compress_file_gzip(input_file, output_file):
    
    tic = time.perf_counter()
    with open(input_file, 'rb') as f_in, gzip.open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)
    toc = time.perf_counter()
    exec_time = toc - tic
    return exec_time

def decompress_file_gzip(input_file, output_file):

    tic = time.perf_counter()
    with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)
    toc = time.perf_counter()
    exec_time = toc - tic
    return exec_time

def simulate_sensor_data():
  Temperatura = random.random()*10 + 20
  Humedad = random.random()*40 + 30
  Voltage = random.random()*0.1 + 4.95
  Corriente = random.random()*5 + 15

  return Temperatura, Humedad, Voltage, Corriente

