def soma(lista):    
    if not lista:
        return 0
    else:
        return lista.pop() + soma(lista)
    
print(soma([5,5,5,5,5,5,5,5,5,5,5,5,5]))