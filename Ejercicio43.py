# Escribir un programa que llene una lista con los veite primeros numeros pares y calcule su suma
l=[]
suma=0
for i in range(2,21,2):
    l.append(i)
print(l)
for j in l:
    suma+=j
print(suma)
