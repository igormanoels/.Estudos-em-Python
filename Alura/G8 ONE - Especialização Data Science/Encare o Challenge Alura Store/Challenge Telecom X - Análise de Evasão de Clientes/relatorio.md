# Relatório Final
## Introdução
Esta análise examina os dados de clientes de telecomunicações para entender os fatores que influenciam a evasão (Churn). O objetivo é identificar padrões e características de clientes que tendem a cancelar o serviço, permitindo à empresa desenvolver estratégias de retenção mais eficazes. Para a produção deste relatório foi realizado:
- Limpeza e Tratamento de Dados
- Remoção de registros com valores ausentes na variável Churn
- Normalização da estrutura JSON aninhada em colunas planas
- Converção das variáveis categóricas (Sim/Não) para valores binários (1/0)
- Criação a coluna "Contas_Diarias" para análise temporal
- Renomeamos colunas para melhor legibilidade

## Análise Exploratória de Dados
### Distribuição de Churn:
- Aproximadamente 26.5% dos clientes cancelaram o serviço (Churn = "Yes")
### Churn por Categorias:
- Clientes com Fibra Óptica tem maior taxa de Churn (41%) comparado com DSL (19%) ou sem internet (7%)
- Contratos mensais tem taxa de Churn muito maior (42%) que contratos anuais (11%) ou bienais (3%)
- Pagamentos por cheque tem maior taxa de Churn (34%) que outros métodos
### Churn por Variáveis Numéricas:
- Clientes que cancelaram tem menor tempo de contrato (média de 17 meses, contra 37 meses)
- O faturamento mensal é maior para clientes que cancelaram (média de R$74,00, contra R$61,00)
- A conta diária é similar entre os grupos, sugerindo que o valor não é o principal fator
### Conclusões
- O tipo de contrato mensal e serviço de internet por fibra óptica são os maiores fatores de Churn
- Métodos de pagamento eletrônicos estão associados a maior rotatividade
- Clientes novos são mais propensos a cancelar
### Recomendações
- Oferecer incentivos para clientes de fibra óptica migrarem para contratos de longo prazo
- Revisar a experiência de clientes com pagamento eletrônico para identificar problemas
- Desenvolver programas de fidelização para clientes nos primeiros meses
- Investigar a qualidade do serviço de fibra óptica, que pode estar causando insatisfação

