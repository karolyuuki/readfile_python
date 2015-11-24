filex = open ('normals.txt', 'r')
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
