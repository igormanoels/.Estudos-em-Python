import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")  # Escolha um tema: 'superhero', 'darkly', 'flatly', etc.
root.title("Estilo com ttkbootstrap")
root.geometry("300x200")

# Botão estilizado
btn = ttk.Button(root, text="Clique Aqui", bootstyle=SUCCESS)
btn.pack(pady=20)

# Campo de entrada estilizado
entry = ttk.Entry(root)
entry.pack(pady=10)

root.mainloop()
