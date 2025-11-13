import math

while True:
    quantidade = int(input())
    if quantidade == 0: 
        break

    total_KM = 0.0
    total_Litros = 0.0
    melhor_consumo = 0.0

    for i in range(quantidade):
        litros_abastecidos, quilometros_rodados = map(float, input().split())
        
        total_KM += quilometros_rodados
        total_Litros += litros_abastecidos

        if litros_abastecidos != 0:
            consumo_individual = quilometros_rodados / litros_abastecidos
            if consumo_individual > melhor_consumo:
                melhor_consumo = consumo_individual
                
    if total_Litros != 0:
        consumo_medio_geral = total_KM / total_Litros
    else:
        consumo_medio_geral = 0.0
    
    media_truncada = math.floor(consumo_medio_geral * 10) / 10
    melhor_truncado = math.floor(melhor_consumo * 10) / 10
    
    print(f"Media: {media_truncada:.1f}")
    print(f"Melhor: {melhor_truncado:.1f}")