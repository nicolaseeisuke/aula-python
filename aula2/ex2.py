import os
os.system ('cls')

salario = float(input('Digite seu salário '))
comissao = (5*salario)/100
ajuste= (comissao+salario)
print(f'Seu salario é R$ {salario:.2f} ')
print(f'Como a comissão seu salário fica {ajuste:.2f}')