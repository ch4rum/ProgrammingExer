#!/bin/python3

# [..        [..                                           [.. [..
# [..        [..                        [..                [.. [..
# [..   [.   [..   [..    [. [... [.... [..        [..     [.. [..  ~ ch4rum
# [..  [..   [.. [..  [..  [..   [..    [. [.    [..  [..  [.. [..  ~ https://github.com/ch4rum/ProgrammingExer
# [.. [. [.. [..[..   [..  [..     [... [..  [..[..   [..  [.. [..  ~ Python3
# [. [.    [....[..   [..  [..       [..[.   [..[..   [..  [.. [..
# [..        [..  [.. [...[...   [.. [..[..  [..  [.. [...[...[...
                                                                                                                                                                                                                                                             
# Relacion dada
R = {(1,2), (1,3), (1,4), (2,3), (2,4), (3,2), (3,4), (5,1), (5,2), (5,3)}
def warshall (R):
    # Funcion que recibe una relacion, saca los nodos,imprime las matrices
    # solo retorna la matriz de cierre transitivo
    n = max(max(R)) # --> Solo para este problema
    w = [[0 for _ in range(n)] for _ in range(n)]

    for row,column in R:
        w[row-1][column-1] = 1

    for k in range(n):
        for row in range(n):
            for column in range(n):
                w[row][column] = w[row][column] or (w[row][k] and w[k][column])
        print (f"W[{k+1}] = {w}\n")
    return w

warshall(R)
