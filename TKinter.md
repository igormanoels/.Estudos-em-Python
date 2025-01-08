# Tabela com os principais comandos do **Tkinter** que podem ser usados para personalizar as telas da sua aplicação. 

### **A tabela está dividida por widgets e comandos relacionados:**

| **Widget/Elemento**      | **Comando**                           | **Descrição**                                                                                  |
|---------------------------|---------------------------------------|------------------------------------------------------------------------------------------------|
| **Janela (Tk)**           | `title("Texto")`                     | Define o título da janela.                                                                    |
|                           | `geometry("LxA+X+Y")`                | Define o tamanho (Largura x Altura) e posição (X, Y) da janela.                               |
|                           | `resizable(False, False)`            | Impede o redimensionamento da janela (horizontal, vertical).                                  |
|                           | `config(bg="cor")`                   | Define a cor de fundo da janela.                                                              |
| **Label**                 | `Label(text="Texto", fg="cor")`      | Cria um rótulo com texto e cor da fonte.                                                      |
|                           | `font=("Fonte", Tamanho, "Estilo")`  | Define a fonte, tamanho e estilo (normal, bold, italic).                                       |
|                           | `bg="cor"`                           | Define a cor de fundo do rótulo.                                                              |
| **Botão (Button)**        | `Button(text="Texto", command=func)` | Cria um botão com texto e associa uma função ao clique.                                        |
|                           | `width` e `height`                   | Define a largura e altura do botão.                                                           |
|                           | `state=DISABLED`                     | Desabilita o botão.                                                                           |
|                           | `activebackground="cor"`             | Define a cor de fundo quando o botão é pressionado.                                           |
| **Entrada de texto**      | `Entry(width=N)`                     | Cria um campo de entrada com largura especificada.                                             |
|                           | `show="*"`                           | Oculta o texto digitado (útil para senhas).                                                   |
| **Texto (Text)**          | `Text(height=N, width=N)`            | Cria uma área de texto com largura e altura específicas.                                       |
|                           | `insert(END, "Texto")`               | Insere texto no final da área de texto.                                                       |
|                           | `get("1.0", END)`                    | Obtém o texto da área de texto (início até o final).                                          |
| **Frame**                 | `Frame(bg="cor")`                    | Cria um contêiner para organizar outros widgets.                                              |
|                           | `pack()` ou `grid()`                 | Posiciona o frame na janela.                                                                  |
| **Canvas**                | `Canvas(width, height, bg="cor")`    | Cria uma área para desenhos e formas geométricas.                                             |
|                           | `create_rectangle(x1, y1, x2, y2)`   | Desenha um retângulo no canvas.                                                               |
|                           | `create_oval(x1, y1, x2, y2)`        | Desenha uma elipse no canvas.                                                                 |
| **Menu**                  | `Menu`                               | Cria um menu suspenso.                                                                        |
|                           | `add_command(label="Texto", command=func)` | Adiciona um item ao menu com uma função associada.                                      |
|                           | `add_separator()`                    | Adiciona um separador no menu.                                                                |
| **Checkbutton**           | `Checkbutton(text="Texto")`          | Cria uma caixa de seleção.                                                                    |
|                           | `variable=var`                       | Associa a caixa a uma variável (IntVar, StringVar).                                           |
| **Radiobutton**           | `Radiobutton(text="Texto")`          | Cria um botão de opção.                                                                       |
|                           | `value=N, variable=var`              | Define o valor e associa a uma variável para seleção.                                         |
| **Listbox**               | `Listbox(height=N)`                  | Cria uma lista com N linhas visíveis.                                                         |
|                           | `insert(END, "Texto")`               | Adiciona um item à lista.                                                                     |
|                           | `get(0, END)`                        | Obtém todos os itens da lista.                                                                |
| **Scrollbar**             | `Scrollbar(orient="vertical")`       | Cria uma barra de rolagem (vertical ou horizontal).                                           |
|                           | `config(command=widget.yview)`       | Associa a barra de rolagem a um widget, como `Text` ou `Listbox`.                             |
| **Posicionamento**        | `pack(side=TOP, fill=X)`             | Posiciona o widget no topo, preenchendo horizontalmente.                                       |
|                           | `grid(row=N, column=N)`              | Posiciona o widget em uma grade, na linha e coluna especificadas.                             |
|                           | `place(x=N, y=N)`                    | Posiciona o widget em coordenadas absolutas.                                                  |


##


# Customização

Tabela com as principais opções de customização de estilo para componentes do Tkinter, organizadas por tipo de widget. 
A tabela inclui propriedades para cores, fontes, bordas e outros aspectos visuais.

### **Tabela de Customização de Estilos em Tkinter**

