import os
os.system('cls')


from datetime import datetime, date, timedelta
'''
data = datetime.date(2024, 1 , 31) # Ano, mes, dia
print(data)
'''
print(datetime.now()) # Imprime a data e hora agora 
print(datetime.today()) # imprime a data e hora agora

print(date.today()) # Imprime a hora



####################################################################################################################################################
data_atual = datetime(2023, 7, 19, 13, 45) # Insere data com hora
print(data_atual)

data_futura = data_atual + timedelta(weeks=1) # Retorna a soma da data, com um valor. Ex. 1 semana
print(data_futura)


####################################################################################################################################################
data_formatada = (data_futura.strftime("%d/%m/%Y - %H:%M")) # Formata data e hora
print(data_formatada)

# Outra forma é usando a formatação gravada em uma variável
formato_data = "%d/%m/%Y"
formato_hora = "%H:%M"

print(date.today().strftime(formato_data)) # apenas é possivel usar um argumento


####################################################################################################################################################
import pytz # pip install pytz para funcionar

d = datetime.now(pytz.timezone("America/Sao_Paulo"))
print("Hora em São Paulo:", d.strftime(formato_hora))
d = datetime.now(pytz.timezone("Asia/Hong_Kong"))
print("Hora em Hong Kong:", d.strftime(formato_hora))