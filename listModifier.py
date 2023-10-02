def listMenu():
    points = list()
    switch = int(input("Insira '1' para adicionar outro elemento à lista, '2' para remover um elemento da lista e '3' para finalizar \n"))
    while switch == 1 or switch == 2:
        if switch == 1: 
            print(points)
            points.append(float(input("Insira um número a ser adicionado à lista: ")))
            print(points)
            switch = int(input("Insira '1' para adicionar outro elemento à lista, '2' para remover um elemento da lista e '3' para finalizar"))
        if switch == 2:
            print(points)
            points.pop(points.index(float(input("Insira um númer a ser removida da lista"))))
            print(points)
            switch = int(input("Insira '1' para adicionar outro elemento à lista, '2' para remover um elemento da lista e '3' para finalizar"))
        if switch == 3:
            print("Encerrando e retornando a lista")
    print(points)
    return points
    exit()