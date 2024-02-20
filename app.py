def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def calc():
    operation = input("Select operation:\n for Addition enter '+'\n for Subtraction enter '-'\n for Multiplication enter '*'\n for Division enter '/'")
    
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid input")
        return
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    match operation:
        case "+":
            print(f"{a} + {b} = ", sum(a,b))
        case "-":
            print(f"{a} - {b} = ", sub(a,b))
        case "*":
            print(f"{a} * {b} = ", mult(a,b))
        case "/":
            print(f"{a} / {b} = ", div(a,b))

calc()

