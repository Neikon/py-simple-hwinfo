import subprocess
import re
import os
import psutil
import platform
from tqdm import tqdm
from time import sleep
from tabulate import tabulate

def get_msinfo32_output():
    if not os.path.exists("msinfo.txt"):
        command = "msinfo32 /report msinfo.txt"
        subprocess.run(command, shell=True)
    with open("msinfo.txt", "r", encoding="utf-16") as file:
        return file.read()

def get_motherboard_info(msinfo32_output):
    pattern = re.compile(r"Producto de placa base\s*(.+)", re.IGNORECASE)
    match = pattern.search(msinfo32_output)
    return match.group(1) if match else None

def get_bios_version(msinfo32_output):
    pattern = re.compile(r"Versión y fecha de BIOS\s*(.+)", re.IGNORECASE)
    match = pattern.search(msinfo32_output)
    return match.group(1) if match else None

def get_processor_info(msinfo32_output):
    pattern = re.compile(r"Procesador\s*(.+)", re.IGNORECASE)
    match = pattern.search(msinfo32_output)
    return match.group(1) if match else None

def get_ram_info():
    ram = psutil.virtual_memory()
    total_ram = ram.total // (1024 ** 3)
    return f"{total_ram} GB"

def get_gpu_model():
    if platform.system() == "Windows":
        if not os.path.exists("dxdiag.txt"):
            command = "dxdiag /t dxdiag.txt"
            subprocess.run(command, shell=True)
        with open("dxdiag.txt", "r") as file:
            dxdiag_output = file.read()
        gpu_model = re.search(r"Card name:\s*(.+)", dxdiag_output)
        return gpu_model.group(1) if gpu_model else None
    else:
        return "Sistema operativo no soportado"

print("Obteniendo datos, por favor espere...")
for i in tqdm(range(100)):
    msinfo32_output = get_msinfo32_output()
    motherboard_info = get_motherboard_info(msinfo32_output)
    bios_version = get_bios_version(msinfo32_output)
    processor_info = get_processor_info(msinfo32_output)
    ram_info = get_ram_info()
    gpu_model = get_gpu_model()

table_data = [
    ["Procesador", processor_info],
    ["Placa base", motherboard_info],
    ["Versión de BIOS", bios_version],
    ["RAM", ram_info],
    ["Modelo de GPU", gpu_model],
]

table = tabulate(table_data, headers=["Componente", "Información"], tablefmt='grid', colalign=("left", "left"))

print(table)

input("\nPresione Enter para salir...")