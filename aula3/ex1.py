h = float(input('Digite o valor da altura da pirâmide' ))
Bmenor = float(input('Digite o valor da base menor' ))
Bmaior = float(input('Digite o valor da base maior' ))
Volume = h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print(f'O volume é {Volume}')