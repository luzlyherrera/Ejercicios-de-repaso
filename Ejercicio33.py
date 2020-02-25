# Escribir un programa que calcule la suma de los numeros hasta un numero dado (introducido por el usuario)
print("Introduzca un numero")
num=int(input())
suma=0
for i in range(1,(num+1)):
    suma=suma+i
print(suma)