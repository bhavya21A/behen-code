from lexer import tokenize
from parser import parse
from executor import execute

with open("hello.bhn", "r", encoding="utf-8") as file:
    code = file.read()

print("CODE:")
print(code)

tokens = tokenize(code)
print("TOKENS:", tokens)

ast = parse(tokens)
print("AST:", ast)

print("OUTPUT:")
execute(ast)