# Questão 4 — Uso de IA para Produtividade

## Ferramenta utilizada

Claude (Anthropic)

## Problema a ser resolvido

A gestão não possui uma visão rápida e consolidada dos chamados recebidos no mês. Atualmente é necessário consultar planilhas manualmente para identificar quantos chamados foram abertos, resolvidos, encaminhados ao desenvolvimento, pendentes ou fora do prazo.

O objetivo seria utilizar Inteligência Artificial para auxiliar na criação de um painel simples de acompanhamento utilizando os dados já registrados na planilha de chamados.

## Prompts utilizados

### Prompt inicial

Tenho uma planilha com colunas: ID, Data de abertura, Solicitante, Tipo, Prioridade, Status (Aberto / Em atendimento / Dev / Outro setor / Resolvido), Prazo, Devolutiva final (Sim/Não). Preciso de uma visão mensal com: total de chamados abertos, resolvidos, encaminhados ao dev, pendentes, fora do prazo e os tipos mais frequentes. Como eu organizaria isso no Excel/Google Sheets com fórmulas e um gráfico simples?

### Prompt de refinamento

Me dê as fórmulas COUNTIF para contar chamados com status "Resolvido", "Dev" e os que estão com prazo anterior à data de hoje e ainda não resolvidos.

### Prompt de visualização

Como eu criaria um gráfico de barras no Excel mostrando a quantidade de chamados por tipo de demanda?

## Resultado esperado

- Dashboard mensal em uma nova aba da planilha;
- Indicadores de total de chamados;
- Quantidade de chamados resolvidos;
- Quantidade de chamados pendentes;
- Chamados encaminhados ao desenvolvimento;
- Chamados fora do prazo;
- Gráfico de barras com os tipos de demanda mais frequentes;
- Destaque visual para chamados vencidos.

## Como validaria os resultados

Conferência manual utilizando uma amostra de chamados para comparar os valores gerados pelas fórmulas com os registros reais da planilha.

Caso os números coincidam, os resultados podem ser considerados válidos.

## Ajustes manuais realizados

- Adequação das fórmulas;
- Ajuste dos períodos analisados para o mês atual;
- Organização dos gráficos e indicadores.

## Dados que não seriam enviados à IA

- Nome completo dos solicitantes;
- Telefones;
- Endereços de e-mail;
- Qualquer outro dado pessoal desnecessário.

## Apresentação para a equipe

A apresentação seria realizada em uma reunião interna utilizando o próprio dashboard no Google Sheets.
Explicando:
- O significado de cada indicador;
- Como atualizar os dados;
- Como interpretar os gráficos;
- Como manter o painel atualizado mensalmente.

# Questão 5 — Visão de BI

## Estrutura da Base de Dados

| Campo | Tipo | Descrição |
| id_chamado | Inteiro | Identificador único |
| data_abertura | Data | Data de abertura do chamado |
| solicitante | Texto | Nome do usuário |
| canal | Texto | Canal de entrada |
| tipo_demanda | Texto | Tipo da solicitação |
| prioridade | Texto | Prioridade da demanda |
| status | Texto | Situação atual do chamado |
| destino | Texto | Setor responsável |
| prazo | Data | Prazo informado pelo usuário |
| data_resolucao | Data | Data de encerramento |
| devolutiva_final | Booleano | Sim ou Não |
| primeiro_retorno | Booleano | Sim ou Não |

## Indicadores para acompanhamento

- Total de chamados no mês;
- Chamados resolvidos;
- Chamados pendentes;
- Chamados encaminhados ao desenvolvimento;
- Chamados fora do prazo;
- Tempo médio de resolução;
- Percentual de chamados com devolutiva final enviada;
- Tipos de demanda mais frequentes.

## Filtros disponíveis

- Período;
- Status;
- Prioridade;
- Tipo de demanda;
- Setor responsável.

## Estrutura do Painel

### Indicadores principais

- Total de chamados;
- Resolvidos;
- Pendentes;
- Encaminhados ao desenvolvimento;
- Fora do prazo.

### Gráficos

- Gráfico de barras por tipo de demanda;
- Gráfico de pizza por status;
- Gráfico de linha mostrando a evolução das aberturas ao longo do período.

### Tabela de acompanhamento

Tabela contendo os chamados fora do prazo com:

- Solicitante;
- Tipo;
- Prioridade;
- Prazo.

## Destaque de pendências e atrasos

Para facilitar a identificação de problemas:

- Cartão de chamados fora do prazo em vermelho;
- Linhas destacadas em vermelho para chamados vencidos;
- Ícones de alerta para registros atrasados.


## Validação dos indicadores

Os resultados seriam conferidos comparando os valores exibidos nos gráficos e indicadores com consultas e filtros realizados diretamente na base de dados.

## Apoio à tomada de decisão

O painel auxiliaria a gestão a identificar:

- Demandas recorrentes que necessitam treinamento ou documentação;
- Possíveis falhas sistêmicas quando houver muitos chamados encaminhados ao desenvolvimento;
- Sobrecarga da equipe através do aumento do tempo médio de resolução;
- Problemas de SLA através do crescimento de chamados fora do prazo.


## Consulta SQL

### Total de chamados pendentes

```sql
SELECT COUNT(*) AS total_pendentes
FROM chamados
WHERE status <> 'Resolvido';
```

### Pendências agrupadas por tipo de demanda

```sql
SELECT tipo_demanda,
       COUNT(*) AS total_pendentes
FROM chamados
WHERE status <> 'Resolvido'
GROUP BY tipo_demanda
ORDER BY total_pendentes DESC;
```
