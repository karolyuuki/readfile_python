
def separate_things (value):
    sizeV =(len(value))
    sizeF = sizeV - 1
    lista = []
    if (sizeF < sizeV):
        nlabel = value[sizeF].replace("\n","")
        lista.append(nlabel)
    return lista

filex = open ('C:/Users/Karol/Desktop/Tsukuba/Python/normals.txt', 'r')
list_items = filex.readlines()
size =(len(list_items))
Llabel = list()
attrb = list()
for item in list_items:
    value = item.split(",")
    attrb.append(item[:-2])
    Llabel.append (separate_things(value))

newarchiveW = open('C:/Users/Karol/Desktop/Tsukuba/Python/list_atributes_general.txt', 'w')
for i in attrb: 	
	for j in i:
		newarchiveW.write(str(j))
	newarchiveW.write("\n")
newarchiveW.close()

newarchiveL = open('C:/Users/Karol/Desktop/Tsukuba/Python/list_labels_general.txt', 'w')
for i in Llabel: 	
	for j in i:
		newarchiveL.write(str(j))
		newarchiveL.write(",")
	newarchiveL.write("\n")
newarchiveL.close()
