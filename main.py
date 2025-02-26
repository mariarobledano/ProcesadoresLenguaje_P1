"""
PROGRAMA PRINCIPAL

Este fichero ejecuta el lexer y el parser, procesando el contenido de `entrada.txt`.
Elimina comentarios antes de enviarlos al lexer para evitar errores.

Funcionalidades:
- Lee la entrada desde `entrada.txt`.
- Elimina comentarios antes del análisis.
- Procesa cada línea y muestra los resultados en la consola.

"""

import re
from lexer import construir_scanner
from parser import construir_parser

lexer = construir_scanner()
parser = construir_parser()


with open("entrada.txt", "r") as f:
    entrada = f.read()

entrada = re.sub(r"'''[\s\S]*?'''", "", entrada) 

lineas = entrada.strip().split("\n")
contador_linea = 1

for linea in lineas:
    linea = re.sub(r'\#.*', '', linea).strip()  
    if linea and not linea.isspace():  
        resultado = parser.parse(linea, lexer=lexer)
        if resultado is not None:
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            print(f"Resultado '{linea}' [Línea {contador_linea}]: {resultado}")
    contador_linea += 1
