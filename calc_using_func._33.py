def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("=== Calculator Using Functions ===")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("Choose: +  -  *  /")
op = input("Enter operation: ")

if op == "+":
    print(add(a, b))
elif op == "-":
    print(sub(a, b))
elif op == "*":
    print(mul(a, b))
elif op == "/":
    print(div(a, b))
else:
    print("Invalid operation")
