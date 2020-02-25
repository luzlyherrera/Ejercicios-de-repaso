# Escribir un programa que mediante una funcion calcule el resultado de restar el doble de un numero a su cuadrado
def resultado(num):
    resta=2*num-pow(num,2)
    print(resta)

resultado(num=int(input("Ingrese un numero: " )))