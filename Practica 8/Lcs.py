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

FECHA: 22/Noviembre/2017
"""
import sys

def readFile(path):
    """Funcion que lee un archivo, elimina los espacios y regresa el texto como cadena."""
    doc = open(path,"r").read()
    doc = doc.replace(" ", "")
    return doc[:len(doc)-1]

def lcs(X , Y):
    """Funcion que obtiene la subsecuencia común mas larga de dos cadenas."""
    m = len(X)
    n = len(Y)
    porcentaje = 0

    #Obtenemos que archivo es el mas grande y ese lo hacemos nuestro 100%
    mayor = max(m , n)

    #Generamos la matriz que almacenara los valores de la dp.
    L = [[None]*(n+1) for i in xrange(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    #L[m][n] contiene el largo de la LCS de X[0...n-1] & Y[0...m-1]
    porcentaje = (L[m][n]*100)/mayor
    return porcentaje

def main():
    doc1 = readFile(sys.argv[1])
    doc2 = readFile(sys.argv[2])
    print("Son iguales en un %d porciento." %(lcs(doc1 , doc2)))

if __name__ == '__main__':
    main()
