# Escribir un programa que calcule el IVA de un producto dado su valor de venta sin IVA
print("Digite el valor del producto sin IVA")
producto=int(input())
IVA=producto*0.16
productoIVA=producto+IVA
print("El valor del producto con IVA es: ")
print(productoIVA)