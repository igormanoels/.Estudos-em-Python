import os

os.system('cls')
# Criar um algoritmo que leia um valor de hora e informe quantos minutos se passaram desde o início do dia.

horaAt = input("Informe qual a hora atual: ")

hora, min = horaAt.split(':')
tempoPassado = ((int(hora) * 60) + int(min))

print("\nDesde que o dia começou se passaram ", tempoPassado, "minutos")
input("\n\nPressione o \"enter\" para encerrar...")
