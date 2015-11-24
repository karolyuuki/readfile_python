import cmath


def dis_euclid(i,j):
    n = len(i)
    soma = 0
    for a in range(len(i)):
        soma = soma + ((j[a] - i[a])^2)
    distancia = cmath.sqrt(soma)
    return distancia

lista1 = [1,3,4,6,23,6,964,30]
lista2 = [4,24,75,6,87,345,94,3]

a = dis_euclid(lista1,lista2)
