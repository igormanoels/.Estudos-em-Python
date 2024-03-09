# LÓGICA BOLEANA

"""
a == b          # A é igual a B
a != b          # A é diferente de B
a < b           # A é menor que B
a <= b          # A é menor ou igual a B
a > b           # A é maior que B
a >= b          # A é maior ou igual a B

"""
print("Informe o primeiro valor: ")
a = int(input())
print("Informe o segundo valor: ")
b = int(input())

if a < b:
    print("A é menor que B") # há um tab nessa linha, para que o Python entenda que o print é o comando da condição
elif a == b:
    print("A é igual a B") # caso contrário o resultado é que são iguais
else:
    print("A é maior que B") # se não o resultado será o else

# para o Python NONE e 0 São interpretados como FALSE
    
# ESTRUTURA CONDICIONAL ANINHADA
a = 16
b = 25
c = 27

if a > b:
    if b > c:
        print ("a é maior que b e b é maior que c")
    else: 
        print ("a é maior que b e menor que c")
elif a == b:
    print ("a é igual a b")
else:
    print ("a é menor que b")


# COMPARADOR E (and) e OU (or)

idade = 25

if idade >= 18:
    print("Pode votar e dirigir.")
elif idade >= 16 and  idade <= 17:
    print("Apenas pode votar.")
else:
    print("Não pode votar e nem dirigir.")
