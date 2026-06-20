from lexer import tokenize
from parser import parse
from executor import execute

with open("hello.bhn", "r", encoding="utf-8") as file:
    code = file.read()

tokens = tokenize(code)

ast = parse(tokens)

execute(ast)