import cmath
import random

def dis_euclid(i,j):
    n = len(i)
    soma = 0
    for a in range(len(i)):
        soma = soma + ((j[a] - i[a])**2)
    distancia = cmath.sqrt(soma)
    return distancia


filex = open ('list_atributes_general.txt', 'r')
list_items = filex.readlines()
randfactor = len(list_items)


ele1 = (list_items[random.randint(0,randfactor)])
Nele1 = list()
Final1 = list()
for c in ele1.split(","):
    Nele1.append(c)
a = (len(Nele1))- 1
for q in range(0,a):
    Final1.append(float(Nele1[q]))

ele2 =(list_items[random.randint(0,randfactor)])
Nele2 = list()
Final2 = list()
for c in ele2.split(","):
    Nele2.append(c)
a = (len(Nele2))- 1
for q in range(0,a):
    Final2.append(float(Nele2[q]))

euclidiana = dis_euclid(Final1,Final2)
print (euclidiana)
