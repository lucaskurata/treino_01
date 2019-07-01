lista = [2,4,6,8,10]

maior = 0
for i in lista:
    if i > maior:
        maior = i
lista.remove(i)
print(lista)
