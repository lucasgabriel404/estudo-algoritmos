votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print('Mande embora!')
    else:
        votaram[nome] = True
        print('Deixe votar!')
    
    verifica_eleitor(input('Nome pessoa que veio votar:\n'))

verifica_eleitor(input('Nome pessoa que veio votar:\n'))