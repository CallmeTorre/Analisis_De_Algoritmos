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

FECHA: 13/Septiembre/2017
"""
def partition(array, p, r):
    """Función que divide a un arreglo de tamaño n = p-r+1 en dos arreglos de tamaño q-p+1 y r-q"""
    x = array[r] #Tu pivote es el ultimo elemento del arreglo
    j = p - 1
    for i in range(p,r):
        if array[i] < x:
            j += 1
            array[j],array[i] = array[i],array[j]
    j += 1
    array[j],array[r] = array[r],array[j]
    return j

def quickSort(array, p, r):
    """Algoritmo de ordenamiento Quick Sort"""
    if p < r:
        q = partition(array, p, r)
        quickSort(array,p, q-1)
        quickSort(array,q+1,r)

def main():
    array = [10,9,8,7,6,5,4,3,2,1]
    quickSort(array,0,len(array)-1)
    print(array)

if __name__ == '__main__':
    main()
