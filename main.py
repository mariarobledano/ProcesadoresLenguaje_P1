from scanner import construir_scanner

lexer = construir_scanner()

with open('entrada.txt', 'r') as f:
    data = f.read()

lexer.input(data)

print("Tokens reconocidos:")
for tok in lexer:
    print(tok)
