num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
op = input("Operator (+, -, *, /, %, //, **): ")

def switch(num1, num2, op):
    try:
        if op == '+':
            return f"{num1} {op} {num2} = {num1 + num2}"
        elif op == '-':
            return f"{num1} {op} {num2} = {num1 - num2}"
        elif op == '*':
            return f"{num1} {op} {num2} = {num1 * num2}"
        elif op == '/':
            return f"{num1} {op} {num2} = {num1 / num2}"
        elif op == '%':
            return f"{num1} {op} {num2} = {num1 % num2}"
        elif op == '//':
            return f"{num1} {op} {num2} = {num1 // num2}"
        elif op == '**':
            return f"{num1} {op} {num2} = {num1 ** num2}"
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

result = switch(num1, num2, op)
print(result)

