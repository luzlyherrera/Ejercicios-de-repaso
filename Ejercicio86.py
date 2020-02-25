# Escrbir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto
#import sys
archivo = open("archivo.txt", "w")
lista = []
for i in range (33,255):
    lista.append(str(chr(i).encode('utf-8'))+"\n")
archivo.writelines(lista)
archivo.close()
