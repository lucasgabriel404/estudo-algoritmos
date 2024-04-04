def maior_valor(lista):
    if not lista:
        return 0
    try:
        if lista[0] < lista[1]:
            lista.pop(0)
            return maior_valor(lista)
        elif lista[1] < lista[0]:
            lista.pop(1)
            return maior_valor(lista)
    except:
        return lista[0]   
        

print(maior_valor([854,45,23,79,521,99999999,526,999,1548,26484,5984,45897,2187,5478888]))