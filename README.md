# Questão 1 — Atendimento de suporte técnico e triagem de demanda

## 1. Perguntas realizadas ao usuário
Para iniciar o diagnóstico, eu faria as seguintes perguntas:

- Qual mensagem de erro aparece exatamente? (Solicitando print ou foto da tela);
- Esse problema começou hoje ou já vinha ocorrendo anteriormente?
- O acesso está sendo feito por navegador ou aplicativo?
- Caso seja navegador, qual está sendo utilizado?
- Já tentou acessar utilizando outro navegador ou dispositivo?
- O erro ocorre em todas as tentativas ou apenas em determinados momentos?
- Houve alguma alteração recente, como troca de senha, mudança de e-mail ou utilização de um novo computador?

## 2. Evidências solicitadas
- Print ou foto da mensagem de erro;
- E-mail utilizado para acesso ao sistema;
- Horário exato em que a tentativa de login foi realizada.

## 3. Verificações realizadas antes de escalar a demanda
- Confirmar se o sistema está disponível e funcionando normalmente;
- Verificar se outros usuários estão enfrentando o mesmo problema;
- Conferir se o e-mail informado está cadastrado corretamente;
- Verificar se a conta foi bloqueada por excesso de tentativas de login;
- Solicitar limpeza de cache e cookies do navegador;
- Testar o acesso em modo anônimo ou em outro navegador;
- Verificar se existe alguma manutenção programada ou indisponibilidade conhecida.

## 4. Classificação da prioridade
Considerando que o usuário informou possuir uma entrega interna com prazo para o mesmo dia, classificaria o chamado da seguinte forma:

| Critério | Classificação |
|-----------|--------------|
| Impacto | Médio-Alto |
| Urgência | Alta |
| Prioridade Final | Alta (P1 - Urgente) |

## 5. Registro da demanda
O chamado seria registrado em planilha ou sistema de controle contendo:

| Campo | Informação |
|---------|------------|
| ID | Gerado automaticamente |
| Data/Hora de abertura | Data e horário do contato |
| Solicitante | Nome e contato do usuário |
| Canal de entrada | E-mail, WhatsApp ou telefone |
| Descrição | Erro ao realizar login no sistema |
| Evidências | Prints e informações anexadas |
| Prioridade | Alta |
| Status | Em atendimento |
| Responsável | Analista de suporte |
| Primeiro retorno | Data e horário do primeiro contato |
| Devolutiva final | Preenchido ao final do atendimento |
| Data de encerramento | Após validação do usuário |

## 6. Situações em que resolveria diretamente
O chamado poderia ser solucionado pelo próprio suporte quando:

- O problema fosse causado por cache ou navegador;
- Houvesse erro de digitação no e-mail ou senha;
- A conta estivesse bloqueada e o suporte possuísse permissão para desbloqueio;
- O sistema apresentasse uma instabilidade temporária já identificada.

## 7. Situações em que encaminharia ao desenvolvedor
O chamado seria escalado para a equipe de desenvolvimento quando:

- Houvesse erro interno da aplicação (erro 500, exceções ou falhas técnicas);
- O problema fosse identificado como um bug do sistema;
- A autenticação falhasse mesmo após todas as verificações realizadas;
- O erro afetasse múltiplos usuários.

## 8. Situações em que encaminharia para outros setores
### Administrativo ou Comercial
- Bloqueio de acesso por questões contratuais.

### Financeiro

- Pendências financeiras que impeçam o acesso ao sistema.

### Implantação

- Usuário sem configuração inicial ou sem permissões cadastradas.

### Atendimento

- Solicitações relacionadas a cadastro ou informações de perfil gerenciadas por outro setor.

## 9. Informações enviadas ao desenvolvedor
Caso fosse necessário escalar a demanda, enviaria:

- Descrição detalhada do problema;
- Print ou evidência do erro;
- E-mail do usuário afetado;
- Data e horário das tentativas de acesso;
- Navegador e dispositivo utilizados;
- Testes já realizados pelo suporte;
- Resultado das verificações efetuadas;
- Prioridade do chamado e prazo informado pelo usuário.

## 10. Garantia de encerramento somente após devolutiva final

- Confirmação do usuário de que o acesso foi restabelecido; ou
- Registro formal da solução aplicada e comunicação ao solicitante.

Além disso, o campo Devolutiva Final permaneceria obrigatório. O status Encerrado só poderia ser selecionado após o preenchimento desse campo, garantindo que nenhuma demanda fosse finalizada sem retorno ao usuário.


## Questão 2

O código-fonte da solução encontra-se em:

/questao2/index.html

# Questão 3 — Lógica de Programação e Integração (API)
## Tecnologias utilizadas

- Python 3
- urllib.request
- json

## Estratégia da solução
1. Consumir a lista de usuários.
2. Consumir a lista de tarefas.
3. Filtrar apenas as tarefas pendentes.
4. Contabilizar a quantidade de tarefas pendentes por usuário.
5. Identificar o usuário com maior quantidade de tarefas pendentes.
6. Exibir o nome do usuário e a quantidade de tarefas pendentes.

## Uso de Inteligência Artificial

| Item | Detalhe |
|--------|----------|
| Ferramenta | Claude |
| Finalidade | Auxiliar na estruturação da lógica de cruzamento de dados |
| Prompts fornecidos | Estutura iniciada por mim e correção de erros |
| Ajustes manuais | Utilização de `urllib.request` em vez de bibliotecas externas para evitar dependências adicionais |
| Validação | Revisão da lógica, conferência da contagem de tarefas e verificação do uso da função `max()` |
| Privacidade | Nenhum dado sensível foi compartilhado. Foram utilizadas apenas URLs públicas da API JSONPlaceholder |

## Resultado esperado
O script imprime:

```text
Usuário mais sobrecarregado: Nome do usuário
Tarefas pendentes: Quantidade
```
