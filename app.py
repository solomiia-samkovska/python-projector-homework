def sum(a, b):
    return a + b

def sub(a,b):
    return a - b

def calc():
    operation = input("Select operation. For addition enter '+', for subtraction enter '-': ")
    if operation not in ["+", "-"]:
        print("Invalid input")
        return
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    match operation:
        case "+":
            print(f"{a} + {b} = ", sum(a,b))
        case "-":
            print(f"{a} - {b} = ", sub(a,b))

calc()

