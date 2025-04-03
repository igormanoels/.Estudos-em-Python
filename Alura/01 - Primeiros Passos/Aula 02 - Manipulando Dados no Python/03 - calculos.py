q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500


# A quantidade total de empregados;
total_funcionarios = q_seguranca + q_docente + q_diretoria
print('Total de funcionários: ', total_funcionarios)


# A diferença entre o salário mais baixo e mais alto; e
diferenca_entre_salarios = s_diretoria - s_seguranca
print('Diferença entre o maior e menor salário: ', diferenca_entre_salarios)


# A média ponderada da faixa salarial da escola.


media_salarial = (q_seguranca * s_seguranca + q_docente * s_docente + q_diretoria * s_diretoria) / total_funcionarios
print('Média salarial:', media_salarial)