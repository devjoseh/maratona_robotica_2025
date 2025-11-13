while (True):
    participantes, rodadas = map(int, input().split(" "))
    if(participantes == 0 and rodadas == 0): break

    hash = {}
    maioresRodadas = {}

    for i in range(1, rodadas + 1):
        pontuacoes = list(map(int, input().split(" ")))
        timeAtual = 1

        for pontuacao in pontuacoes:
            pontuacaoAtual = hash.get(timeAtual, 0)
            hash[timeAtual] = pontuacaoAtual + pontuacao

            maiorPontuacao = maioresRodadas.get(timeAtual, 0)
            if(pontuacao > maiorPontuacao):
                maioresRodadas[timeAtual] = pontuacao

            timeAtual += 1

    vencedor = 1
    for timeAtual in range(2, participantes + 1):
        if hash[timeAtual] > hash[vencedor]:
            vencedor = timeAtual
        
        elif hash[timeAtual] == hash[vencedor]:
            if maioresRodadas[timeAtual] > maioresRodadas[vencedor]:
                vencedor = timeAtual
            elif maioresRodadas[timeAtual] == maioresRodadas[vencedor]:
                pass

    print(f"Time {vencedor}")

