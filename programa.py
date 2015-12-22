import funcoes
import random

def centroide(lista):
    Attrb, labels = funcoes.separadados(lista)


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

    print(len(Cent1), len(Cent2), len(Cent3))

    for i,iname in zip([Cent1, Cent2, Cent3],[1,2,3]):
        for j in i:
            for k in j:
                print(str(k)+",")
            print(str(iname)+"\n")
    return Centroide1, Centroide2, Centroide3, Cent1, Cent2, Cent3
