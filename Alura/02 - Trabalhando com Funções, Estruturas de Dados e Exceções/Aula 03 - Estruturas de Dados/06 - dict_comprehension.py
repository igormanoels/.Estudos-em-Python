# MÉTODO DE IMPLEMENTAR
# {chave: valor for item in lista}

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]


coluna = ["Notas", "Média Final", "Situação"]

# Colunas com os tipos dos dados (exceto nome)
cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}

print(cadastro)



# adicionando o nome dos estudantes, extraindo apenas seus nomes da lista de tuplas
cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]




