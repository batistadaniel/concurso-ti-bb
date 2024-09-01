# Importando a biblioteca
import pandas as pd

def resultado_final(dados):

    # Separa cada linha de informacoes por (/).
    # Substitui quebras de linha por espaco e separa por (;).
    # Armazena em uma lista.
    colunas = [linha.replace("\n", " ").split(";") for linha in dados.split('/')]

    # Cria o DataFrame com as colunas definidas.
    df = pd.DataFrame(colunas, columns=['Nome', 'Inscricao', 'Pontuacao', 'Classificacao Micro-Macrorregiao', 'PCD', 'PPP'])

    # Ordena o DataFrame pela coluna Pontuacao em ordem decrescente para classificacao ficar crescente, porem como existem notas repitidas tive que reordenar no google sheets novamente.
    df = df.sort_values(by='Pontuacao', ascending=False)

    # Define a coluna Nome como indice do DataFrame.
    csv = df.set_index('Nome')

    # Exibe o DataFrame.
    display(csv)


resultado_final(dados)    
