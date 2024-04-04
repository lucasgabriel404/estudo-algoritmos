def contagem_itens(lista):
    if not lista:
        return 0
    else:
        lista.pop()
        return 1 + contagem_itens(lista)
    
print(contagem_itens([1,5,5,4,7,8,5,3,4,5,8,8,6,4,7,65,9,5,84,9,2,84,59,5,48,15,98,4,4]))
