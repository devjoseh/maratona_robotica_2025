while (True):
    paradas = int(input())
    if(paradas == 0): break

    atual = 0
    maximo = 0

    for i in range(1, paradas + 1):
        entrou, saiu = map(int, input().split(" "))

        atual += entrou
        atual -= saiu
        
        if atual > maximo:
            maximo = atual

    print(maximo)