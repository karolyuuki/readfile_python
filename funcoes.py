import math
import random

def distanciaeuclidiana(i,j):
    n = len(i)
    soma = 0
    for a in range(len(i)):
        soma = soma + ((j[a] - i[a])**2)
    distancia = math.sqrt(soma)
    return distancia
    

def separadados(filename):
    filex = open (filename, 'r')
    list_items = filex.readlines()
    size =(len(list_items))
    Llabel = list()
    attr = list()
    for item in list_items:
        value = item.split(",")
        attr.append(item[:-3])
        label= value.pop()
        Llabel.append(label)

    newarchiveW = open('list_atributes2.txt', 'w')
    for i in attr: 	
        for j in i:
                newarchiveW.write(str(j))
        newarchiveW.write("\n")
    newarchiveW.close()

    newarchiveL = open('list_labels2.txt', 'w')
    for i in Llabel: 	
            for j in i:
                newarchiveL.write(str(j))
            newarchiveL.write("\n")
    newarchiveL.close()

    return attr, Llabel

def converteitens(lista):
    nitem= list()
    for item in lista.split(","):
        nitem.append(float(item))
    return nitem

import funcoes
import random

def centroide(lista):
    Attrb, labels = funcoes.separadados(lista)


    c = len(Attrb)
    Centroide1 = converteitens(Attrb[random.randint(0,c)])
    Centroide2 = converteitens(Attrb[random.randint(0,c)])
    Centroide3 = converteitens(Attrb[random.randint(0,c)])


    Cent1 = list()
    Cent2 = list()
    Cent3 = list()

    for item in Attrb:
        nitem = funcoes.converteitens(item)
        a = distanciaeuclidiana(nitem,Centroide1)
        b = distanciaeuclidiana(nitem,Centroide2)
        c = distanciaeuclidiana(nitem,Centroide3)
        if a<b and a<c:
            Cent1.append(nitem)
        elif b<a and b<c:
            Cent2.append(nitem)
        else:
            Cent3.append(nitem)

    #print(len(Cent1), len(Cent2), len(Cent3))

    #for i,iname in zip([Cent1, Cent2, Cent3],[1,2,3]):
        #for j in i:
            #for k in j:
                #print (str(k)+",")
            #print(str(iname)+"\n")
    return Centroide1, Centroide2, Centroide3, Cent1, Cent2, Cent3

def cluster(lista,centroides):
    Attrb, labels = funcoes.separadados(lista)


    c = len(Attrb)
    Centro = centroides[1]
    Centroide1 = Centro[0]
    Centroide2 = Centro[1]
    Centroide3 = Centro[2]


    Cent1 = list()
    Cent2 = list()
    Cent3 = list()

    for item in Attrb:
        nitem = funcoes.converteitens(item)
        a = distanciaeuclidiana(nitem,Centroide1)
        b = distanciaeuclidiana(nitem,Centroide2)
        c = distanciaeuclidiana(nitem,Centroide3)
        if a<b and a<c:
            Cent1.append(nitem)
        elif b<a and b<c:
            Cent2.append(nitem)
        else:
            Cent3.append(nitem)

    #print(len(Cent1), len(Cent2), len(Cent3))
    newarchive= open ('lists_cluster.txt','w')
    for i,iname in zip([Cent1, Cent2, Cent3],[1,2,3]):
        for j in i:
            for k in j:
                newarchive.write(str(k)+",")
            newarchive.write(str(iname)+"\n")
    return Cent1, Cent2, Cent3
