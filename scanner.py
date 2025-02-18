"""
Práctica 1 Procesadores del Lenguaje- Introducción al entorno 
Luis del Valle 
Maria Robledano
"""
import ply.lex as lex

tokens = [
    'ENTERO', 'REAL', 'BINARIO', 'HEXADECIMAL',
    'MAS', 'MENOS', 'MULT', 'DIV',
    'EXP', 'LOG', 'SIN', 'COS'
]

def t_COMMENT_SINGLE(t):
    r'\#.*'
    pass

def t_COMMENT_MULTI(t):
    r"'''(.|\n)*?'''"
    pass

def t_HEXADECIMAL(t):
    r'0x[A-F0-9]+'
    return t

def t_BINARIO(t):
    r'0b[01]+'
    return t

def t_REAL(t):
    r'\d+\.\d+'
    return t

def t_ENTERO(t):
    r'\d+'
    return t

t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'

t_EXP = r'exp'
t_LOG = r'log'
t_SIN = r'sin'
t_COS = r'cos'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

def construir_scanner():
    return lex.lex()
