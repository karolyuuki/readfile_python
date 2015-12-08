import math


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
    print (size)
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
