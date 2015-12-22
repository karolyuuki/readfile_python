import funcoes

centroids = list()
medias = list()
for it in range(0,50):

    c1, c2, c3, cent1, cent2, cent3 = funcoes.centroide('normals.txt')

    centroids.append([c1,c2,c3])
    a = 0
    b = 0
    c = 0

    for i in cent1:
        a= a + funcoes.distanciaeuclidiana(c1,i)
    med1= a/len(cent1)

    for i in cent2:
        b= b + funcoes.distanciaeuclidiana(c2,i)
    med2= b/len(cent2)

    for i in cent3:
        c= c + funcoes.distanciaeuclidiana(c3,i)
    med3= c/len(cent3)

    media = (med1+med2+med3)/3
    medias.append(media)
    
#percorrer medias pra achar o menor valor
#Se fizer isso com algum tipo de sort n'ao vai dar muito certo, pq vai desordenar
#e n'ao vai dar mais pra saber qual media eh de qual centroide
#se der um zip neles dois com as medias primeiro e usar s[o as medias
#como parametro pode dar certo


