def parse(tokens):

    ast = []

    i = 0

    while i < len(tokens):

        # Variable declaration
        if tokens[i] == "rakho":

            ast.append({
                "type": "variable",
                "name": tokens[i + 1],
                "value": tokens[i + 3]
            })

            i += 4

        # Print statement
        elif tokens[i] == "bolo":

            # Addition expression
            if i + 3 < len(tokens) and tokens[i + 2] == "+":

                ast.append({
                    "type": "print_add",
                    "left": tokens[i + 1],
                    "right": tokens[i + 3]
                })

                i += 4

            # Normal print
            else:

                ast.append({
                    "type": "print",
                    "value": tokens[i + 1]
                })

                i += 2

        else:
            i += 1

    return ast