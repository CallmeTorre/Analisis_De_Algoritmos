#!/usr/bin/python

def euclides(m,n):
    """Funcion que recibe dos numeros enteros positivos m y n y retorna su MCD (Maximo Comun Multiplo)"""
    cont = 0
    r = 0
    cont +=1
    cont +=1
    while n != 0:
        r = m%n
        cont +=1
        m = n
        cont +=1
        n = r
        cont +=1
    return cont#, m

def fibonacci(n):
    """Funcion que genera la secuencia de Fibonacci para un numero n."""
    if n<0:
        return None
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def main():
    array = []
    for i in range(1,25):
        array.append(fibonacci(i))
    for i in range(23,0,-1):
        if(i>1):
            print(euclides(array[i], array[i-1]),array[i],array[i-1])

if __name__ == '__main__':
    main()
