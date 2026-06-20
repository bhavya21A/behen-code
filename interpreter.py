from lexer import tokenize
from parser import parse
from executor import execute

print("""
🌸━━━━━━━━━━━━━━━━━━━━━━━━━━🌸
Welcome to BehenCode
🌸━━━━━━━━━━━━━━━━━━━━━━━━━━🌸

💅 Code karo.
🐛 Bugs pakdo.
👑 Slay karo.
""")

with open("hello.bhn", "r", encoding="utf-8") as file:
    code = file.read()

print("\n📄 CODE:")
print(code)

print("\n🔍 TOKENIZING...")
tokens = tokenize(code)
print("TOKENS:", tokens)

print("\n🧠 BUILDING AST...")
ast = parse(tokens)
print("AST:", ast)

print("\n🌸━━━━━━━━━━━━━━━━━━━━━━━━━━🌸")
print("💖 OUTPUT")
print("🌸━━━━━━━━━━━━━━━━━━━━━━━━━━🌸")

execute(ast)

print("\n✨ Program khatam, behen!")
