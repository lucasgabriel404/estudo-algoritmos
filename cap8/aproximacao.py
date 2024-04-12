estados_abranger = set(['mt','wa','or','id','nv','ut','ca','az'])

#ESTAÇÕES
estacoes = {}
estacoes['kum'] = set(['id','nv','ut'])
estacoes['kdois']= set(['wa','id','mt'])
estacoes['ktres']= set(['or','nv','ca'])
estacoes['kquatro']= set(['nv','ut'])
estacoes['kcinco']= set(['ca','az'])
estacoes_final = set()


while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()

    for estacao, estados_por_estacao in estacoes.items():
        print('Estados restantes:', estados_abranger)
        cobertos = estados_abranger & estados_por_estacao #estados que a estação abrange que ainda n foram escolhidos
        if len(cobertos) > len(estados_cobertos): #se a quantidade de estados que a estacao abrange for maior que o ultimo escolhido
            melhor_estacao = estacao            
            estados_cobertos = cobertos
            print('Estação:', melhor_estacao, ', estados retirados:', estados_cobertos)

    estacoes_final.add(melhor_estacao)
    estados_abranger -= estados_cobertos

print(estacoes_final)