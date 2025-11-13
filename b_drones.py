while (True):
    drones = int(input())
    if(drones == 0): break

    hash = {}

    for i in range(1, drones + 1):
        distancias = list(map(int, input().split(" ")))
        hash[i] = sum(distancias)
    
    vencedor = max(hash.items(), key=lambda item: (item[1], -item[0]))[0]
    print(f"Drone {vencedor}")
    