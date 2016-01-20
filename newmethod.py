import funcoes

def bestCentroid(onelist):
    centroids = list()
    med = list()
    a=1
    cont=0
    while (a==1):

        c1, c2, c3, cent1, cent2, cent3 = funcoes.centroide(onelist)

        a = 0
        b = 0
        c = 0

        try:
            for i in cent1:
                a= a + funcoes.distanciaeuclidiana(c1,i)
            med1= a/len(cent1)
        except(ZeroDivisionError):
            med1 = 6

        try:
            for i in cent2:
                b= b + funcoes.distanciaeuclidiana(c2,i)
            med2= b/len(cent2)
        except(ZeroDivisionError):
            med2 = 6

        try:
            for i in cent3:
                c= c + funcoes.distanciaeuclidiana(c3,i)
            med3= c/len(cent3)
        except(ZeroDivisionError):
            med3 = 6

        media = (med1+med2+med3)/3
        cont = cont+1
        #print(cont, media)
        if (media<= 3.5):
            a = 0
            centroids.append(c1)
            centroids.append(c2)
            centroids.append(c3)
            medias = media
            med.append(med1)
            med.append(med2)
            med.append(med3)
        else:
            a=1

    return (medias,centroids,med)

lista = 'normals.txt'
Genmedia,centroides,medias = bestCentroid(lista)
print (centroides)
print (Genmedia, medias)


cents = list()
cents =funcoes.cluster2(lista,centroides)

def Srandom(medias, centroides, times, mediaoriginal):
    cont = 0
    ncentroides = centroides
    med,cent1,cent2,cent3,amedias = funcoes.centroide2(lista, centroides)
    for i in medias:
        if (i > 3.1 and i <=3.5):
            print(ncentroides[cont])
            aux = list()
            aux = cents[cont]
            if times == ((len(aux))-1):
                print(times)
                return (centroides, cent1, cent2, cent3, mediaoriginal)
            aux = aux[times]
            print(aux)
            ncentroides[cont] = aux[1]
            print(ncentroides[cont])
        if (i > 3.5):
            aux = list()
            aux = cents[cont]
            middle = round(len(aux)/2)
            if times == ((middle-2)):
                print(times)
                return (centroides, cent1, cent2, cent3, mediaoriginal)
            aux = aux[middle+times]
            ncentroides[cont] = aux[1]
        if (i<=3.1):
            ncentroides[cont]= ncentroides[cont]
        cont = cont+1
        
    print('ncentroides')
    print(ncentroides)
    nmed,ncent1,ncent2,ncent3,nmedias = funcoes.centroide2(lista, ncentroides)
    print(nmedias)
    if ((nmedias[0]<=3.1)and (nmedias[1]<=3.1)and(nmedias[2]<=3.1)):
        return (ncentroides, ncent1, ncent2, ncent3, nmed)
    print(nmed)
    if (mediaoriginal<=nmed):
        print('serviu de nada essa mudanca ai')
        times = times+1
        #print (times)
        Srandom(medias, centroides, times, mediaoriginal)
    else:
        print('melhorou!')
        novamedia=nmed
        Srandom(nmedias,ncentroides,1,novamedia)
    return(ncentroides, ncent1, ncent2, ncent3, nmed)

ncentroides, ncent1, cent2, cent3, nmed = Srandom(medias,centroides, 1, Genmedia)
print (nmed)
