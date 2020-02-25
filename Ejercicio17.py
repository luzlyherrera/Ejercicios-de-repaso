# Escribir un programa que detecte si se han introducido en orden creciente tres numeros introducidos por el usuario
print("introduzca 3 numeros")
a=int(input())
b=int(input())
c=int(input())
if a < b < c:
    print("Los números estan ordenados en orden creciente")
else:
    print("Los numeros no estan en orden creciente")