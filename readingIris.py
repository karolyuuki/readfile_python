def separate_things (sizeV, value):
    sizeF = sizeV - 1
    lista = []
    a = 0
    while (a < sizeF):
         lista.append(value[a])
         a = a+1
    return lista

def separate_things2 (sizeV, value):
    sizeF = sizeV - 1
    lista = []
    if (sizeF < sizeV):
        nlabel = value[sizeF].replace("\n","")
        lista.append(nlabel)
    return lista

filex = open ('C:/Users/Karol/Desktop/Tsukuba/Python/iris.txt', 'r')
list_items = filex.readlines()
size =(len(list_items))
print (size)
Latrb = list()
Llabel = list()
for item in list_items:
    value = item.split(",")
    n =(len(value))
    Latrb.append (separate_things(n, value))
    Llabel.append (separate_things2(n, value))


newarchiveA = open('C:/Users/Karol/Desktop/Tsukuba/Python/list_atributes.txt', 'w')
newarchiveA.write (str(Latrb))
newarchiveA.close()

newarchiveL = open('C:/Users/Karol/Desktop/Tsukuba/Python/list_labels.txt', 'w')
newarchiveL.write (str(Latrb))
newarchiveL.close()
