import os
os.system('cls')

distancia = float(input('Digite a distância entre a cicade 1 e cidade 2 '))
tempo = float(input('Digite o tempo de da viagem'))
vm = (distancia/tempo)

print(f'A velocidade média é {vm:.2f} km/h')
