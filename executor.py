def execute(ast):

    variables = {}

    for node in ast:

        # Variable Declaration
        if node["type"] == "variable":

            value = node["value"]

            if value.isdigit():
                value = int(value)

            variables[node["name"]] = value

        # Normal Print
        elif node["type"] == "print":

            value = node["value"]

            if value in variables:
                print(f"💖 {variables[value]}")
            else:
                print(f"💖 {value}")

        # Addition Print
        elif node["type"] == "print_add":

            try:

                left = variables[node["left"]]
                right = variables[node["right"]]

                print(f"✨ {left + right}")

            except KeyError as e:

                print(
                    f"😭 Behen, '{e.args[0]}' naam ka variable nahi mila."
                )

            except Exception:

                print(
                    "🚩 Behen, kuch toh gadbad ho gayi addition karte waqt."
                )

