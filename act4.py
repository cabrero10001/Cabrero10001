def parImpares(n):
    if n%2 == 0:
        return True
    else:
        return False
def datos():
    n = int(input("Ingrese un número entero: "))
    if parImpares(n):
        print(f"El número {n} es par.")
    else:
        print(f"El número {n} es impar.")
datos()