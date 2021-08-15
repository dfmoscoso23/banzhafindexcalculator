list1 =["a","c","v","m","n"]
def combinatoria(listado, dataProcesada):
	if len(listado)==1:
		return dataProcesada
	data = []
	####
	## code
	conj=[[s] for s in listado]
	primer_item=[listado[0]]
	for x in listado[1:]:
		comb=conj[:]
		temp=primer_item[:]
		temp.append(x)
		data.append(temp)
	dataProcesada.append(data)
	#return data	
	####
	#dataProcesada2 = data.extend(dataProcesada) 
	return combinatoria(listado[1:],dataProcesada)

print (combinatoria(list1,[]))
