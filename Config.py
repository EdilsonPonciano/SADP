import os
#import mysql.connector

baseURL = 'http://revistas.inpi.gov.br/rpi/'
baseDownloadURL ='http://revistas.inpi.gov.br/txt/P'
PCP = '(21)' #Padrao de Classificacao de Patente
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="mydatabase"
# )
class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CLEAR = '\033[0m'

def LastsVersions():
    versionsName = []
    for fileModule in os.listdir("./Downloads/"):
        if fileModule.endswith(".txt"):
            versionsName.append(fileModule[1:5])
    with open('./Config/VersionsDownloaded.txt', 'w') as f:
        try:
            for item in versionsName:
                f.write("%s\n" % item)
        except:
            f.write(str(0))
    with open('./Config/LastVersionsDownloaded.txt', 'w') as f:
            try:
                f.write(versionsName[-1])
            except:
                f.write(str(0))

def getLastVersionsDownloaded():
    try:
        version_file = open("./Config/LastVersionsDownloaded.txt", "r")
        file = version_file.read().split("\n")
        version_file.close()
        try:
            return int(file[0])
        except:
            return 0

    except KeyError:
        return 0

def getLastVersion():
    try:
        version_file = open("./Config/LastVersion.txt", "r")
        file = version_file.read().split("\n")
        version_file.close()
        try:
            return int(file[0])
        except:
            return 0

    except KeyError:
        return 0

def VersionsDownloaded():
    try:
        version_file = open("./Config/VersionsDownloaded.txt", "r")
        file = version_file.read().split("\n")
        version_file.close()
        try:
            return file
        except:
            return 0

    except KeyError:
        return 0
