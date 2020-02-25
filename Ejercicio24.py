# Escribir un programa que lea desde el teclado el importe bruto de un factura y determine el importe neto según los siguientes criterios
# Importe bruto menor de 20.000 - sin descuento
# Importe bruto mayor de 20.000 - 15% de descuento
print("Ingrese el importe bruto de la factura")
importBruto= int(input())
if importBruto > 20000:
    descuento=importBruto*0.85
    print("El importe neto es:")
    print(descuento)
else:
    print("El importe neto es:")
    print(importBruto)
