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

FECHA: 6/Septiembre/2017
"""
import random

def merge(array, p, q, r):
    cont = 0
    n1 = q - p + 1
    n2 = r - q

    L = [array[p+i] for i in range(0,n1)]
    R = [array[q+1+j] for j in range(0,n2)]

    i = 0
    j = 0
    k = p

    cont +=1
    while i < n1 and j < n2:
        cont += 1
        if(L[i] <= R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    cont +=1
    while i < n1:
        cont += 1
        array[k] = L[i]
        i += 1
        k += 1

    cont +=1
    while j < n2:
        cont += 1
        array[k] = R[j]
        j += 1
        k += 1
    return(cont)

def mergeSort(array, p, r, cont):
    cont +=1
    if p < r:
        q = (p+r)/2
        mergeSort(array, p, q,cont+1)
        mergeSort(array, q+1, r,cont +1)
        merge(array, p, q, r)
    print(cont)

def main():
    for x in range(1,4):
        algo = random.sample(range(1,5), x)
        print(algo)
        #merge(algo,0,len(algo)/2,len(algo)-1)
        mergeSort(algo,0,len(algo)-1,0)
        print("////////////")
    #print algo

if __name__ == '__main__':
    main()
