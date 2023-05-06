# py-simple-hwinfo
Script Python para sacar informacion basica del hardware del pc en windows

Disclaimer: Este código y la descripción proporcionada fueron creados con la ayuda de una Inteligencia Artificial (IA) diseñada para asistir en la programación y redacción de documentación.

Este código en Python obtiene información sobre el sistema y sus componentes, como el procesador, la placa base, la versión de BIOS, la memoria RAM y el modelo de GPU en sistemas Windows. Utiliza las bibliotecas subprocess, re, os, psutil, platform, tqdm, time y tabulate.

La función get_msinfo32_output() genera un archivo de texto llamado "msinfo.txt" con la información del sistema utilizando el comando msinfo32 /report msinfo.txt. Luego, se utilizan expresiones regulares para extraer información relevante sobre la placa base, la versión de BIOS y el procesador en las funciones get_motherboard_info(), get_bios_version() y get_processor_info().

La información de la memoria RAM se obtiene utilizando la biblioteca psutil en la función get_ram_info(). Para obtener el modelo de GPU, se verifica si el sistema operativo es Windows utilizando el módulo platform. Si es Windows, se ejecuta el comando dxdiag /t dxdiag.txt para generar un archivo de texto con información del sistema, incluida la GPU. Luego, se extrae el modelo de GPU utilizando expresiones regulares en la función get_gpu_model(). Si el sistema operativo no es Windows, la función devuelve "Sistema operativo no soportado".

Se muestra una barra de progreso mientras se obtiene la información, gracias a la biblioteca tqdm. Al finalizar, se presenta la información en una tabla utilizando la biblioteca tabulate. El usuario debe presionar Enter para salir del programa.
