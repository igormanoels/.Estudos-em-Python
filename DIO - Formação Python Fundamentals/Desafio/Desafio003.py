'''
    Em nossa aplicação financeira, identificamos a necessidade de rastrear e auditar as ações dos usuários para garantir a
segurança e a integridade das operações. O console tem sido útil até agora, mas a quantidade crescente de atividades torna
difícil acompanhar todas as operações em tempo real. Portanto, decidimos que é vital registrar essas informações
em um arquivo para análise posterior e backup contínuo.

Modificar o atual decorador de log, que imprime informações no console, para que ele salve essas informações em um
arquivo de log, possibilitando uma revisão mais fácil e uma análise mais detalhada das operações dos usuários.

O decorador deve registrar o seguinte para cada chamada de função:
1. Data e hora atuais
2. Nome da função
3. Argumentos da função
4. Valor retornado pela função
5. O arquivo de log deve ser chamado log.txt.
6. Se o arquivo log.txt já existir, os novos logs devem ser adicionados ao final do
arquivo.
7. Cada entrada de log deve estar em uma nova linha.
'''