lista = []

while true:
	valor = int(input('infome um valor'))
	lista.append(valor)
	if (len(lista)>5): lista.pop(0)
	print(lista)
print('fim do programa!!!')	
