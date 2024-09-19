# Importando a biblioteca
import pandas as pd

# Classe e suas funcoes
class ResultadoFinal:
    def __init__(self, dados):
        self.dados = dados
        self.df = None  

    def resultado_final(self):
        
        # Separa cada linha de informacoes por (/).
        # Substitui quebras de linha por espaco e separa por (;).
        # Armazena em uma lista.        
        colunas = [linha.replace("\n", " ").split(";") for linha in self.dados.split('/')]

        # Cria o DataFrame
        self.df = pd.DataFrame(colunas, columns=['Nome', 'Inscricao', 'Pontuacao', 'Classificacao Micro-Macrorregiao', 'PCD', 'PPP']).set_index('Nome')

        # Convertendo a classificacao geral para numérico
        self.df['Classificacao Micro-Macrorregiao'] = pd.to_numeric(self.df['Classificacao Micro-Macrorregiao'], errors='coerce')

        # Ordenando de forma crescente a coluna 'Classificacao Micro-Macrorregiao'
        self.df = self.df.sort_values(by='Classificacao Micro-Macrorregiao', ascending=True)

        # Exibe o DataFrame
        display(self.df)

    def ultima_pessoa_sem_cota(self):
        if self.df is not None:  # Verifica se df foi gerado
            # Filtra a última linha onde 'PCD' e 'PPP' são iguais a " - "
            filtro = self.df[(self.df['PCD'] == " - ") & (self.df['PPP'] == " - ")].tail(1)

            # Exibe o DataFrame filtrado
            display(filtro)
        else:
            print("DataFrame não gerado. Execute o método resultado_final primeiro.")

    def ultima_pessoa_cota_pcd(self):
        if self.df is not None:  # Verifica se df foi gerado
            # Converte a coluna 'PCD' para numérico, onde valores inválidos se tornam NaN
            self.df['PCD'] = pd.to_numeric(self.df['PCD'], errors='coerce')

            # Filtra a última pessoa onde 'PCD' tem um valor numérico 
            filtro = self.df[self.df['PCD'].notna()].tail(1)

            # Exibe o DataFrame filtrado
            display(filtro)
        else:
            print("DataFrame não gerado. Execute o método resultado_final primeiro.")


    def ultima_pessoa_cota_ppp(self):
        if self.df is not None:  # Verifica se df foi gerado
            # Converte a coluna 'PPP' para numérico, onde valores inválidos se tornam NaN
            self.df['PPP'] = pd.to_numeric(self.df['PPP'], errors='coerce')

            # Filtra a última pessoa onde 'PPP' tem um valor numérico 
            filtro = self.df[self.df['PPP'].notna()].tail(1)
            # Exibie o DataFrame filtrado
            display(filtro)
        else:
            print("DataFrame não gerado. Execute o método resultado_final primeiro.")




# Atribui os dados a uma variavel
dados = """Aarao Aata Leal Guimaraes; 571190589-7; 74,5; 905 ; - ; - /Abel Barbosa Neto Souto; 571022340-0; 75,0; 850 ; - ; -
/Abimael de Queiroz Lima; 570068440-7; 66,0; 3367 ; - ; 241 /Abner Filipe Cunha Ribeiro; 572090305-5; 72,5; 1279 ; - ; -
/Abner Silveira de Freitas; 571925980-4; 73,5; 1055 ; - ; - /Abraao Freitas Medeiros; 571460406-8; 76,0; 679 ; - ; - /Aciria
Borges Alves Rufino; 570525714-0; 73,0; 1177 ; - ; - /Adalberto Luis Navarrete Filho; 570925900-3; 88,0; 15 ; - ; - /Adam
Basilio; 570498450-4; 74,5; 947 ; - ; -"""


# Instancia a classe
resultado = ResultadoFinal(dados)


# Funcao que exibe o resultado final completo
resultado.resultado_final()


# Funcao que exibe informacoes sobre o corte para ampla concorrencia
resultado.ultima_pessoa_sem_cota()


# Funcao que exibe informacoes sobre o corte para vagas pcd
resultado.ultima_pessoa_cota_pcd()


# Funcao que exibe informacoes sobre o corte para vagas ppp
resultado.ultima_pessoa_cota_ppp()
