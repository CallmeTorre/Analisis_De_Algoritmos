#!/usr/bin/python

def euclides(m,n):
    """Algoritmo de Euclides para encontrar el mcd de dos numeros enteros positivos m y n"""
    r = 0
    while n!= 0:
        r = m%n
        m = n
        n = r
    return m

def main():
    print(euclides(1000,120))

if __name__ == '__main__':
    main()
