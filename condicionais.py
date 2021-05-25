"""
if, else, elif

if idade < 18:
    print('Pó passar')
elif idade == 18:
    print('tu tem 18')
else:
    print('não pó passar')
"""

"""
and(e), or(ou), not(não), is (é)

Operadores unários: 
    - not
Operadores binários:
    - and, or, is
    
"""
ativo = True
logado = False

if ativo and not logado:
    print('Bem-vindo usuário!')
else:
    print('ativa ai')

# Se não estiver ativo
if not ativo:
    print('Ativa ai')
else:
    print('ativo')

if ativo is True:
    print('nah')
else:
    print('aaaa')


# ativo é Falso?
print(ativo is False)
