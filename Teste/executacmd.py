import subprocess

def abrir_prompt_de_comando():
    try:
        subprocess.Popen(['notepad']) # notepad abre o cmd
    except Exception as e:
        print("Erro ao abrir o prompt de comando:", e)

# Chamando a função para abrir o prompt de comando
abrir_prompt_de_comando()
