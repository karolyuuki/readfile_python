import funcoes
import random

Attrb, labels = funcoes.separadados('normals.txt')


c = len(Attrb)
Centroide1 = funcoes.converteitens(Attrb[random.randint(0,c)])
Centroide2 = funcoes.converteitens(Attrb[random.randint(0,c)])
Centroide3 = funcoes.converteitens(Attrb[random.randint(0,c)])


Cent1 = list()
Cent2 = list()
Cent3 = list()

for item in Attrb:
    nitem = funcoes.converteitens(item)
    a = funcoes.distanciaeuclidiana(nitem,Centroide1)
    b = funcoes.distanciaeuclidiana(nitem,Centroide2)
    c = funcoes.distanciaeuclidiana(nitem,Centroide3)
    if a<b and a<c:
        Cent1.append(nitem)
    elif b<a and b<c:
        Cent2.append(nitem)
    else:
        Cent3.append(nitem)

return Cent1, Cent2, Cent3
