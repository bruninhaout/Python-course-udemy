# Um encanador recebe pelo numero de dias trabalhados, sabendo que cada dia vale R$ 30,00, imprimir a quantia liquida e são descontados 8% de imposto de renda

d = int(input('Dias trabalhados = '))
valor_sem_desconto = 30 * d
final = valor_sem_desconto - (valor_sem_desconto * 0.08)
print(f'Valor bruto = R$ {valor_sem_desconto}\nValor líquido = R$ {final}')
