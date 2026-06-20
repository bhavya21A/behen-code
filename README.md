# 🌸 BehenCode

BehenCode is a fun beginner-friendly programming language inspired by Bhai Lang.

The goal of BehenCode is to learn how programming languages work by building one from scratch using Python.

---

## Current Features

✅ Variables (`rakho`)

✅ Printing (`bolo`)

✅ Numbers

✅ Addition (`+`)

✅ Lexer

✅ Parser

✅ AST (Abstract Syntax Tree)

✅ Executor

---

## Project Structure

```text
behen-code/

├── lexer.py
├── parser.py
├── executor.py
├── interpreter.py
├── hello.bhn
├── README.md
└── examples/
```

---

## Example Program

```behen
namaste behen

rakho x = 10
rakho y = 20

bolo x + y

alvida behen
```

Output:

```text
30
```

---

## How It Works

BehenCode follows a simple interpreter architecture:

```text
Source Code
    ↓
Lexer
    ↓
Parser
    ↓
AST
    ↓
Executor
    ↓
Output
```

---

## Running BehenCode

Run the interpreter:

```bash
python interpreter.py
```

---

## Example AST

Source Code:

```behen
rakho marks = 85

bolo marks
```

Generated AST:

```python
[
    {
        "type": "variable",
        "name": "marks",
        "value": "85"
    },
    {
        "type": "print",
        "value": "marks"
    }
]
```

---

## Upcoming Features

* `agar` (if statements)
* `warna` (else statements)
* `ghoomo` (loops)
* Functions (`kaam`)
* String operations
* Command Line Interface

Example future syntax:

```behen
rakho marks = 85

agar marks >= 40
bolo "Pass"
warna
bolo "Fail"
bas
```

---

## Author

Created by Bhavya as a learning project to understand interpreters, parsers, and programming language design.
