import ply.yacc as yacc
from scanner import tokens
import math

# Reglas de precedencia (para operaciones)
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
)

# Variable global de memoria
memory = 0  

# Definir operaciones matemáticas en notación polaca
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

def p_expresion_binario(p):
    'expresion : BINARIO'
    p[0] = p[1]

def p_expresion_hexadecimal(p):
    'expresion : HEXADECIMAL'
    p[0] = p[1] 

# Manejo de infinito y nan
def p_expresion_inf_nan(p):
    '''expresion : INF
                 | NAN'''
    p[0] = p[1]

# Manejo de MEMORY
def p_asignacion_memory(p):
    'expresion : MEMORY IGUAL expresion'
    global memory
    memory = p[3]
    p[0] = memory  

def p_expresion_memory(p):
    'expresion : MEMORY'
    global memory
    p[0] = memory  

# Manejo de números negativos (operador unario NEG)
def p_expresion_negativa(p):
    'expresion : NEG expresion'
    p[0] = -p[2]

# Manejo de errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

# Construir el parser
def construir_parser():
    return yacc.yacc()
