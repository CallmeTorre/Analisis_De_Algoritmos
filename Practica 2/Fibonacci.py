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

def recursive_fibonacci(n,contador):
    """Funcion que genera la secuencia de Fibonacci para un numero n de manera recursiva"""
    if n<0:
        return None
    elif n==1:
        print(contador)
        return 0
    elif n==2:
        print(contador)
        return 1
    else:
        return recursive_fibonacci(n-1,contador + 1)+recursive_fibonacci(n-2, contador + 1)

def iterative_fibonacci(n):
    """Funcion que genera la secuencia de Fibonacci para un numero n de manera iterativa"""
    cont = 0
    array = [0]*n
    array[0] = 0
    array[1] = 1
    for x in range(2,n):
        array[x] = array[x-2]+array[x-1]
        cont += 1
    return cont#,array

def main():
    #Recursivo
    for x in range(2,80):
        print(recursive_fibonacci(x,0))

    #Iterativo
    for x in range(2,80):
        print("Para %d tarda %d" %(x,iterative_fibonacci(x)))

if __name__ == '__main__':
    main()
