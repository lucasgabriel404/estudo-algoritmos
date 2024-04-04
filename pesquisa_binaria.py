minha_lista = []

for novo_item in range(25000):
    minha_lista.append(novo_item)


def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista)-1

    while baixo <= alto:
        meio = int((baixo+ alto)/2)
        chute = meio
        print(f'*******************************\nLimite superior: {alto}\n  Meio: {meio} \nLimite inferior:{baixo}\n*******************************')

        if chute == item:
            print('numero encontrado')
            return meio
        if chute > item:
            print('valor muito alto:', meio, '-1 no limite superior')
            alto = meio -1
        else:
            print('valor muito baixo:', meio, '+1 no limite inferior')
            baixo = meio +1
    return None
print(pesquisa_binaria(minha_lista,3875))