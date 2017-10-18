def msc(array,bajo,medio,alto):
    suma_izq = 0
    max_izq = 0
    suma = 0
    for x in range(medio,bajo-1,-1):
        suma = suma + array[x]
        if(suma > suma_izq):
            suma_izq = suma
            max_izq = x
    suma_der = 0
    max_der = 0
    suma = 0
    for y in range(medio+1,alto+1):
        suma = suma + array[y]
        if(suma > suma_der):
            suma_der = suma
            max_der = y
    return suma_der+suma_izq

def ms(array,bajo,alto):
    if(bajo == alto):
        return array[bajo]
    else:
        medio = (bajo + alto)/2
        return max(ms(array,bajo,medio),
                   ms(array,medio+1,alto),
                   msc(array,bajo,medio,alto))

def main():
    array = [2, 3, 4, 5, 7]
    #sum_c = msc(array,0,len(array)/2,len(array)-1)
    #print(sum_c)
    sum_f =ms(array,0,len(array)-1)
    print(sum_f)

if __name__ == '__main__':
    main()
