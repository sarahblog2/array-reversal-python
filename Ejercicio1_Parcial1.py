
arreglo = [1, 2, 3, 4, 5]

print(f"El arreglo original es: {arreglo}")

def InvertirArreglo(arreglo):
    n = len(arreglo)  
    arreglo_inv = [] 

    for i in range(n):  
        arreglo_inv.append(arreglo[n - 1 - i])

    print(f"El arreglo invertido es : {arreglo_inv}")  
    return arreglo_inv  


def MostrarArreglo(arreglo):
    
    for a in arreglo:  
        print(a, end=" ") 
    print()


MostrarArreglo(arreglo)


arregloInvertido = InvertirArreglo(arreglo)  
MostrarArreglo(arregloInvertido)  

