def recursiveS(n,contador):
    """Funcion que regresa la suna de los primeros n cubos de manera recursiva"""
    if n == 1:
        print(contador)
        return 1
    else:
        return recursiveS(n-1,contador+1) + n*n*n

def iterativeS(n):
    """Funcion que regresa la suna de los primeros n cubos de manera iterativa"""
    cont = 0
    sum = 0
    for x in range(n,1,-1):
        sum = sum + x*x*x
        cont += 1
    return cont#,sum + 1

def main():
    #Recursivo
    for x in range(1,80):
        print("Para %d tardo: " %x)
        recursiveS(x,0)

    #Iterativo
    for x in range(1,80):
        print("Para %d tardo: " %x)
        recursiveS(x,0)

if __name__ == '__main__':
    main()
