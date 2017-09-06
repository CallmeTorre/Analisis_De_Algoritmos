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
import random

def suma(a,b):
    """Funcion que recibe dos arreglos binarios A y B de longitud n y retorna la suma de ellos."""
    cont = 0
    maxlen = max(len(a), len(b))
    cont += 1
    result  = []
    cont += 1
    carry   = 0
    cont += 1
    i = maxlen - 1
    cont += 1

    cont += 1
    while(i >= 0):
        s = int(a[i]) + int(b[i])
        cont += 1
        cont += 1
        if s == 2: #1+1
            cont += 1
            if carry == 0:
                carry = 1
                cont += 1
                result.append(0)
                cont += 1
            else:
                cont += 1
                result.append(1)
                cont += 1
        elif s == 1: # 1+0
            cont += 1
            cont += 1
            if carry == 1:
                result.append(0)
                cont += 1
            else:
                cont += 1
                result.append(1)
                cont += 1
        else: # 0+0
            cont += 1
            if carry == 1:
                cont += 1
                result.append(1)
                cont += 1
                carry = 0
                cont += 1
            else:
                cont += 1
                result.append(0)
                cont += 1
        i = i - 1;
        cont += 1

    cont += 1
    if carry>0:
        result.append(1)
        cont += 1

    return cont #,result[::-1]

def rellena(n):
    """Funcion que genera dos numeros binarios aleatorios de longitud n y los almacena en dos arreglos"""
    a = []
    b = []
    for x in range(0,n):
        a.append(random.randint(0,1))
        b.append(random.randint(0,1))
    return a[::-1],b[::-1]

def main():
    for x in range(1,16):
        c = 0
        n = pow(2,x)
        a,b =  rellena(n)
        c = suma(a,b)
        print("Potencia: %d, Numero de operaciones:%d" %(n,c))

if __name__ == '__main__':
    main()
