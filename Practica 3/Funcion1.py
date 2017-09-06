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

def Funcion(n):
    i = 0
    extra = 0
    while i < n:
        for j in range(1,11):
            extra = i #Acción(i), cualquier acción que sea O(1).
        i += 2

def main():
    Funcion(10)

if __name__ == '__main__':
    main()
