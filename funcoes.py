import math
import random

def distanciaeuclidiana(i,j):
    #Calculates the distance betweent two points
    n = len(i)
    soma = 0
    for a in range(len(i)):
        soma = soma + ((j[a] - i[a])**2)
    distancia = math.sqrt(soma)
    return distancia
    

def separadados(filename):
    #recieves a file and returns one lists with the attributes
    #and other one with the labels. Also save them in txt files
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

def centroide(lista):
    Attrb, labels = separadados(lista)


    c = (len(Attrb))-1
    Centroide1 = converteitens(Attrb[random.randint(0,c)])
    Centroide2 = converteitens(Attrb[random.randint(0,c)])
    Centroide3 = converteitens(Attrb[random.randint(0,c)])


    Cent1 = list()
    Cent2 = list()
    Cent3 = list()

    for item in Attrb:
        nitem = converteitens(item)
        a = distanciaeuclidiana(nitem,Centroide1)
        b = distanciaeuclidiana(nitem,Centroide2)
        c = distanciaeuclidiana(nitem,Centroide3)
        if a<b and a<c:
            Cent1.append(nitem)
        elif b<a and b<c:
            Cent2.append(nitem)
        else:
            Cent3.append(nitem)


    return Centroide1, Centroide2, Centroide3, Cent1, Cent2, Cent3

def cluster(lista,centroides):
    Attrb, labels = separadados(lista)


    c = len(Attrb)
    Centro = centroides[1]
    Centroide1 = Centro[0]
    Centroide2 = Centro[1]
    Centroide3 = Centro[2]


    Cent1 = list()
    Cent2 = list()
    Cent3 = list()

    for item in Attrb:
        nitem = converteitens(item)
        a = distanciaeuclidiana(nitem,Centroide1)
        b = distanciaeuclidiana(nitem,Centroide2)
        c = distanciaeuclidiana(nitem,Centroide3)
        if a<b and a<c:
            Cent1.append(nitem)
        elif b<a and b<c:
            Cent2.append(nitem)
        else:
            Cent3.append(nitem)

    newarchive= open ('lists_cluster.txt','w')
    for i,iname in zip([Cent1, Cent2, Cent3],[1,2,3]):
        for j in i:
            for k in j:
                newarchive.write(str(k)+",")
            newarchive.write(str(iname)+"\n")
    return Cent1, Cent2, Cent3

def cluster2(lista,centroides):
    Attrb, labels = separadados(lista)


    c = len(Attrb)
    Centroide1 = centroides[0]
    Centroide2 = centroides[1]
    Centroide3 = centroides[2]


    Cent1 = list()
    Cent2 = list()
    Cent3 = list()

    for item in Attrb:
        nitem = converteitens(item)
        a = distanciaeuclidiana(nitem,Centroide1)
        b = distanciaeuclidiana(nitem,Centroide2)
        c = distanciaeuclidiana(nitem,Centroide3)
        if a<b and a<c:
            Cent1.append([a,nitem])
        elif b<a and b<c:
            Cent2.append([b,nitem])
        else:
            Cent3.append([c,nitem])
    Cent1.sort(key=lambda tup: tup[0])
    Cent2.sort(key=lambda tup: tup[0])
    Cent3.sort(key=lambda tup: tup[0])
    print('/n')

    newarchive= open ('lists_cluster2.txt','w')
    for i,iname in zip([Cent1, Cent2, Cent3],[1,2,3]):
        for j in i:
            for k in j:
                newarchive.write(str(k)+",")
            newarchive.write(str(iname)+"\n")
    return Cent1, Cent2, Cent3

def centroide2(lista,centroides):
    Attrb, labels = separadados(lista)


    Centroide1 = centroides[0]
    Centroide2 = centroides[1]
    Centroide3 = centroides[2]


    cent1 = list()
    cent2 = list()
    cent3 = list()
    med = list()

    for item in Attrb:
        nitem = converteitens(item)
        a = distanciaeuclidiana(nitem,Centroide1)
        b = distanciaeuclidiana(nitem,Centroide2)
        c = distanciaeuclidiana(nitem,Centroide3)
        if a<b and a<c:
            cent1.append(nitem)
        elif b<a and b<c:
            cent2.append(nitem)
        else:
            cent3.append(nitem)

    x = 0
    y = 0
    z = 0

    try:
        for i in cent1:
            x= x + distanciaeuclidiana(Centroide1,i)
        med1= x/len(cent1)
    except(ZeroDivisionError):
        med1 = 6

    try:
        for i in cent2:
            y= y + distanciaeuclidiana(Centroide2,i)
        med2= y/len(cent2)
    except(ZeroDivisionError):
        med2 = 6

    try:
        for i in cent3:
            z= z + distanciaeuclidiana(Centroide3,i)
        med3= z/len(cent3)
    except(ZeroDivisionError):
        med3 = 6

    media = (med1+med2+med3)/3
    med.append(med1)
    med.append(med2)
    med.append(med3)

    return media, cent1, cent2,cent3, med
