# Propriedades e Métodos de Manipulação de Data em Python

| Método/Propriedade                    | Descrição                                                                                      | Exemplo                                                               |
|---------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `datetime.now()`                      | Retorna a data e hora atual.                                                                   | `datetime.now()`                                                      |
| `datetime.today()`                    | Retorna a data e hora atual (igual a `datetime.now()`).                                        | `datetime.today()`                                                    |
| `datetime.strptime(date_string, format)` | Converte uma string em um objeto datetime usando um formato especificado.                     | `datetime.strptime('2024-01-31', '%Y-%m-%d')`                         |
| `datetime.strftime(format)`           | Converte um objeto datetime em uma string formatada.                                           | `datetime.now().strftime('%Y-%m-%d %H:%M:%S')`                        |
| `datetime.date()`                     | Retorna a data sem a hora do objeto datetime.                                                  | `datetime.now().date()`                                               |
| `datetime.time()`                     | Retorna a hora sem a data do objeto datetime.                                                  | `datetime.now().time()`                                               |
| `datetime.year`                       | Retorna o ano do objeto datetime.                                                              | `datetime.now().year`                                                 |
| `datetime.month`                      | Retorna o mês do objeto datetime.                                                              | `datetime.now().month`                                                |
| `datetime.day`                        | Retorna o dia do objeto datetime.                                                              | `datetime.now().day`                                                  |
| `datetime.hour`                       | Retorna a hora do objeto datetime.                                                             | `datetime.now().hour`                                                 |
| `datetime.minute`                     | Retorna os minutos do objeto datetime.                                                         | `datetime.now().minute`                                               |
| `datetime.second`                     | Retorna os segundos do objeto datetime.                                                        | `datetime.now().second`                                               |
| `datetime.timedelta()`                | Representa uma duração, a diferença entre duas datas ou horas.                                 | `timedelta(days=5, hours=3)`                                          |
| `date.today()`                        | Retorna a data atual.                                                                          | `date.today()`                                                        |
| `date(year, month, day)`              | Cria um objeto de data.                                                                        | `date(2024, 1, 31)`                                                   |
| `date.year`                           | Retorna o ano do objeto date.                                                                  | `date(2024, 1, 31).year`                                              |
| `date.month`                          | Retorna o mês do objeto date.                                                                  | `date(2024, 1, 31).month`                                             |
| `date.day`                            | Retorna o dia do objeto date.                                                                  | `date(2024, 1, 31).day`                                               |
| `date.weekday()`                      | Retorna o dia da semana como um inteiro (segunda-feira=0, domingo=6).                          | `date(2024, 1, 31).weekday()`                                         |
| `date.isoweekday()`                   | Retorna o dia da semana como um inteiro (segunda-feira=1, domingo=7).                          | `date(2024, 1, 31).isoweekday()`                                      |
| `relativedelta()`                     | Usado para operações de data relativas, como adicionar ou subtrair meses ou anos.              | `date.today() + relativedelta(months=+1)`                             |
| `parser.parse(date_string)`           | Converte uma string em um objeto datetime. (Requer instalação do módulo `python-dateutil`)     | `parser.parse('2024-01-31')`                                          |

# Exemplos de Uso

```python
from datetime import datetime, date, timedelta
from dateutil import parser
from dateutil.relativedelta import relativedelta

# Data e hora atuais
now = datetime.now()
print("Data e hora atuais:", now)

# Converter string para datetime
date_str = "2024-01-31"
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
print("Data convertida:", date_obj)

# Adicionar 5 dias a data atual
future_date = now + timedelta(days=5)
print("Data futura:", future_date)

# Adicionar 1 mês a data atual
future_date = date.today() + relativedelta(months=+1)
print("Data futura com 1 mês a mais:", future_date)

# Converter string para datetime usando dateutil
date_obj = parser.parse("2024-01-31")
print("Data convertida com dateutil:", date_obj)
