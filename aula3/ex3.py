import os 
os.system ('cls')

anos = int(input('Digite sua idade em anos:' ))
meses = int(input('Digite a quantidade de meses além dos anos:' ))
dias = int(input('Digite sua idade em anos:' ))

idade = anos * 365 + meses * 30 + dias

print(f'A sua idade expressa em dias é {idade}')