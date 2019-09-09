from Src import Config

class SearchPatentSorter:

    bcolors = Config.bcolors
    PCP = Config.PCP #Padrao de Classificacao de Patente
    listaCDP = []
    foundLines = 0
    foundCount = 0
    countLines = 0

    def __init__(self):
        self.version = int(input("\n{0}Digite a edicao desejada (ex: 2525): {1}".format(self.bcolors.BLUE, self.bcolors.CLEAR)))
        self.CCP = input(
            "{0}Digite o codigo de classificacao desejado (ex: a61k, a61b): {1}".format(self.bcolors.BLUE, self.bcolors.CLEAR))
        try:
            text_file = open("./Downloads/P{0}.txt".format(self.version), "r", encoding="utf8")# encoding="utf8"
        except:
            print('\n{0}Arquivo não encontrado, faca o download do arquivo e tente novamente. {1}'.format(self.bcolors.RED, self.bcolors.CLEAR))
            return
        file = text_file.read().split("\n")

        for lines in range(file.__len__()):
            if "(51)" in file[lines][0:5]:
                if self.CCP.upper() in file[lines]:
                    if (self.PCP in file[lines - 1]):
                        lineFounded = file[lines - 1]
                    elif (self.PCP in file[lines - 2]):
                        lineFounded = file[lines - 2]
                    elif (self.PCP in file[lines - 3]):
                        lineFounded = file[lines - 3]
                    elif (self.PCP in file[lines - 4]):
                        lineFounded = file[lines - 4]

                    self.listaCDP.append(lineFounded)
                    self.foundCount = self.foundCount + file[lines].count(self.CCP.upper())  # CONTAR TERMOS
                    self.foundLines += 1

        text_file.close()
        if (self.listaCDP.__len__() == 0):
            print('\n{0}Nenhum termo encontrado {1}'.format(self.bcolors.RED, self.bcolors.CLEAR))
            return
        else:
            print('\n{0}{1} Codigo de Classificacao em {2} Patentes {3}'.format(self.bcolors.GREEN, self.foundCount,self.foundLines,
                                                                       self.bcolors.CLEAR))
            with open('./Outputs/{0}_{1}.txt'.format(self.CCP, self.version), 'w') as f:
                for item in self.listaCDP:
                    f.write("%s\n" % item)
            print('\n{0} Salvo em /Outputs/{1}_{2}.txt{3}'.format(self.bcolors.GREEN,self.CCP, self.version, self.bcolors.CLEAR))