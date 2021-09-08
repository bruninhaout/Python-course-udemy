#   String tudo em aspas.

nome = 'bruna de paula cordeiro'

nome2 = 'BRUNA DE PAULA CORDEIRO'

print(nome.upper())
print(nome.title())
print(nome2.lower())
print(nome2.title())

nome3 = nome2.title()
#  Separa como uma lista, cada palavra ['Bruna', 'de', 'Paula', 'Cordeiro']
print(nome3.split())
print(nome[0:5])  # Slice de estring

#  ['  0,      1,     2,         3'   ]
#  ['bruna', 'de', 'paula', 'cordeiro']
print(nome.split()[0])

print(nome[::-1])  # inversão de string
"""
[::-1]  -> comece do primeiro elemento, vá até o ultimo e inverta (escreve algo ao contrario)
"""

print(nome.replace('a', 'o'))  # trocar de letra, troca todas as letra equivalentes

frase = 'socorram me subino onibus em marrocos'  # Palíndromo (mesmo ao contrário)
print(frase[::-1])
