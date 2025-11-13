while (True):
    quantidade = int(input())
    if(quantidade == 0): break

    requisicoes = list(map(int, input().split(" ")))
    minimo = min(requisicoes)
    maximo = max(requisicoes)
    media = sum(requisicoes) / len(requisicoes)

    print(f"{minimo} {maximo} {int(media)}")
