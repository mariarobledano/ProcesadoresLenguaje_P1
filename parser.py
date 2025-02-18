import ply.yacc as yacc
from scanner import tokens

# Reglas de Precedencia (aunque en notación polaca no son necesarias)
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
)

# Definimos las reglas de la gramática en notación polaca (prefija)
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
        p[0] = p[2] / p[3]

def p_expresion_funcion(p):
    '''expresion : EXP expresion
        | LOG expresion
        | SIN expresion
        | COS expresion'''
    import math
    if p[1] == 'exp':
        p[0] = math.exp(p[2])
    elif p[1] == 'log':
        p[0] = math.log(p[2])
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
    p[0] = int(p[1][2:], 2)

def p_expresion_hexadecimal(p):
    'expresion : HEXADECIMAL'
    p[0] = int(p[1], 16)

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

# Constructor del parser
def construir_parser():
    return yacc.yacc()

