'''
 Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____ 
'''

# Problema A

lista_a = [1, 3, 5, 7]
proximo_item_a= lista_a [-1] + 2 
print (f'O próximo número do exercício A: {proximo_item_a}')

# Problema B
lista_b = [2,4,8,16,32,64]
proximo_item_b = lista_b [-1]*2
print (f'O próximo número do exercício B: {proximo_item_b}')

# Problema C
lista_c = [0, 1, 4, 9, 16, 25, 36]
proximo_item_c = len(lista_c)**2
print (f'O próximo número do exercício C: {proximo_item_c}')

# Problema D
lista_d = [4, 16, 36, 64]
proximo_item_d = lista_d[-1]*2
print (f'O próximo número do exercício D: {proximo_item_d}')

#Problema E
lista_e = [1, 1, 2, 3, 5, 8]
proximo_item_e = lista_e [-1] + lista_e[-2]
print (f'O próximo número do exercício E: {proximo_item_e}')

#Problema F 
lista_f = [2,10, 12, 16, 17, 18, 19]
proximo_item_f = lista_f [-1] + 1
print (f'O próximo número do exercício F: {proximo_item_f}')