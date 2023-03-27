import os
os.system('cls')

a = float(input('Digite o coeficiente a:'))
b = float(input('Digite o coeficiente b:'))
c = float(input('Digite o coeficiente c:'))

delta = b**2 - 4*a*c

x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)

print(f'x1= {x1:.2f} \nx2= {x2:.2f}')