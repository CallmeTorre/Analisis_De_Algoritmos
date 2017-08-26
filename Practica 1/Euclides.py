#!/usr/bin/python

#Variable global que nos sirve para almacenar los Fibonacci ya calculados
aux = [0]*100
aux[1] = 1

def euclides(m,n):
    """Funcion que recibe dos numeros enteros positivos m y n y retorna su MCD (Maximo Comun Multiplo)"""
    cont = 0
    r = 0
    while n != 0:
        r = m%n
        m = n
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
    elif aux[n] != 0: #Verifica si ya se calculo anteriormente y agiliza el proceso
        return aux[n]
    else:
        aux[n] = fibonacci(n-1)+fibonacci(n-2)
        return aux[n]

def main():
    for i in range(1,80):
        a = fibonacci(i)
        b = fibonacci(i+1)
        print("Entra: %d para %d y %d" % (euclides(a,b),a,b))
        
if __name__ == '__main__':
    main()
