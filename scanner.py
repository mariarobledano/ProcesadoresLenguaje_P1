"""
SCANNER (LEXER)

Este fichero contiene el analizador léxico (lexer) del programa.
Su función es dividir la entrada en tokens y filtrar elementos no deseados como comentarios.

Funcionalidades:
- Reconoce números (enteros, reales, binarios, hexadecimales).
- Reconoce operadores matemáticos (+, -, *, /).
- Soporta funciones matemáticas (sin, cos, log, exp).
- Maneja valores especiales (inf, nan).
- Implementa una variable de memoria (MEMORY) que almacena valores.
- Ignora comentarios de una línea y multilínea.

"""


import ply.lex as lex

tokens = [
    'ENTERO', 'REAL', 'BINARIO', 'HEXADECIMAL',
    'MAS', 'MENOS', 'MULT', 'DIV',
    'EXP', 'LOG', 'SIN', 'COS', 'INF', 'NAN', 
    'MEMORY', 'IGUAL', 'NEG'
]


def t_COMMENT_SINGLE(t):
    r'\#.*'
    pass

def t_COMMENT_MULTI(t):
    r"'''[\s\S]*?'''"
    pass

def t_HEXADECIMAL(t):
    r'0x[A-F0-9]+'
    t.value = int(t.value, 16)
    return t

def t_BINARIO(t):
    r'0b[01]+'
    t.value = int(t.value[2:], 2)
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_INF(t):
    r'inf'
    t.value = float('inf')
    return t

def t_NAN(t):
    r'nan'
    t.value = float('nan')
    return t

def t_MEMORY(t):
    r'MEMORY'
    return t

t_IGUAL = r'='

t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'

t_EXP = r'exp'
t_LOG = r'log'
t_SIN = r'sin'
t_COS = r'cos'

def t_NEG(t):
    r'neg'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

def construir_scanner():
    return lex.lex()
