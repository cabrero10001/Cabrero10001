def intercambio(a, b):
    return b, a
def act():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    a, b = intercambio(a, b)
    print(f"Los numeros intercambiados son: a={b} y b={a}")
act()