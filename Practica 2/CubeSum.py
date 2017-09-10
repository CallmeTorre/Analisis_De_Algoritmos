# -*- coding: utf-8 -*-
"""
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO
Análisis de Algoritmos
GRUPO: 3CV1

ALUMNOS:
    Reyes Fragoso Roberto
    Torreblanca Faces Jesús Alexis

PROFESOR: Luna Benoso Benjamín

FECHA: 5/Septiembre/2017
"""

def recursiveS(n):
    """Funcion que regresa la suna de los primeros n cubos de manera recursiva"""
    if n == 1:
        return 1
    else:
        return recursiveS(n-1) + n*n*n

def iterativeS(n):
    """Funcion que regresa la suna de los primeros n cubos de manera iterativa"""
    sum = 0
    for x in range(n,1,-1):
        sum = sum + x*x*x
    return sum + 1

def main():
    #Recursivo
    print("Recursivo")
    for x in range(1,80):
        print("Para %d el resultado es: %d" %(x,recursiveS(x)))

    #Iterativo
    print("Iterativo")
    for x in range(1,80):
        print("Para %d el resultado es: %d" %(x,iterativeS(x)))

if __name__ == '__main__':
    main()
