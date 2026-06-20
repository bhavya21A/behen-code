def tokenize(code):

    tokens = []

    for line in code.splitlines():

        line = line.strip()

        if not line:
            continue

        parts = line.split()

        for part in parts:
            tokens.append(part)

    return tokens