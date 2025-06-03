def conversion(a):
    formula = (a *1.8)+32
    return formula
def datos():
    a = float(input("Ingrese la temperatura en grados Celsius: "))
    resultado = conversion(a)
    print(f"La temperatura en grados Fahrenheit es: {resultado:.2f}°F")
datos()