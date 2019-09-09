from Src import Config, Scraping, Download, SearchPatentSorter, ClassifyRip


class Main:
        bcolors = Config.bcolors
        Config.LastsVersions()
        while True:
            try:
                Rip = int(input("{0}"
                            "\nUltima Edicao Baixada: {1}"
                            "\nEdicao Mais Rescente Encontrada: {2}\n"
                            "\n\n[][][][] DONWLOADS [][][][]"
                            "\n1 - Proucurar Novas Edicoes"
                            "\n2 - Baixar Edicao Especifica"
                            "\n3 - Baixar Intervalo de Versões"
                            "\n4 - Lista de Edicoes Ja Baixadas"
                            "\n\n[][][][] CLASSIFICACAO [][][]][]"
                            "\n5 - Buscar Numero do Pedido de Deposito"
                            "\n6 - Classificar Edicao de Revista"
                            "\n\n0 - Encerrar"
                            "\n==> {3}".format(bcolors.PINK, Config.getLastVersionsDownloaded(), Config.getLastVersion(),bcolors.CLEAR)))

            except:
                print('\n{0}Error, o valor digitado precisa ser um numero inteiro.{1}'.format(bcolors.RED, bcolors.CLEAR))

            if Rip == 1:
                    Scraping.Scraping()
            elif Rip == 2:
                    try:
                        version = int(input("{0}Digite a edicao desejada (ex: 2525): {1}".format(bcolors.BLUE, bcolors.CLEAR)))
                        Download.Download(version)
                    except:
                        print('\n{0}Error, a edicao desejada precisa ser um numero inteiro.{1}'.format(bcolors.RED, bcolors.CLEAR))
            elif Rip == 3:
                    try:
                        version1 = int(input("\n{0}Digite a MENOR edicao desejada (ex: 2520): {1}".format(bcolors.BLUE, bcolors.CLEAR)))
                        version2 = int(input("{0}Digite a MAIOR edicao desejada (ex: 2526): {1}".format(bcolors.BLUE, bcolors.CLEAR)))
                        for version in range(version1, version2+1):
                            Download.Download(version)
                    except:
                        print('\n{0}Error, a edicao desejada precisa ser um numero inteiro OU a Versao Menor e Maior que a Maior Versao.{1}'.format(bcolors.RED,bcolors.CLEAR))
            elif Rip == 4:
                    list = Config.VersionsDownloaded()
                    print("\n{0}{1}{2}".format(bcolors.YELLOW, list, bcolors.CLEAR))
            elif Rip == 5:
                    SearchPatentSorter.SearchPatentSorter()
            elif Rip == 6:
                ClassifyRip.Classify()
            elif Rip == 0:
                break
            else:
                break
