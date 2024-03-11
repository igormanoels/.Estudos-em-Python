| Função          | Descrição                                                    | Exemplo                                                   |
|-----------------|--------------------------------------------------------------|-----------------------------------------------------------|
| `capitalize()`  | Retorna uma cópia da string com o primeiro caractere em maiúsculo e o restante em minúsculo. | `'python'.capitalize()` retorna `'Python'` |
| `casefold()`    | Retorna uma versão da string transformada em minúsculas, tratando de forma mais agressiva as letras maiúsculas. | `'PyThOn'.casefold()` retorna `'python'` |
| `center(width[, fillchar])` | Retorna a string centralizada dentro de uma string de largura especificada, com caracteres de preenchimento opcionais à esquerda e à direita. | `'Python'.center(10, '-')` retorna `'--Python--'` |
| `count(sub[, start[, end]])` | Retorna o número de ocorrências de uma substring na string. | `'banana'.count('a')` retorna `3` |
| `encode([encoding[, errors]])` | Retorna uma versão codificada da string como uma sequência de bytes. | `'ä'.encode('utf-8')` retorna `b'\xc3\xa4'` |
| `endswith(suffix[, start[, end]])` | Verifica se a string termina com o sufixo especificado. | `'hello world'.endswith('world')` retorna `True` |
| `expandtabs([tabsize])` | Retorna uma cópia da string com as tabulações (`\t`) expandidas usando espaços. | `'foo\tbar'.expandtabs(4)` retorna `'foo bar'` |
| `find(sub[, start[, end]])` | Retorna o índice da primeira ocorrência de uma substring na string, ou -1 se a substring não for encontrada. | `'hello world'.find('world')` retorna `6` |
| `format(*args, **kwargs)` | Formata a string substituindo campos de substituição por seus valores correspondentes. | `'{} + {} = {}'.format(2, 3, 2+3)` retorna `'2 + 3 = 5'` |
| `format_map(mapping)` | Similar a `format()`, mas aceita um dicionário de mapeamento como argumento. | `'Meu nome é {nome}'.format_map({'nome': 'João'})` retorna `'Meu nome é João'` |
| `index(sub[, start[, end]])` | Similar a `find()`, mas levanta uma exceção `ValueError` se a substring não for encontrada. | `'hello world'.index('world')` retorna `6` |
| `isalnum()`     | Retorna `True` se todos os caracteres da string são alfanuméricos. | `'abc123'.isalnum()` retorna `True` |
| `isalpha()`     | Retorna `True` se todos os caracteres da string são alfabéticos. | `'abc'.isalpha()` retorna `True` |
| `isascii()`     | Retorna `True` se todos os caracteres da string são ASCII. | `'abc'.isascii()` retorna `True` |
| `isdecimal()`   | Retorna `True` se todos os caracteres da string são decimais. | `'123'.isdecimal()` retorna `True` |
| `isdigit()`     | Retorna `True` se todos os caracteres da string são dígitos. | `'123'.isdigit()` retorna `True` |
| `isidentifier()`| Retorna `True` se a string for um identificador válido em Python. | `'var_1'.isidentifier()` retorna `True` |
| `islower()`     | Retorna `True` se todos os caracteres da string estiverem em minúsculas. | `'abc'.islower()` retorna `True` |
| `isnumeric()`   | Retorna `True` se todos os caracteres da string forem numéricos. | `'123'.isnumeric()` retorna `True` |
| `isprintable()` | Retorna `True` se todos os caracteres da string forem imprimíveis. | `'hello\nworld'.isprintable()` retorna `False` |
| `isspace()`     | Retorna `True` se todos os caracteres da string forem espaços em branco. | `'   '.isspace()` retorna `True` |
| `istitle()`     | Retorna `True` se a string estiver em formato de título. | `'Hello World'.istitle()` retorna `True` |
| `isupper()`     | Retorna `True` se todos os caracteres da string estiverem em maiúsculas. | `'ABC'.isupper()` retorna `True` |
| `join(iterable)`| Concatena os elementos de um iterable usando a string como delimitador. | `','.join(['a', 'b', 'c'])` retorna `'a,b,c'` |
| `ljust(width[, fillchar])` | Retorna a string justificada à esquerda em uma string de largura especificada, com caracteres de preenchimento opcionais à direita. | `'Python'.ljust(10, '-')` retorna `'Python----'` |
| `lower()`       | Retorna uma versão da string em minúsculas. | `'PyThOn'.lower()` retorna `'python'` |
| `lstrip([chars])` | Retorna uma cópia da string com caracteres de espaços em branco removidos do início. | `'   Python   '.lstrip()` retorna `'Python   '` |
| `maketrans(x[, y[, z]])` | Retorna uma tabela de tradução para usar com o método `translate()`. | `str.maketrans('abc', '123')` retorna `{97: 49, 98: 50, 99: 51}` |
| `partition(sep)` | Divide a string na primeira ocorrência do separador e retorna uma tupla contendo a parte antes do separador, o separador em si e a parte após o separador. | `'hello world'.partition(' ')` retorna `('hello', ' ', 'world')` |
| `replace(old, new[, count])` | Retorna uma cópia da string com todas as ocorrências de uma substring substituídas por outra substring. | `'hello world'.replace('world', 'python')` retorna `'hello python'` |
| `rfind(sub[, start[, end]])` | Similar a `find()`, mas retorna o índice da última ocorrência da substring. | `'hello world'.rfind('l')` retorna `9` |
| `rindex(sub[, start[, end]])` | Similar a `index()`, mas retorna o índice da última ocorrência da substring. | `'hello world'.rindex('l')` retorna `9` |
| `rjust(width[, fillchar])` | Retorna a string justificada à direita em uma string de largura especificada, com caracteres de preenchimento opcionais à esquerda. | `'Python'.rjust(10, '-')` retorna `'----Python'` |
| `rpartition(sep)` | Divide a string na última ocorrência do separador e retorna uma tupla contendo a parte antes do separador, o separador em si e a parte após o separador. | `'hello world'.rpartition(' ')` retorna `('hello', ' ', 'world')` |
| `rsplit([sep[, maxsplit]])` | Divide a string nos espaços em branco e retorna uma lista. | `'hello world'.rsplit()` retorna `['hello', 'world']` |
| `rstrip([chars])` | Retorna uma cópia da string com caracteres de espaços em branco removidos do final. | `'   Python   '.rstrip()` retorna `'   Python'` |
| `split([sep[, maxsplit]])` | Divide a string nos espaços em branco e retorna uma lista. | `'hello world'.split()` retorna `['hello', 'world']` |
| `splitlines([keepends])` | Divide a string em linhas e retorna uma lista de strings. | `'hello\nworld'.splitlines()` retorna `['hello', 'world']` |
| `startswith(prefix[, start[, end]])` | Verifica se a string começa com o prefixo especificado. | `'hello world'.startswith('hello')` retorna `True` |
| `strip([chars])` | Retorna uma cópia da string com caracteres de espaços em branco removidos do início e do final. | `'   Python   '.strip()` retorna `'Python'` |
| `swapcase()`    | Retorna uma versão da string onde maiúsculas são convertidas em minúsculas e vice-versa. | `'PyThOn'.swapcase()` retorna `'pYtHoN'` |
| `title()`       | Retorna uma versão da string com as primeiras letras de cada palavra em maiúsculas. | `'hello world'.title()` retorna `'Hello World'` |
| `translate(table)` | Retorna uma cópia da string onde cada caractere foi mapeado através da tabela de tradução. | `'abc'.translate(str.maketrans('abc', '123'))` retorna `'123'` |
| `upper()`       | Retorna uma versão da string em maiúsculas. | `'python'.upper()` retorna `'PYTHON'` |
| `zfill(width)`  | Retorna uma cópia da string preenchida com zeros à esquerda para atingir a largura especificada. | `'42'.zfill(5)` retorna `'00042'` |