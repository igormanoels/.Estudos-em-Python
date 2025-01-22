# Caminho para compilar um projeto em python

## Usando pyinstaller
- pyinstaller --onefile --windowed seu_script.py
    - '--onefile' para gerar um arquivo único
    - '--windoed' para gerar a janela do projeto
    - '--noconsole' para não exibir comandos em console/terminal
    - '--console' para gerar saídas no terminal/console, usado para testes

**Opções**
- 1 - pyinstaller --onefile --windowed --distpath "C:LOCAL\Output" "C:LOCAL\Input\seu_arquivo.py" 
- 2 - pyinstaller --onefile --windowed --icon="D:\LOCAL\meu_icone.ico" --distpath "C:LOCAL\Output" "C:LOCAL\Input\seu_arquivo.py"
[Py Installer](https://pyinstaller.org/en/stable/)


## Usando auto-py-to-exe
- 1 - instale pelo terminal 'pip install auto-py-to-exe'
- 2 - pelo terminal use o comando 'auto-py-to-exe'

[auto py to exe](https://pypi.org/project/auto-py-to-exe/#files)

