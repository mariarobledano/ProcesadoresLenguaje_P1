"""
PARSER (ANALIZADOR SINTÁCTICO)

Este fichero contiene el analizador sintáctico del programa.
Su función es interpretar los tokens generados por el lexer y evaluar expresiones matemáticas.

Funcionalidades:
- Maneja operaciones matemáticas en notación polaca (prefija).
- Implementa reglas gramaticales para operadores y funciones.
- Procesa números y valores especiales (inf, nan).
- Implementa la memoria (`MEMORY`) como una variable almacenable.
- Detecta errores de sintaxis.

"""

import ply.yacc as yacc
from lexer import tokens
import math

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
)

memory = 0  

def p_expresion_operacion(p):
    '''expresion : MAS expresion expresion
                 | MENOS expresion expresion
                 | MULT expresion expresion
                 | DIV expresion expresion'''
    if p[1] == '+':
        p[0] = p[2] + p[3]
    elif p[1] == '-':
        p[0] = p[2] - p[3]
    elif p[1] == '*':
        p[0] = p[2] * p[3]
    elif p[1] == '/':
        p[0] = p[2] / p[3] if p[3] != 0 else float('nan')  # Evitar división por 0

# Definir funciones matemáticas
def p_expresion_funcion(p):
    '''expresion : EXP expresion
                 | LOG expresion
                 | SIN expresion
                 | COS expresion'''
    if p[1] == 'exp':
        p[0] = math.exp(p[2])
    elif p[1] == 'log':
        p[0] = math.log(p[2]) if p[2] > 0 else float('nan')  # Evitar log de números negativos
    elif p[1] == 'sin':
        p[0] = math.sin(p[2])
    elif p[1] == 'cos':
        p[0] = math.cos(p[2])

def p_expresion_numero(p):
    '''expresion : ENTERO
                 | REAL'''
    p[0] = float(p[1]) 

def p_expresion_valores_especiales(p):
    '''expresion : BINARIO
                 | HEXADECIMAL
                 | INF
                 | NAN'''
    p[0] = p[1]


def p_asignacion_memory(p):
    'expresion : MEMORY IGUAL expresion'
    global memory
    memory = p[3]
    p[0] = memory  

def p_expresion_memory(p):
    'expresion : MEMORY'
    global memory
    p[0] = memory  

def p_expresion_negativa(p):
    'expresion : NEG expresion'
    p[0] = -p[2]

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

def construir_parser():
    return yacc.yacc()
