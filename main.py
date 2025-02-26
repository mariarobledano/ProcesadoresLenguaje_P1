import re
from scanner import construir_scanner
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
