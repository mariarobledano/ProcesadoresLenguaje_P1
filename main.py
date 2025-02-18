from scanner import construir_scanner
from parser import construir_parser

lexer = construir_scanner()
parser = construir_parser()

# Ejemplo de entrada en notación polaca (prefija)
entrada = """
+ 3 4
* + 3 4 2
sin 0.5
log 1
0b1010
0xA3
"""

lexer.input(entrada)

tokens = []
for tok in lexer:
    tokens.append(tok)

# Procesar línea por línea con contador
lineas = entrada.splitlines()
contador_linea = 1

for linea in lineas:
    if linea.strip():  # Evitar líneas vacías
        resultado = parser.parse(linea, lexer=lexer)
        if resultado is not None:
            # Mostrar enteros sin decimales
            if resultado.is_integer():
                resultado = int(resultado)
            print(f"Resultado '{linea.strip()}' [Línea {contador_linea}]: {resultado}")
    contador_linea += 1