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

#Variable global que nos sirve para almacenar los Fibonacci ya calculados
aux = [0]*100
aux[1] = 1

def euclides(m,n):
    """Funcion que recibe dos numeros enteros positivos m y n y retorna su MCD (Maximo Comun Multiplo)"""
    r = 0
    while n != 0:
        r = m%n
        m = n
        n = r
    return m

def fibonacci(n):
    """Funcion que genera la secuencia de Fibonacci para un numero n."""
    if n<0:
        return None
    elif n==1:
        return 0
    elif n==2:
        return 1
    elif aux[n] != 0: #Verifica si ya se calculo anteriormente y agiliza el proceso
        return aux[n]
    else:
        aux[n] = fibonacci(n-1)+fibonacci(n-2)
        return aux[n]

def main():
    for i in range(1,80):
        a = fibonacci(i)
        b = fibonacci(i+1)
        print("Para %d y %d el MCD es: %d" % (a,b,euclides(a,b)))

if __name__ == '__main__':
    main()
