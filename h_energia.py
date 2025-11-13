while (True):
    medicoes = int(input())
    if(medicoes == 0): break

    departamentos = {}
    ordem_insercao = {}
    contador = 0

    for _ in range(medicoes):
        codigo, tipo, consumo = map(str, input().split(" "))
        consumo = float(consumo)

        if codigo not in departamentos:
            departamentos[codigo] = {
                "tipo": tipo,
                "consumo": 0.0
            }
            ordem_insercao[codigo] = contador
            contador += 1
        
        departamentos[codigo]["consumo"] += consumo

    tiposConsumo = {}
    for codigo, dados in departamentos.items():
        tipo = dados["tipo"]
        consumo = dados["consumo"]

        if tipo not in tiposConsumo:
            tiposConsumo[tipo] = []
        tiposConsumo[tipo].append(consumo)
    
    maiorTipo = None
    maiorMedia = 0

    for tipo, consumos in tiposConsumo.items():
        media = sum(consumos) / len(consumos)
        if media > maiorMedia:
            maiorMedia = media
            maiorTipo = tipo
    
    print(f"{maiorTipo} {maiorMedia:.2f}")

    consumoTotalGeral = sum(dados["consumo"] for dados in departamentos.values())
    mediaGeral = consumoTotalGeral / len(departamentos)

    acimaMedia = []
    for codigo, dados in departamentos.items():
        if dados["consumo"] > mediaGeral:
            acimaMedia.append((codigo, dados["tipo"], dados["consumo"], ordem_insercao[codigo]))
    
    acimaMedia.sort(key=lambda x: (-x[2], x[0]))

    for codigo, tipo, consumo, _ in acimaMedia:
        print(f"{codigo} {tipo} {consumo:.2f}")