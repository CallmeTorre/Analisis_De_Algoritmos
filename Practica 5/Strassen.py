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

FECHA: 15/Octubre/2017
"""
import operator

def ikj_matrix_product(A, B):
    """Función que multiplica matrices usando el algoritmo ikj."""
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def operation(A, B, op):
    """Función que recibe dos matrices y les aplica el operador que también recibe."""
    ops = {'+': operator.add,
           '-': operator.sub}
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = ops[op](A[i][j], B[i][j])
    return C

def Strassen(A,B):
    """Función que multiplica una matriz usando el algoritmo de Strassen"""
    n = len(A)
    if n==2:
        return ikj_matrix_product(A, B)
    else:
        new_size = n/2
        a11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        b11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                a11[i][j] = A[i][j]            # top left
                a12[i][j] = A[i][j + new_size]    # top right
                a21[i][j] = A[i + new_size][j]    # bottom left
                a22[i][j] = A[i + new_size][j + new_size] # bottom right

                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + new_size]    # top right
                b21[i][j] = B[i + new_size][j]    # bottom left
                b22[i][j] = B[i + new_size][j + new_size] # bottom right

        s1 = operation(b12, b22, "-") # b12 - b22
        s2 = operation(a11, a12, "+") # a11 + a12
        s3 = operation(a21, a22, "+") # a21 + a22
        s4 = operation(b21, b11, "-") # b21 - b11
        s5 = operation(a11, a22, "+") # a11 + a22
        s6 = operation(b11, b22, "+") # b11 + b22
        s7 = operation(a12, a22, "-") # a12 - a22
        s8 = operation(b21, b22, "+") # b21 + b22
        s9 = operation(a11, a21, "-") # a11 - a21
        s10 = operation(b11, b12, "+") # b11 + b12

        p1 = Strassen(a11, s1) # a11 * s1
        p2 = Strassen(s2, b22) # s2 * b22
        p3 = Strassen(s3, b11) # s3 * b11
        p4 = Strassen(a22, s4) # a22 * s4
        p5 = Strassen(s5, s6) # s5 * s6
        p6 = Strassen(s7, s8) # s7 * s8
        p7 = Strassen(s9, s10) # s9 * s10

        aux = operation(p5, p4, "+") # p5 + p4
        aux2 = operation(aux, p2, "-") # p5 + p4 - p2
        c11 = operation(aux2, p6, "+") # p5 + p4 - p2 + p6
        c12 = operation(p1,p2, "+") # p1 + p2
        c21 = operation(p3, p4, "+") # p3 + p4
        aux = operation(p5, p1, "+") # p5 + p1
        aux2 = operation(aux, p3, "-") # p5 + p1 - p3
        c22 = operation(aux2, p7, "-") # p5 + p1 - p3 - p7

        C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                C[i][j] = c11[i][j]
                C[i][j + new_size] = c12[i][j]
                C[i + new_size][j] = c21[i][j]
                C[i + new_size][j + new_size] = c22[i][j]
        return C

def main():
    x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    y=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(Strassen(x,y))

if __name__ == '__main__':
    main()
