#Funcion que llena el arreglo con números aleatorios
#Funcion que crea una copia original del arreglo 
#Funcion que muestra en pantalla en arreglo
#Funcion de ordena por burbuja
#Funcion de ordenar por seleccion
#Funcion de ordenar por insercion
#Funcion de ordenar por quirk-sort
#Funcion que muestra un menú de opciones 

import random

def arreglo(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0,100))
    return lista
 
def copiar(original):
    copia = []
    for i in range(len(original)):
        copia.append(original[i])
    return copia

def mostrar(lista):
    print("-------------")
    for i in range(len(lista)):
        print(lista[i])
    print("-------------")
def metodoBurbuja(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                mostrar(lista)
                print("----------------\n")
                
def metodoSeleccion(lista):
    for i in range(len(lista)-1,0,-1):
       posicionDelMayor=0
       for j in range(1,i+1):
           if lista[j]>lista[posicionDelMayor]:
               posicionDelMayor = j

       temp = lista[i]
       lista[i] = lista[posicionDelMayor]
       lista[posicionDelMayor] = temp
       mostrar(lista)
       print("----------------\n")
       
def metodoInsercion(lista):
    for i in range(len(lista)):
        for j in range(i,0,-1):
            if(lista[j-1] > lista[j]):
                aux=lista[j]
                lista[j]=lista[j-1]
                lista[j-1]=aux
                mostrar(lista)
                print("----------------\n")
                
def metodoQuickSort(lista,izq,der):
    i=izq
    j=der
    x=lista[(izq + der)//2]
 
    while( i <= j ):
        while lista[i]<x and j<=der:
            i=i+1
        while x<lista[j] and j>izq:
            j=j-1
        if i<=j:
            aux = lista[i]; lista[i] = lista[j]; lista[j] = aux;
            i=i+1;  j=j-1;
 
        if izq < j:
            metodoQuickSort(lista, izq, j)
    if i < der:
        metodoQuickSort(lista, i, der )
        mostrar(lista)
        print("----------------\n")
        
def menu():
    l=[]
    print("Seleccione una opcion:")
    print("1. Ordenar el arrelo por el método de burbuja")
    print("2. Ordenar el arrelo por el método de seleccion")
    print("3. Ordenar el arrelo por el método de insercion")
    print("4. Ordenar el arrelo por el método de quick sort")
    print("5. Salir")
    n=int(input("Ingrese un numero: "))
    if n==1:
        num=int(input("Ingresa cuantos numeros quiere que tenga el arreglo\n"))
        l=arreglo(num)
        print("El arreglo creado es: ")
        mostrar(l)
        print("El arreglo ordenado es:")
        metodoBurbuja(l)
        menu()
    elif n==2:
        num=int(input("Ingresa cuantos numeros quiere que tenga el arreglo\n"))
        l=arreglo(num)
        print("El arreglo creado es: ")
        mostrar(l)
        print("El arreglo ordenado es:")
        metodoSeleccion(l)
        menu()
    elif n==3:
        num=int(input("Ingresa cuantos numeros quiere que tenga el arreglo\n"))
        l=arreglo(num)
        print("El arreglo creado es: ")
        mostrar(l)
        print("El arreglo ordenado es:")
        metodoInsercion(l)
        menu()
    elif n==4:
        num=int(input("Ingresa cuantos numeros quiere que tenga el arreglo\n"))
        l=arreglo(num)
        print("El arreglo creado es: ")
        mostrar(l)
        print("El arreglo ordenado es:")
        metodoQuickSort(l)
        menu()
    else:
        print("Bye")
        
menu()

"""
l=arreglo(5)
print(l)
print(copiar(l))
mostrar(l)
metodoQuickSort(l,0,len(l)-1)
"""