def bonificacion(a):
    valorBonificacion = a * .10
    total = a + valorBonificacion
    return total
def main():
    a = float(input("Ingrese el valor del salario: "))
    total = bonificacion(a)
    print(f"El total del salario con bonificacion es: {total:.2f}")
main()