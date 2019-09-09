import requests
import time
from bs4 import BeautifulSoup
from Src import Config, Download

class Scraping:

        bcolors = Config.bcolors
        time.sleep(1)
        LastV = Config.getLastVersionsDownloaded()

        try:
            print('{0}Iniciando Buscas...{1}'.format(bcolors.BLUE, bcolors.CLEAR))
            response = requests.get(Config.baseURL, timeout=5)  # GETTINGRESPONSE? 200:404

            if (response == 404):
                print('\n{0}Error 404 {1}'.format(bcolors.RED, bcolors.CLEAR))
            else:
                content = BeautifulSoup(response.content, "html.parser")
                name_list = content.find(class_='table table-text-center table-condensed table-bordered table-middle')
                links_list = name_list.find_all('a')
                found = 0
                for href in reversed(links_list):
                    if 'txt/P' in href.get('href'):
                        if 'txt/PC' in href.get('href'):
                            None
                        else:
                            try:
                                version = href.get('href')[-8:-4]
                                if int(version) > int(LastV):
                                    f = open("./Config/LastVersion.txt", "w")
                                    f.write(str(version))
                                    print('\n{0}Nova Edicao Encontrada: {2}. {1}'.format(bcolors.YELLOW, bcolors.CLEAR, version))
                                    f.close()
                                    Download.Download(version)
                                    found += 1
                            except:
                                 pass
                if found == 0:
                    print('{0}Nenhuma nova edicao encontrada...{1}'.format(bcolors.YELLOW,bcolors.CLEAR))
        except:
            print('\n{0}Error, o site nao responde...{1}'.format(bcolors.RED, bcolors.CLEAR))