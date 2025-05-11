'''
# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem 
# "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
'''
turno = input('Informe em qual turno você estuda: ')

if turno == 'manhã' or turno == 'Manhã' or turno == 'manha' or turno == 'Manha' or turno == 'diurno' or turno == 'diurno':
    print('Bom dia!')
elif turno == 'tarde' or turno == 'Tarde' or turno == 'vespertino' or turno == 'Vespertino':
    print('Boa tarde!')
elif turno == 'noite' or turno == 'Noite' or turno == 'Noturno' or turno == 'noturno':
    print('Boa noite!')
else: 
    print('Valor inválido')


