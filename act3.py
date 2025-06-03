def areaTriangulo(base, altura):
    return (base * altura) / 2
def datos():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    resultado = areaTriangulo(base, altura)
    print(f"El área del triángulo es: {resultado:.2f} unidades cuadradas")
datos()