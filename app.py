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


resultado_final("""Aarao Aata Leal Guimaraes; 571190589-7; 74,5; 905 ; - ; - /Abel Barbosa Neto Souto; 571022340-0; 75,0; 850 ; - ; -
/Abimael de Queiroz Lima; 570068440-7; 66,0; 3367 ; - ; 241 /Abner Filipe Cunha Ribeiro; 572090305-5; 72,5; 1279 ; - ; -
/Abner Silveira de Freitas; 571925980-4; 73,5; 1055 ; - ; - /Abraao Freitas Medeiros; 571460406-8; 76,0; 679 ; - ; - /Aciria
Borges Alves Rufino; 570525714-0; 73,0; 1177 ; - ; - /Adalberto Luis Navarrete Filho; 570925900-3; 88,0; 15 ; - ; - /Adam
Basilio; 570498450-4; 74,5; 947 ; - ; -""")
