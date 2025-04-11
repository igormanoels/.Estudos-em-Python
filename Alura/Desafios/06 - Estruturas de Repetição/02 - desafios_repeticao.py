'''
2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar 
ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
Considere que a colônia A inicia com 4 elementos e a B com 10.
'''
colonia_a = 4
colonia_b = 10
dias = 0

while(colonia_a <= colonia_b):
    colonia_a *= 1.03
    colonia_b *= 1.015
    dias += 1

print(f'Levou {dias} dias para que a \'colonia A\' supera-se a \'colonia B\'')


