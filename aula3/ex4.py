import os
os.system ('cls')

prestacao = float(input("Digite o valor da prestação em atraso: "))
multa = float(input("Digite a porcentagem da multa pelo atraso: "))
qtde_dias = int(input("Digite a quantidade de dias de atraso: "))

valor_atualizado = prestacao + (prestacao * multa/100) + (prestacao * 0.01 * qtde_dias)

print("O valor da prestação atualizado é de R$ {:.2f}".format(valor_atualizado))