| **Widget** | **Propriedade**         | **Descrição**                                     | **Exemplo de Valor**          |
|------------|-------------------------|-------------------------------------------------|-------------------------------|
| **Janela** | `bg`                    | Cor de fundo da janela.                         | `#F0F8FF` (hexadecimal)       |
|            | `title`                 | Título da janela.                               | `"Minha Aplicação"`           |
|            | `geometry`              | Dimensões e posição da janela.                  | `"400x300+100+100"`           |
| **Button** | `text`                  | Texto exibido no botão.                         | `"Clique Aqui"`               |
|            | `bg` / `background`     | Cor de fundo do botão.                          | `"#1E90FF"`                   |
|            | `fg` / `foreground`     | Cor do texto no botão.                          | `"#FFFFFF"`                   |
|            | `font`                  | Fonte do texto.                                 | `("Arial", 12, "bold")`       |
|            | `activebackground`      | Cor de fundo ao pressionar.                     | `"#87CEFA"`                   |
|            | `activeforeground`      | Cor do texto ao pressionar.                     | `"#000000"`                   |
|            | `relief`                | Estilo da borda.                                | `"flat"`, `"ridge"`, `"solid"`|
|            | `bd` / `borderwidth`    | Largura da borda.                               | `3`                           |
| **Label**  | `text`                  | Texto exibido no rótulo.                        | `"Bem-vindo!"`                |
|            | `bg`                    | Cor de fundo do rótulo.                         | `"#F0F8FF"`                   |
|            | `fg`                    | Cor do texto.                                   | `"#000000"`                   |
|            | `font`                  | Fonte do texto.                                 | `("Verdana", 14, "italic")`   |
|            | `anchor`                | Alinhamento do texto no rótulo.                 | `"center"`, `"w"`, `"e"`      |
| **Entry**  | `bg`                    | Cor de fundo da caixa de texto.                 | `"#FFFFFF"`                   |
|            | `fg`                    | Cor do texto digitado.                          | `"#000000"`                   |
|            | `font`                  | Fonte do texto.                                 | `("Courier", 12)`             |
|            | `highlightbackground`   | Cor da borda ao perder foco.                    | `"#D3D3D3"`                   |
|            | `highlightcolor`        | Cor da borda ao ganhar foco.                    | `"#1E90FF"`                   |
|            | `width`                 | Largura do campo em caracteres.                 | `20`                          |
| **Frame**  | `bg`                    | Cor de fundo do frame.                          | `"#D3D3D3"`                   |
|            | `relief`                | Estilo da borda do frame.                       | `"sunken"`, `"raised"`        |
|            | `bd` / `borderwidth`    | Largura da borda do frame.                      | `2`                           |
| **Canvas** | `bg`                    | Cor de fundo do canvas.                         | `"#FFFFFF"`                   |
|            | `height`                | Altura do canvas.                               | `200`                         |
|            | `width`                 | Largura do canvas.                              | `300`                         |
| **Listbox**| `bg`                    | Cor de fundo da lista.                          | `"#F0F8FF"`                   |
|            | `fg`                    | Cor do texto na lista.                          | `"#000000"`                   |
|            | `font`                  | Fonte do texto.                                 | `("Arial", 12)`               |
|            | `selectbackground`      | Cor de fundo do item selecionado.               | `"#1E90FF"`                   |
|            | `selectforeground`      | Cor do texto do item selecionado.               | `"#FFFFFF"`                   |
| **Scrollbar**| `bg`                  | Cor de fundo da barra de rolagem.               | `"#D3D3D3"`                   |
|             | `troughcolor`          | Cor do trilho da barra.                         | `"#F0F8FF"`                   |


### **Como Usar os Estilos**
1. **Definir diretamente nos widgets:**  
   Passe os valores como argumentos ao criar os widgets.

   ```python
   btn = Button(root, text="Clique Aqui", bg="#1E90FF", fg="#FFFFFF")
   ```

2. **Centralizar com funções:**  
   Crie funções para encapsular os estilos padrão e reutilize em toda a aplicação.

3. **Usar `ttk.Style` para widgets avançados:**  
   Ideal para customizações globais.


##


# TTK Style

### MODELO 
    from tkinter import *
    from tkinter import ttk

    # Função para configurar estilos
    def configurar_estilo():
        style = ttk.Style()
        
        # Estilo para ttk.Button
        style.configure(
            "TButton",                 # Nome do estilo padrão para ttk.Button
            background="#1E90FF",      # Cor de fundo
            foreground="#FFFFFF",      # Cor do texto
            font=("Arial", 12, "bold"),
            padding=10                 # Espaçamento interno
        )
        style.map(
            "TButton",
            background=[("active", "#87CEFA")],  # Cor ao pressionar
            foreground=[("active", "#000000")]  # Texto ao pressionar
        )
        
        # Estilo para ttk.Label
        style.configure(
            "TLabel",
            background="#F0F8FF",      # Cor de fundo
            foreground="#000000",      # Cor do texto
            font=("Verdana", 14, "italic")
        )

    root = Tk()
    root.geometry("300x300")

