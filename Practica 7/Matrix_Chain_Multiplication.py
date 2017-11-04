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

FECHA: 7/Noviembre/2017
"""
import sys

def printParenthesis(i,j,n,bracket):
    """Función que imprime el orden correcto de parentesis en la multiplicacion."""
    if i == j:
        print("A"),
        return
    print("("),
    printParenthesis(i,bracket[i][j],n,bracket)
    printParenthesis(bracket[i][j]+1,j,n,bracket)
    print(")"),

def matrixChainOrder(p,n):
    """Funcion que obtiene el costo optimo para la multiplicacion de matrices."""
    #Por simplicidad se agrega una columna y una fila en m[][].
    #La columna y la fila 0 en m[] no se utilizan.
    m = [[0 for x in range(n)] for x in range(n)]

    #Bracket almacena el break point optimo en la subexpresion de i hasta j.
    bracket = [[0 for x in range(n)] for x in range(n)]

    #m[i][j] = Numero minimo de multiplicaciones escalares necesitadas para computar A[i]A[i+1]...A[j] = A[i...j]
    #Donde las dimensiones de A[i] es p[i-1] * p[i]
    #El costo es 0 cuando se multiplica una matriz.
    for i in range(1,n):
        m[i][i] = 0
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in range(i,j):
                #q es el costo de las multiplicaciones.
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if(q < m[i][j]):
                    m[i][j] = q
                    #Cada entrada en bracket[i][j] = k muestra donde
                    #se va a dividr el producto de arr i,i+1,...j para el costo minimo.
                    bracket[i][j] = k
    print("Forma correcta de Parentesis: ")
    printParenthesis(1,n-1,n,bracket)
    print("")
    print("Minimo numero de multiplicaciones: %d" % m[1][n-1])

def main():
    arr = [10,20,30,40,30]
    size = len(arr)
    arr2 = [10,20,50,10]
    size2 = len(arr2)
    arr3 = [30,10]
    size3 = len(arr3)
    print("Arreglo: "),
    print(arr)
    matrixChainOrder(arr,size)
    print("---------------------------")
    print("Arreglo: "),
    print(arr2)
    matrixChainOrder(arr2,size2)
    print("---------------------------")
    print("Arreglo: "),
    print(arr3)
    matrixChainOrder(arr3,size3)
    print("---------------------------")

if __name__ == '__main__':
    main()
