lista_encomendas = []
while True:
    quantidade_encomendas, capacidade_peso = map(int, input().split())
    if quantidade_encomendas == 0:
        print()
        break
    lista_encomendas = []
    custo_total = 0
    for x in range(quantidade_encomendas):
        coordenada_x, coordenada_y, peso_encomenda = map(int, input().split())
        if coordenada_x < 0:
            coordenada_x = -coordenada_x
        if coordenada_y < 0:
            coordenada_y = -coordenada_y
        distancia_Manhattan = abs(coordenada_x) + abs(coordenada_y)
        encomendas = coordenada_x, coordenada_y, peso_encomenda, distancia_Manhattan
        lista_encomendas.append(encomendas)
    lista_encomendas.sort(key=lambda x: x[3], reverse=True)
    while lista_encomendas:
        peso_atual = 0
        distancia_viagem = 0
        entregas_feitas = []
        for encomenda in lista_encomendas:
            x, y, peso, distancia = encomenda
            if peso_atual + peso <= capacidade_peso:
                peso_atual += peso
                entregas_feitas.append(encomenda)
                distancia_viagem = max(distancia_viagem, distancia)
        custo_total += distancia_viagem * 2
        for entrega in entregas_feitas:
            lista_encomendas.remove(entrega)
    print(custo_total)