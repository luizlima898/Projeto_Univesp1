lista =[1, 2, 3, 4, 5, 6, 7] 
print (lista)
valor = 6
if valor in lista:
   print("There is the number")
   indice = lista.index(valor)
   print("The number is set in position:", indice)
else:
        print("There is no number") 