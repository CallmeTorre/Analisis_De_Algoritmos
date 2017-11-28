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

FECHA: 29/Noviembre/2017
"""
from heapq import heappush, heappop, heapify
from collections import Counter
import sys

def readFile(path):
    """Funcion que lee un archivo, elimina los espacios y regresa el texto como cadena."""
    doc = open(path,"r").read()
    doc = doc.replace(" ", "")
    return doc[:len(doc)-1]

def writeFrequencies(array,count):
    """Funcion que crea un archivo y escribe el caracter y la frecuencia con la que aparece."""
    doc = open("Codificacion/Frecuencias.txt","w")
    doc.write("Simbolo | Frecuencia\n")
    for elem in array:
        element = elem[0]
        frecuency =  str(count[elem[0]])
        doc.write("%s | %s\n" %(element , frecuency))
    doc.close()

def writeCodification(array):
    """Funcion que crea un archivo y escribe el caracter y la codificacion que este tiene."""
    doc = open("Codificacion/Codificacion.txt","w")
    doc.write("Simbolo | Codigo\n")
    for elem in array:
        element = elem[0]
        code = elem[1]
        doc.write("%s | %s\n" %(element , code))
    doc.close()

def encodeFile(array,string):
    """Funcion que crea un archivo con el texto original codificado."""
    for elem in array:
        string = string.replace(elem[0],str(elem[1]))
    doc = open("Codificacion/Archivo_codificado.txt","w")
    doc.write(string)
    doc.close()

#def decodeFile(array):
#    encodedString = readFile("Codificacion/Archivo_codificado.txt")
#    for elem in array:
#        encodedString = encodedString.replace(str(elem[1]),elem[0])
#    doc = open("Decodificacion/Archivo_decodificado.txt","w")
#    doc.write(encodedString)
#    doc.close()

def huffman(dict_freq):
    """Funcion que genera los codigos de Huffman usando un heap."""
    heap = [[wt, [sym, ""]] for sym, wt in dict_freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def main():
    txt = readFile(sys.argv[1])
    dict_freq = Counter(txt)
    huff = huffman(dict_freq)
    writeFrequencies(huff,dict_freq)
    writeCodification(huff)
    encodeFile(huff,txt)
    decodeFile(huff)

if __name__ == '__main__':
    main()
