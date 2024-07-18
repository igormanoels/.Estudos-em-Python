import os
os.system('cls')

class Filelterator:
    def __init__ (self, filename):
        self.file = open(filename)
    
    def __iter__(self):
        return self
    
    def __next__ (self):
        line = self.file.readtine()
        if line != "":
            return line
        else:
            self.file.close()
            raise StopIteration # Finaliza o laço de repetição

for line in Filelterator('c:\\temp\\NomeDoArquivo.txt'):
    print (line)