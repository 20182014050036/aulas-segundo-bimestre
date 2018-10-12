lista=[]

valor_n = int(input('Informe o Valor de N: '))
#contador = 1
valor_anterior = 0
valor_atual = 1
fibonacci = 1
for contador in range(1, valor_n+1):
   lista.insert(contador, valor_atual)
   fibonacci = valor_atual + valor_anterior
   valor_anterior = valor_atual
   valor_atual = fibonacci
  
  
print(lista)
