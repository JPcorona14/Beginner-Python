import art

print(art.logo)

print("Welcome to the Calculator")



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b



operators = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide 
    }




def calculator():
    cont = True
    item1 = float(input("Please type the first number you will be using?\n"))
    
    while cont:
        action = input("Please pick an operation to use?\n")
        item2 = float(input("Please type the next number you will be using?\n"))
        answer = operators[action](item1, item2)
        print(f"{item1} {action} {item2} = {answer}")

        if input("Please type y if you would like to continue operation or n if you would like to start new?\n").lower() == "y":
            item1 = answer
        else:
            cont = False
            calculator()

calculator()
