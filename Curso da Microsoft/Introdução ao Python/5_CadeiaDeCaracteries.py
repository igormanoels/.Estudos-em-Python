# TRABALHANDO COM CADEIA DE CARACTERES

fato = "Na Lua não existe atmosféra."
print(fato)

fato2 = fato + " Nenhum som pode ser ouvido na Lua."
print(fato2) # Para adicionar uma outra cadeia de caracteres você precisa incluir as duas em outra variável

aspas = 'Essa fase possui um item com "aspas" no meio da frase'
print(aspas) # Para usar aspas no meio da frase, usar aspas simples na saída do texto

aspasMul = """Esse texto possuí um trecho com "aspas" e 'aspas simples'."""
print(aspasMul)

quebralinha = "\nPrimeiro Parágrafo \nSegundo Parágrafo \nTerceiro Parágrafo"
print(quebralinha)

quebralinha2 = """
Outra forma de 1º Parágrafo
2º Parágrafo
3º Parágrafo
"""
print(quebralinha2)

print("esse é um título".title())       # Cada primeira letra da sentença ficará em caixa alta

# O mesmo pode ser feito com uma variável
heading = "temperaturas e fatos sobre a lua"
heading_caixaalta = heading.title()
print(heading_caixaalta)

# Dividindo a cadeia de caractes
heading_lista = heading.split()     # Converte a cadeia em um vetor de palavras
print(heading_lista)                # Chama a lista completa
print(heading_lista[4])             # Chama o elemento do vetor a partir da posição 0
tamanho = len(heading_lista)        # Atribui o tamanho do vetor a uma variavel, contando os elemento a partir de 1
print(tamanho)                      # exibe o tamanho do vetor

temperatura = "Daylight: 260 F\n Nighttime: -280 F"         # O \n pode ser utulizado como quebra de sentença, criando duas posições
temperatura_lista = temperatura.split('\n')                     
print(temperatura_lista) 

data = "29/01/2024"
data_lista = data.split('/')            #O mesmo pode ser feito ao atribuir um elemento como '/' como em data
print(data_lista)
dia = (data_lista[0])                   # Aqui você chama o elemento que deseja do vetor
print("Hoje é dia " , dia)

print("Lua" in heading)       # Procura dentro da sentença existe o valor "Lua", como está escrito "lua" ele retorna FALSE
print("lua" in heading)       # Retorna TRUE porque está escrito extamente igual

print(heading.find("lua"))    # Procura em qual posição a palavra lua está localizada 
# Quando a palavra não é localizada o programa retorna -1

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars")) # 1 vez
print(temperatures.count("Moon")) # 0 vez
# Retorna o número total de ocorrências de uma determinada palavra em uma cadeia de caracteres

print("The Moon And The Earth".lower())         # Converte a sequencia de caracteres para minuscula
print("The Moon And The Earth".upper())         # Converte a sequencia de caracteres para maiuscula
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())           # Converte a cadeia de texto para minuscula e verifica se conte o valor desejado

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
# altera uma palavra por outra dentro da cadeia de caracteres

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))                 # Reuni novamente os itens de uma cadeia que foram separados

valor = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % valor)
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# inclui na sentença o valor correspondente a variavel


print("On the Moon, you would weigh about {} of your weight on Earth.".format((valor)))
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", valor))
# Inclui na sentença o item desejado, com o uso das chaves para indicar o item que irá subistituir, nas chaves vai a posição do vetor


nome = 'Igor'
planeta = 'Marte'
gravidade = 1.43
print("A gravidade segundo {0} \n-------------------------- \nNome do planeta: {1} \nGravidade:  {2}".format(nome, planeta, gravidade))



planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)                                              # Exibe o vetor
print("There are", len(planets), "planets")                 #Exibe a quantidade de itens do vetor
planets.append("Pluto")                                     # Inclui mais uma variável para o vetor
print("Actually, there are", len(planets), "planets")       # Exibe a quantidade de itens do vetor
print(planets[-1], "is the last planet")                    # Exibe o último item do vetor
planets_before_earth = planets[0:2]                         # Exibe apenas os indices desejados em intervalor de 0 a 2
print(planets_before_earth)                                 # o mesmo pode ser feito se a entrada for [ :2] ou do 3º ao último [3:8] 


amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
regular_satellite_moons = amalthea_group + galilean_moons           # Concatena duas listas
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort()                                      # Classifica em ordem alfabética
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True)                          # Classifica a lista em ordem reversa
print("The regular satellite moons of Jupiter are", regular_satellite_moons)