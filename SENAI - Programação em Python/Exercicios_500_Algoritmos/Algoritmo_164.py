import os
import time

os.system('cls')
'''
    Desafio: Já pensou em fazer em simular uma pausa usando a estrutura para
        comecei
        <após alguns segundos>
        parei
'''

for i in range(60):
    time.sleep(1)
    print(f"{i+1} segundo(s).")
else:
    print("Fim do cronometro.")
    
input("\n\nPressione o \"enter\" para encerrar...")
