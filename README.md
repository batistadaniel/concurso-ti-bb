# Análise de Resultado Final do Concurso para TI - Banco do Brasil ![image](https://uploaddeimagens.com.br/images/004/837/687/full/bb-logo-2.png?1725158260)


Este é um simples projeto em Python que visa analisar o resultado final do concurso para a área de Tecnologia da Informação (TI) do Banco do Brasil. O objetivo do projeto é transformar os dados do concurso em uma tabela ordenada pela pontuação dos candidatos, permitindo uma visualização clara e rápida dos resultados.

## Objetivo

O foco do projeto é:
- Organizar os dados extraídos do PDF do resultado do concurso.
- Classificar os candidatos com base na pontuação.
- Filtrar as últimas pessoas classificadas em ampla concorrência e nas cotas PCD e PPP.

## Decisão de Implementação

Para simplificar o processo, optei por copiar diretamente os dados do PDF do resultado e colá-los na função, sem a necessidade de uma leitura automática do arquivo PDF. Embora existam maneiras mais sofisticadas de fazer isso (como ler diretamente de um arquivo PDF usando bibliotecas como `pdfplumber` ou `PyPDF2`), o foco aqui é manter o projeto simples e fácil de executar.

## Executando no Google Colab

Se preferir rodar este projeto no Google Colab, siga os passos abaixo:

1. **Acessar o Google Colab**
   - Vá para o [Google Colab](https://colab.research.google.com/#create=true). Isso abrirá um novo notebook com um espaço pronto para você digitar os códigos.

2. **Adicionar e rodar o código no Colab**
   - Cole o código Python no notebook. 

3. **Inserir os dados do PDF**
   - Copie os dados do PDF e insira-os na variavél 'dados', como no exemplo:
     ```python
     dados = """Aarao Aata Leal Guimaraes; 571190589-7; 74,5; 905 ; - ; - /Abel Barbosa Neto Souto; 571022340-0; 75,0; 850 ; - ; -
     /Abimael de Queiroz Lima; 570068440-7; 66,0; 3367 ; - ; 241 /Abner Filipe Cunha Ribeiro; 572090305-5; 72,5; 1279 ; - ; -
     /Abner Silveira de Freitas; 571925980-4; 73,5; 1055 ; - ; - /Abraao Freitas Medeiros; 571460406-8; 76,0; 679 ; - ; - /Aciria
     Borges Alves Rufino; 570525714-0; 73,0; 1177 ; - ; - /Adalberto Luis Navarrete Filho; 570925900-3; 88,0; 15 ; - ; - /Adam
     Basilio; 570498450-4; 74,5; 947 ; - ; -"""
     ```
3.1 Use ```resultado = ResultadoFinal(dados)``` para instanciar a classe.

3.2 Use ```resultado.resultado_final()``` para exibir o resultado final completo.

3.3 Use ```resultado.ultima_pessoa_sem_cota()``` para exibir informacoes sobre o corte para ampla concorrencia.

3.4 Use ```resultado.ultima_pessoa_cota_pcd()``` para exibir informacoes sobre o corte para vagas pcd.

3.5 Use ```resultado.ultima_pessoa_cota_ppp()``` para exibir informacoes sobre o corte para vagas ppp.

4. **Executar o notebook**
   - Clique no botão de "play" à esquerda da célula para executar o código. O resultado será exibido diretamente no notebook como uma tabela interativa.


## Resumo Classificados - 2022

| Categoria | Primeiro | Corte |
|-----------|----------|-------|
| Ampla     | 98,5     | 71    |
| PCD       | 81       | 51    |
| PPP       | 88       | 51,5  |


## Resumo Cadastro Reserva - 2022

| Categoria | Corte |
|-----------|-------|
| Ampla     | 68    |
| PCD       | *     |
| PPP       | 57    |

*\*Todos foram chamados na primeira convocação*

## Resumo Classificados - 2021

| Categoria | Primeiro | Corte |
|-----------|----------|-------|
| Ampla     | 88       | 67,5  |
| PCD       | 83,5     | 60,5  |
| PPP       | 78       | 52,5  |

## Resumo Cadastro Reserva - 2021

| Categoria | Corte |
|-----------|-------|
| Ampla     | 59,5  |
| PCD       | *     |
| PPP       | *     |

*\*Todos foram chamados na primeira convocação*


## Contribuições

Este é um projeto simples e direto, mas caso deseje melhorar ou adicionar novas funcionalidades, sinta-se à vontade para comentar!
