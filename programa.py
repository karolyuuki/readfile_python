import funcoes

c1, c2, c3, cent1, cent2, cent3 = funcoes.centroide('normals.txt')

print(c1)
print(c2)
print(c3)
a = 0
b = 0
c = 0

for i in cent1:
    a= a + funcoes.distanciaeuclidiana(c1,i)
med1= a/len(cent1)
print (med1)

for i in cent2:
    b= b + funcoes.distanciaeuclidiana(c2,i)
med2= b/len(cent2)
print (med2)

for i in cent3:
    c= c + funcoes.distanciaeuclidiana(c3,i)
med3= c/len(cent3)
print (med3)
