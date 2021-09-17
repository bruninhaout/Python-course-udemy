# ler numero inteiro, imprimir a soma do sucessor de seu triplo com o antecessor de seu dobro

num = int(input('Numero = '))
suc = (num*3)+1
ant = (num*2)-1
soma = suc + ant
print(f'Resultado = {soma}')
