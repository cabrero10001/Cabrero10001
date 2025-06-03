def mayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
def act():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))
    resultado = mayor(a, b, c)
    print(f"El numero mayor entre {a}, {b} y {c} es: {resultado}")
act()