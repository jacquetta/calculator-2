"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# input_num = input("Enter problem: ")
# tokens = input_num.split(" ")
# for i in range(1, len(tokens)):
#     tokens[i] = int(tokens[i])

while True: 
    input_num = input("Enter problem: ")
    tokens = input_num.split(" ")
    if tokens[0] != 'q':
        for i in range(1, len(tokens)):
            tokens[i] = int(tokens[i])
        print(tokens)

       
        if tokens[0] == "+":
            print(add(tokens[1], tokens[2]))
        elif tokens[0] == "-":
            print(subtract(tokens[1], tokens[2]))
        elif tokens[0] == "*":
            print(multiply(tokens[1], tokens[2]))
        elif tokens[0] == "/":
            print(divide(tokens[1], tokens[2]))
        elif tokens[0] == "square":
            print(square(tokens[1]))
        elif tokens[0] == "cube":
            print(cube(tokens[1]))
        elif tokens[0] == "pow":
            print(power(tokens[1], tokens[2]))
        elif tokens[0] == "mod":
            print(mod(tokens[1], tokens[2]))

    else: 
        print('quit')
        break 
    