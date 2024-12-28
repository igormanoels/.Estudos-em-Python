import tkinter as tk

# Função para atualizar o conteúdo do Entry
def atualizar_entry(novo_valor):
    local_var.set(novo_valor)  # Atualiza o valor do StringVar, refletindo no Entry

# Configuração da janela principal
root = tk.Tk()
root.title("Atualizar Entry Dinamicamente")

# Variável de controle
local_var = tk.StringVar(value="Inicial")  # Valor inicial

# Campo de texto (Entry) vinculado ao StringVar
etDestino = tk.Entry(root, textvariable=local_var)
etDestino.pack(pady=10)

# Botão para simular uma atualização do "local"
botao = tk.Button(root, text="Atualizar Local", command=lambda: atualizar_entry("Novo Local"))
botao.pack(pady=10)

# Outro botão para testar outra atualização
botao2 = tk.Button(root, text="Atualizar para 'Outro Local'", command=lambda: atualizar_entry("Outro Local"))
botao2.pack(pady=10)

root.mainloop()
