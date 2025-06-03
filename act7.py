def anios(a):
    meses = a * 12
    dias = a * 365
    return meses, dias
def act():
    a = int(input("Ingrese la cantidad de años: "))
    meses, dias= anios(a)
    print(f"{a} años son {meses} meses y {dias} dias.")
act()