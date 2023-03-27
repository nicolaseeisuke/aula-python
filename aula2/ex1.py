import os
os.system ('cls')

lado1 = float (input('Digite o valor do lado1 do rêtangulo '))
lado2 = float (input('Digite o valor do lado2 do rêtangulo '))
lado3 = float (input('Digite o valor do lado3 do rêtangulo '))
lado4 = float (input('Digite o valor do lado4 do rêtangulo '))
b = float(input('Digite o valor da base do rêtangulo '))
a = float(input('Dite o valor da altura '))
perimetro = (lado1+lado2+lado3+lado4)
area = (b*a)

print(f'O valor do perimetro do retangulo é {perimetro:.2f} cm')
print(f'O valor da area do retangulo é {area:.2f}cm')