# Análise de Resultado Final do Concurso para TI - Banco do Brasil ![image](https://github.com/user-attachments/assets/d09a88c5-9bef-4d07-bd5f-be7d16941717)


Este é um simples projeto em Python que visa analisar o resultado final do concurso para a área de Tecnologia da Informação (TI) do Banco do Brasil. O objetivo do projeto é transformar os dados do concurso em uma tabela ordenada pela pontuação dos candidatos, permitindo uma visualização clara e rápida dos resultados.

## Objetivo

O foco do projeto é:
- Organizar os dados extraídos do PDF do resultado do concurso.
- Classificar os candidatos com base na pontuação.
- Visualizar os dados de forma tabular e ordenada.

## Decisão de Implementação

Para simplificar o processo, optei por copiar diretamente os dados do PDF do resultado e colá-los na função, sem a necessidade de uma leitura automática do arquivo PDF. Embora existam maneiras mais sofisticadas de fazer isso (como ler diretamente de um arquivo PDF usando bibliotecas como `pdfplumber` ou `PyPDF2`), o foco aqui é manter o projeto simples e fácil de executar.

## Executando no Google Colab

Se preferir rodar este projeto no Google Colab, siga os passos abaixo:

1. **Acessar o Google Colab**
   - Vá para o [Google Colab](https://colab.research.google.com/#create=true). Isso abrirá um novo notebook com um espaço pronto para você digitar os códigos.

2. **Adicionar e rodar o código no Colab**
   - Cole o código Python no notebook. Certifique-se de que o código da função `resultado_final()` está correto. O Colab já tem o Python e a biblioteca `pandas` instalada, então você pode pular a instalação.

3. **Inserir os dados do PDF**
   - Copie os dados do PDF e insira-os no formato de string dentro da função, como no exemplo:
     ```python
     resultado_final("""Aarao Aata Leal Guimaraes; 571190589-7; 74,5; 905 ; - ; - /Abel Barbosa Neto Souto; 571022340-0; 75,0; 850 ; - ; -
     /Abimael de Queiroz Lima; 570068440-7; 66,0; 3367 ; - ; 241 /Abner Filipe Cunha Ribeiro; 572090305-5; 72,5; 1279 ; - ; -
     /Abner Silveira de Freitas; 571925980-4; 73,5; 1055 ; - ; - /Abraao Freitas Medeiros; 571460406-8; 76,0; 679 ; - ; - /Aciria
     Borges Alves Rufino; 570525714-0; 73,0; 1177 ; - ; - /Adalberto Luis Navarrete Filho; 570925900-3; 88,0; 15 ; - ; - /Adam
     Basilio; 570498450-4; 74,5; 947 ; - ; -""")
     ```

4. **Executar o notebook**
   - Clique no botão de "play" à esquerda da célula para executar o código. O resultado será exibido diretamente no notebook como uma tabela interativa.

## Estrutura do Projeto

- **função `resultado_final`:** Organiza os dados em um DataFrame, classifica os candidatos por pontuação e exibe a tabela final.

## Contribuições

Este é um projeto simples e direto, mas caso deseje melhorar ou adicionar novas funcionalidades, sinta-se à vontade para comentar!
