while (True):
    medicoes = int(input())
    if(medicoes == 0): break

    potencias = list(map(int, input().split(" ")))
    potenciaFinal = 0

    for item in potencias:
        potenciaFinal += int(item * 9 / 10)

    print(int(potenciaFinal))