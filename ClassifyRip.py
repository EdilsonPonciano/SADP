from Src import Config
import time
import pandas as pd

class Classify:
    bcolors = Config.bcolors

    def __init__(self):
        self.version = int(
            input("\n{0}Digite a edicao desejada (ex: 2525): {1}".format(self.bcolors.BLUE, self.bcolors.CLEAR)))

        text_file = open("./Downloads/P{0}.txt".format(self.version), "r", encoding="utf8")
        file = text_file.read().split("\n")

        df = pd.read_csv("./Template/ClassifyTemplate.csv")
        # df2 = pd.read_csv("./Template/ALLRIPS.csv")

        print("\n{0}Classificando, aguarde! isso pode levar um tempo... {1}".format(self.bcolors.BLUE, self.bcolors.CLEAR))
        for count in range(file.__len__()):

            linha = file[count]

            if '(Cd)' in linha:
                if'(Cd)' in file[count + 1]:
                    break
                if file.__len__() - count > 12:
                    i = 12
                else:
                    i = file.__len__() - count

                for lineMore1 in range(i):
                    if file[count + lineMore1][1:3] == 'co':
                        column = "(Co) Comentario"
                    elif file[count + lineMore1][1:3] == '11':
                        column = "(11) Número da Patente"
                    elif file[count + lineMore1][1:3] == '21':
                        column = "(21) Número do Pedido"
                    elif file[count + lineMore1][1:3] == '22':
                        column = "(22) Data do Depósito"
                    elif file[count + lineMore1][1:3] == '30':
                        column = "(30) Dados da Prioridade Unionista"
                    elif file[count + lineMore1][1:3] == '31':
                        column = "(31) Data Prioridade"
                    elif file[count + lineMore1][1:3] == '32':
                        column = "(32) Numero Prioridade"
                    elif file[count + lineMore1][1:3] == '33':
                        column = "(33) Sigla Pais"
                    elif file[count + lineMore1][1:3] == "43":
                        column = "(43) Data da Publicação do Pedido"
                    elif file[count + lineMore1][1:3] == '45':
                        column = "(45) Data da Concessão da Patente"
                    elif file[count + lineMore1][1:3] == '51':
                        column = "(51) Classificação Internacional"
                    elif file[count + lineMore1][1:3] == "52":
                        column = "(52)  Classificação Nacional"
                    elif file[count + lineMore1][1:3] == '54':
                        column = "(54) Título"
                    elif file[count + lineMore1][1:3] == "57":
                        column = "(57) Resumo"
                    elif file[count + lineMore1][1:3] == "61":
                        column = "(61) Dados do Pedido"
                    elif file[count + lineMore1][1:3] == "62":
                        column = "(62) Dados do pedido original do qual o presente é uma divisão"
                    elif file[count + lineMore1][1:3] == '66':
                        column = "(66) Prioridade Interna"
                    elif file[count + lineMore1][1:3] == '71':
                        column = "(71) Nome do Depositante"
                    elif file[count + lineMore1][1:3] == '72':
                        column = "(72) Nome do Inventor"
                    elif file[count + lineMore1][1:3] == '73':
                        column = "(73) Nome do Titular"
                    elif file[count + lineMore1][1:3] == '74':
                        column = "(74) Nome do Procurador"
                    elif file[count + lineMore1][1:3] == "81":
                        column = "(81) Países Designados"
                    elif file[count + lineMore1][1:3] == '85':
                        column = "(85) Data do Início da Fase Nacional"
                    elif file[count + lineMore1][1:3] == '86':
                        column = "(86) Número, Idioma e Data do Depósito Internacional"
                    elif file[count + lineMore1][1:3] == '87':
                        column = "(87) Número, Idioma e Data da Publicação Internacional"
                    elif file[count + lineMore1][1:3] == "99":
                        column = "(99) Comentário"
                    else:
                        column = file[count + lineMore1][1:3]
                    df.loc[count, '(Ed) Ediçao'] = "{0:.{1}f}".format(self.version, 1)
                    # df2.loc[count, '(Ed) Ediçao'] = "{0:.{1}f}".format(self.version, 1)
                    df.loc[count, column] = file[count + lineMore1][4:file[count + lineMore1].__len__()+1]
                    # df2.loc[count, column] = file[count + lineMore1][4:file[count + lineMore1].__len__() + 1]

                df.to_csv("./Outputs/P{0}.csv".format(self.version))
                # df2.to_csv("./Template/ALLRIPS.csv")
                # df2.to_csv("./Template/AllRip.csv")
                print("{0}{1} - {2}{3}".format(self.bcolors.GREEN, linha, time.asctime(), self.bcolors.CLEAR))

        print("\n{0}Classificacao Concluida! {1}".format(self.bcolors.GREEN, self.bcolors.CLEAR))
        print("\n{0}Salvo ./Outputs/P{1}.csv {2}".format(self.bcolors.GREEN, self.version, self.bcolors.CLEAR))
        print("\n{0}Salvo./Template/AllRip.csv {1}".format(self.bcolors.GREEN, self.bcolors.CLEAR))
