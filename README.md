# Análise de Resultado Final do Concurso para TI - Banco do Brasil

Este é um simples projeto em Python que visa analisar o resultado final do concurso para a área de Tecnologia da Informação (TI) do Banco do Brasil. O objetivo do projeto é transformar os dados do concurso em uma tabela ordenada pela pontuação dos candidatos, permitindo uma visualização clara e rápida dos resultados.

## Objetivo

O foco do projeto é:
- Organizar os dados extraídos do PDF do resultado do concurso.
- Classificar os candidatos com base na pontuação.
- Visualizar os dados de forma tabular e ordenada.

## Decisão de Implementação

Para simplificar o processo, optei por copiar diretamente os dados do PDF do resultado e colá-los na função, sem a necessidade de uma leitura automática do arquivo PDF. Embora existam maneiras mais sofisticadas de fazer isso (como ler diretamente de um arquivo PDF usando bibliotecas como `pdfplumber` ou `PyPDF2`), o foco aqui é manter o projeto simples e fácil de executar.

## Passo a Passo para Executar

1. **Instalar dependências**
   - Certifique-se de ter o Python instalado.
   - Instale a biblioteca `pandas`, que será utilizada para manipulação de dados. Você pode instalá-la com o comando:
     ```bash
     pip install pandas
     ```

2. **Copiar e colar os dados**
   - Extraia os dados do PDF do resultado final do concurso.
   - Copie os dados e cole-os diretamente dentro da função `resultado_final`, como uma string. Por exemplo:
     ```python
     dados = """
     Nome;Inscricao;Pontuacao;Classificacao Micro-Macrorregiao;PCD;PPP
     Fulano de Tal;123456;98;1;Sim;Nao
     Ciclano de Tal;654321;89;2;Nao;Sim
     """
     resultado_final(dados)
     ```

3. **Executar o script**
   - Basta rodar o script Python que contém a função `resultado_final()`. O resultado será exibido como uma tabela, mostrando a classificação dos candidatos de acordo com a pontuação.

## Estrutura do Projeto

- **função `resultado_final`:** Organiza os dados em um DataFrame, classifica os candidatos por pontuação e exibe a tabela final.

## Contribuições

Este é um projeto simples e direto, mas caso deseje melhorar ou adicionar novas funcionalidades, sinta-se à vontade para comentar!
