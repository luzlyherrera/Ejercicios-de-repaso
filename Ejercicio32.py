# Escribir un programa que realice la pregunta ¿Desea continuar S/N? y wur no pare de hacerla hasta que el usuario teclee N
print("¿Desea continuar? S/N")
entrada=str(input())
while entrada=='S':
    print("¿Desea continuar? S/N")
    entrada=str(input())
print("Bye")
