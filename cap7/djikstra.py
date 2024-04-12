#GRAFOS
grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2
grafo['a'] = {}
grafo['a']['fim'] = 1
grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5
grafo['fim'] = {}

#CUSTO
infinito = float('inf')
custos = {}
custos['a'] = 6 #atualiza para 5 pois caminho por b é menor
custos['b'] = 2
custos['fim'] = infinito # inicio-b-fim =7 pai=b / (inicio-b)-a-fim=6 pai=a

#PAIS
pais = {}
pais['a'] = 'inicio' #atualiza para b pois caminho por b é menor
pais['b'] = 'inicio'
pais['fim'] = None # atualiza para b// atualiza para a

#PROCESSADOS
processados = []


def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:        
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo] # custo de b <- 2 //custo atualizado de a <- 5
    vizinhos = grafo[nodo] # vizinho mais proximo de b <- 3 //vizinho mais proximo de a(fim) <-1
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n] #custo de inicio-b + custo de b-a <- 5 // inicio-b-fim =7//(inicio-b)-a-fim <-6
        if custos[n] > novo_custo: #se o custo de inicio-a foi maior que inicio-b-a// se inicio-b-fim for maior que inicio-b-a-fim
            custos[n] = novo_custo #custo de a <-5 // custo de fim <- 6
            pais[n] = nodo #pai de a <-b // pai de fim <-a
    processados.append(nodo)  
    nodo = ache_no_custo_mais_baixo(custos)  

print("nodos processados:", processados)

def caminho(final):
    print(pais[final])    
    try:
        if pais[final]:
            caminho(pais[final])
        else:
            print("Caminho encontrado!")
    except:
        print('Caminho encontrado!')

caminho('fim')