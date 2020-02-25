# Escribir un numero que calcule el factorial de un numero usando resursividad
def factorial (*n):
    for x in n:
        fac=1
    for y in range(1,x+1):
        fac=fac*y
    print(fac)
num=int(input("Ingresa numero entero\n"))
factorial(num)