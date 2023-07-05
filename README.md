# Azure DevOps Metrics

Este projeto é uma ferramenta para coletar métricas de linhas de código em repositórios do Azure DevOps.

***

## Pré-requisitos

Antes de executar este projeto, você precisará ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Pacotes Python necessários: azure-devops e msrest.

Você também precisará ter um token de acesso pessoal (Personal Access Token) do Azure DevOps com permissões adequadas para acessar os repositórios desejados.

***

## Configuração

1. Clone este repositório em seu ambiente local:

```bash
$ git clone https://github.com/gersonborgesbatista/Azure-DevOps-Metrics.git
$ cd Azure-DevOps-Metrics
```
2. Instale os pacotes Python necessários:

```bash
pip install azure-devops msrest
```

3. Abra o arquivo `script.py` em um editor de texto e localize as seguintes linhas:

```bash
personal_access_token = 'SEU_TOKEN_DE_ACESSO_PESSOAL'
organization_url = 'https://dev.azure.com/sua-organizacao'
```

Substitua `'SEU_TOKEN_DE_ACESSO_PESSOAL'` pelo seu token de acesso pessoal do Azure DevOps e `'https://dev.azure.com/sua-organizacao'` pela URL da sua organização do Azure DevOps.

***

## Executando o Projeto

Para executar o projeto e coletar as métricas de linhas de código nos repositórios do Azure DevOps, execute o seguinte comando:

```bash
python3 script.py
```

Isso iniciará o script e coletará as métricas de linhas de código para os repositórios do Azure DevOps configurados. As métricas serão salvas em um arquivo CSV chamado `report_<timestamp>.csv`, onde `<timestamp>` é a data e hora da execução do script.

***

## Contatos

Para qualquer pergunta ou feedback, sinta-se à vontade para entrar em contato:

* E-mail: gerson.borges@live.com
* Linkedin: https://www.linkedin.com/in/gerson-borges/
