# Escribir un programa que divida todos los elementos de una matriz M (3,4) por el elemento situado en la posicion (2,2)
import numpy as np
matriz=[[2,4,6,8],
     [10,12,14,16],
     [20,18,2,22]]
m=np.array(matriz)
print(m)
print(m[2,2])
division=(1/(m[2,2]))*m
print(division)