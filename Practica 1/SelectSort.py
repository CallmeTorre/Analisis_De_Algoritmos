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

def selectSort(array):
    """Algoritmo de ordenamiento Selection Sort."""
    min_index = 0
    for j in range(0,len(array)-2):
        min_index = j
        for i in range(j+1,len(array)):
            if(array[i] < array[j]):
                min_index = i
        array[j], array[min_index] = array[min_index], array[j]
    return array

def main():
    print(selectSort([9,8,7,6,5,4,3,2,1]))

if __name__ == '__main__':
    main()
