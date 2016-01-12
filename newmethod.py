import funcoes

def bestCentroid(onelist):
    centroids = list()
    medias = list()
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
        print(cont, media)
        if (media<= 3.5):
            a = 0
            centroids.append(c1)
            centroids.append(c2)
            centroids.append(c3)
            medias.append(media)
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

Cents = list()
Cents =funcoes.cluster2(lista,centroides)

#for i,j in zip(medias,centroides):
    #if (i > 3.1 and i <=3.5):
    

# If the average distance is between 3.1 and 3.8, we will choose
# in the list of this centroid what item is closer to them and turn it the
# new centroid. If the average distance is between 3.8 and 5, we will choose
# someone in the middle of the list.
