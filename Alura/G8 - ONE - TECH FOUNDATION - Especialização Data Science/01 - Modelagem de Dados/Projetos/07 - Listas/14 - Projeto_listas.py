'''
14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe 
fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta 
e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas 
listas correspondem às espécies de plantas e animais nas áreas, respectivamente.


Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade 
biológica. Dica: use as funções built-in sum() e len(). 
'''

areas = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496],  
         'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

for chave, valor in areas.items():
    media = round(sum(valor) / len(valor))
    print(f'A média da {chave} é de {media} espécies.')


