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
                print(variables[value])

            else:
                print(value)

        # Addition Print
        elif node["type"] == "print_add":

            left = variables[node["left"]]
            right = variables[node["right"]]

            print(left + right)