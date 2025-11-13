while (True):
    produtos = int(input())
    if(produtos == 0): break

    estoque = list(map(int, input().split(" ")))

    qntPedidos = int(input())
    pedidos = list(map(int, input().split(" ")))

    for item in pedidos:
        item_idx = item - 1

        if 0 <= item_idx < len(estoque):
            if (estoque[item_idx] > 0):
                estoque[item_idx] = estoque[item_idx] - 1
    
    disponivel = 0
    fora = 0
    for item_estq in estoque:
        if(item_estq > 0):
            disponivel += 1
        else:
            fora += 1
        
    print(disponivel)
    print(fora)