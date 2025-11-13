while (True):
    variacoes = int(input())
    if(variacoes == 0): break

    energia_final = 0
    menor_energia = 0
    energia_atual = 0

    variacoesEnergia = list(map(int, input().split(" ")))
    energia_final += sum(variacoesEnergia)

    for item in variacoesEnergia:
        energia_atual += item
        
        if(energia_atual < menor_energia):
            menor_energia = energia_atual
            
    print(energia_final)
    print(menor_energia)
    
    