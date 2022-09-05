from secrets import randbelow


lista = [8, 5, 2, 4, 1, 6, 3, 7]

def separa(lista):
    if len(lista) <1:
        return[]

    izquierda = []
    derecha = []
    pivote = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] <pivote:
            izquierda.append(lista[i])
        else:
            derecha.append(lista[i])

    return izquierda, pivote, derecha

def quickSort(lista):
    if len(lista) <2:
        return lista

    izquierda, pivote, derecha = separa(lista) 

    return quickSort(izquierda) + [pivote] + quickSort (derecha)

print(quickSort(lista))      
