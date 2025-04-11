''' 
2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve 
um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
'''
porcentagem = int(input('Informe a porcentagem de produção: '))

if porcentagem == 0:
    print('Não houve crescimento!')
elif porcentagem > 0:
    print(f'Houve um crescimento de {porcentagem}%')
else:
    print(f'Houve um decrescimento de {porcentagem}%')


