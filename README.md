# aulas-segundo-bimestre
aulas de listas
listadevalores =[]
while True:
	valor = int(input('informe um valor: '))
	listadevalores.append(valor)
	Print(listadevalores)
	if (valor==0): break 

#.pop é um metodo que elimina uma determinada posição
#.insert adiciona valores a lista 



----------------------------------------------------------
maximo=listadevalores[0]
minimo=listadevalores[0]
soma=listadevalores[0]
for posição in range(1, len(listadevalores)):
	if (listadevalores[posição]> maximo):maximo=listadevalores[posição]
	if (listadevalores[posição]<minimo):maximo=listadevalores[posição]
	soma= soma+ listadevalores[posição]
print(maximo)
print(minimo)
----------------------------------------------
print(listadevalores)
if valor==0:break

print ('')
listadevalores.pop()
print(listadevalores)

print ('')
listadevalores.pop(2)
print(listadevalores)

print ('')
y=int(input('informe um novo valor'))
listadevalores.insert(2,y)
print(listadevalores)
---------------------------------------------



