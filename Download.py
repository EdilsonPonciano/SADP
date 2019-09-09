from Src import Config
import requests, zipfile, io

class Download:
    bcolors = Config.bcolors
    url = Config.baseDownloadURL
    def __init__(self, version):
        try:
            link = requests.get("{0}{1}{2}".format(self.url,version,".zip"))
            z = zipfile.ZipFile(io.BytesIO(link.content))
            z.extractall("Downloads")#Extrai para pastar Downloads
            print('\n{0}Edicao {2} baixada e extraida com sucesso!{1}'.format(self.bcolors.BLUE, self.bcolors.CLEAR, version))
        except Exception as e:
            print('\n{0}Error, Edicao invalida ou link quebrado!{1}'.format(self.bcolors.RED, self.bcolors.CLEAR,version))