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

def recursive_fibonacci(n):
    """Funcion que genera la secuencia de Fibonacci para un numero n de manera recursiva"""
    if n<0:
        return None
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

def iterative_fibonacci(n):
    """Funcion que genera la secuencia de Fibonacci para un numero n de manera iterativa"""
    array = [0]*n
    array[0] = 0
    array[1] = 1
    for x in range(2,n):
        array[x] = array[x-2]+array[x-1]
    return array[n-1]

def main():
    #Recursivo
    print("Recursivo")
    for x in range(2,80):
        print("Fibonacci de %d es: %d" %(x,recursive_fibonacci(x)))

    #Iterativo
    print("Iterativo")
    for x in range(2,80):
        print("Fibonacci de %d es: %d " %(x,iterative_fibonacci(x)))

if __name__ == '__main__':
    main()
