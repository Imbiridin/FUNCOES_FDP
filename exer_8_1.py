def meio_da_lista(numeros):

    lista = []
    minimo = min(numeros)
    maximo = max(numeros)
    
    for num in numeros:
        if num != minimo and num != maximo:
            lista.append(num)
    print(lista)

meio_da_lista([5,4,3,8,9])

    