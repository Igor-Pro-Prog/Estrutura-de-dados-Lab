l = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
l2 = []
cont=0

#imprime o maior número:
print ("imprime o maior número:")
print(max(int(l) for l in l))
#imprime o menor número:
print ("o menor número é")
print(min(int(l) for l in l))
#impreme os números pares:
print ("os números pares são:")
for valor in l:
    if valor % 2 == 0:
        l2.append(valor)

print(l2)
#imprime o número de ocorrencias do primeiro elemento na lista:
print ("número de ocorrencias do primeiro elemento na lista:")
cont = 0
for i in range(len(l)):
  if l[i] == 3:
   cont += 1
print(cont)

#imprime a media dos elementos:
print("imprime a media dos elementos:")
count = 0
for i in l: 
    count += i 
      
avg = count/len(l) 
  
print("soma = ", count) 
print("média = ", avg)
#imprime a soma dos elementos de valor negativo:
print("imprime a soma dos elementos de valor negativo:")
soma_dos_negativos = 0
for n in l:
    if n < 0:
        soma_dos_negativos += n # some o valor de n ao total já computado
print('A soma dos elementos negativos é = {}'.format(soma_dos_negativos))
