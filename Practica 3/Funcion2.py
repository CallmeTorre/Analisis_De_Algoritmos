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

def Funcion(array, x):
    for i in range(0,len(array)):
        if(array[i] < x):
            array[i] = min(array)
        elif(array[i] > x):
            array[i] = max(array)
        else:
            break

def main():
    algo = [6,7,8,9]
    x = 0
    Funcion(algo,x)
    print algo

if __name__ == '__main__':
    main()
