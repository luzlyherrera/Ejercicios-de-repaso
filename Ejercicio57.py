# Escribir un programa que cuente las mayusculas de una cadena de caracteres
frase=(input("Introduce una frase para poder contar las mayusculas: "))
cont=0
for i in frase:
    if i !=i.lower():
        cont+=1
print(cont)