# Crear un módulo de funciones aritmeticas que realicen las operaciones suma, multiplicacion, division y potencia
def suma(n1,n2):
    calculo_suma=n1+n2
    return calculo_suma

def resta(n1,n2):
    calculo_resta=n1-n2
    return calculo_resta

def multi(n1,n2):
    calculo_multi=n1*n2
    return calculo_multi

def divi(n1,n2):
    if(n2==0):
        print("La operación no se puede efectuar")
    else:
        calculo_divi=n1/n2
        return calculo_divi

def potencia(n1,n2):
    if(n2==0):
        print(1)
    else:
        calculo_pot=pow(n1,n2)
        return calculo_pot