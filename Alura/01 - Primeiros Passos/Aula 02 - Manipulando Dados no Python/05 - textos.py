
texto1 = "primeiro"
texto2 = 'segundo'
print(type(texto1), type(texto2))




texto = '  Geovana Alessandra dias Sanyos '
print(texto)


print(texto.upper()) # Caixa alta


print(texto.lower()) # Caixa baixa


print(texto.strip()) # Remove os espaços do texto
 
texto = texto.strip().replace('y', 't').upper() # Acúmulo de métodos
print(texto, '\n\n')



# Entrada de dados
nome = input('Informe seu nome: ')
print(type(nome))

idade = int(input('Informe sua idade: '))
print(type(idade))

nota = float(input('Informe a nota do {nome}: '))
print(type(nota))

situacao = bool(input('Informe se ele está aprovado: '))
print(type(situacao))


print(f'Nome {nome} - nota do teste {nota}', '\n\n')



# OUTRAS FORMAS DE EXIBIR A SAÍDA
nome = "Ana Maria"
idade = 17
print(f"O nome da aluna é {nome} e sua idade é {idade} anos.")


'''
    Cada tipo de saída tem um valor 
    %s para string
    %d para inteiro
    %f para reais
'''
nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, idade_aluno, media_aluno))

# Formatando o valor da nota para duas casas decimais
print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno), '\n\n') 





# Utilizando o FORMAT

nome_aluno = 'Fabricio Daniel'
print('Nome do aluno: {}'.format(nome_aluno))

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é {}, ele tem {} anos e sua média é {}.' .format(nome_aluno, idade_aluno, media_aluno))


