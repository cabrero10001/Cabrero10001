def calculator (a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division por cero"
    else:
        return "Error: operacion no valida"
def act():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    operation = input("Ingrese la operacion (+, -, *, /): ")
    resultado = calculator(a, b, operation)
    print(f"El resultado de {a} {operation} {b} es: {resultado}")
act()