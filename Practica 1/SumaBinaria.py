#!/usr/bin/python
import random

def suma(a,b):
    maxlen = max(len(a), len(b))
    result  = []
    carry   = 0
    i = maxlen - 1

    while(i >= 0):
        s = int(a[i]) + int(b[i])
        if s == 2: #1+1
            if carry == 0:
                carry = 1
                result.append(0)
            else:
                result.append(1)
        elif s == 1: # 1+0
            if carry == 1:
                result.append(0)
            else:
                result.append(1)
        else: # 0+0
            if carry == 1:
                result.append(1)
                carry = 0
            else:
                result.append(0)
        i = i - 1;

    if carry>0:
        result.append(1)

    return result[::-1]

def rellena(n):
    a = []
    b = []
    for x in range(0,n):
        a.append(random.randint(0,1))
        b.append(random.randint(0,1))
    return a[::-1],b[::-1]

def main():
    for x in range(1,4):
        n = pow(2,x)
        a,b =  rellena(n)
        print("Arreglo 1: ")
        print(a)
        print("\n")
        print("Arreglo 2: ")
        print(b)
        print("Suma: ")
        print(suma(a,b))

if __name__ == '__main__':
    main()
