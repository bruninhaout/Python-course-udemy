"""
Recebendo dados do usuario
input() -> todo dado via input é do tipo string
Em python string é tudo que estiver em:
- Aspas simples;
- Aspas dupla;
- Aspas simples triplas;
- Aspas duplas triplas;
"""

#   print("Digite o seu nome:")
#   nome = input()
nome = input('Qual seu nome? \n')

#  print("Digite a sua idade")
#  idade = input()
ano = int(input())
print(ano)
idade = int(input('Digite a sua idade: \n'))

# Antigo -> print('Seu nome eh: %s' % nome)
# Moderno -> print('Seu nome eh: {0}' .format(nome))
print(f'Seu nome sera: {nome}')
print(nome)

# Antigo ->print('Seu nome eh: %s, e sua idade: %s' % (nome, idade))
# Moderno -> print('Seu nome eh: {0}, e sua idade: {1}' .format(nome, idade))
print(f'Agora sabemos que seu nome eh: {nome},e sua idade {idade}')

"""
# int(idade) => Cast
Cast é uma 'conversão' de um tipo de dado para outro 
"""
ano = 2020 - idade
print(f'A {nome} nasceu em {ano}')
