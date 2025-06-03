def multi(a, b):
    if a%b == 0:
        return (f"{a} es multiplo de {b}.")
    else:
        return (f"{a} no es multiplo de {b}.")
def act():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    resultado = multi(a, b)
    print(resultado)
act()