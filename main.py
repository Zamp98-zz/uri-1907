# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class grafo:
    def __init__(self, v, cor):
        self.cor = cor
        self.vizinhos = v
    def getVizinhos(self):
        return self.vizinhos
    def getCor(self):
        

def constroi(matriz, linha, coluna):
    cor = 1 #primeira cor
    for a in range(linha):
        print(a)
        for b in range(coluna-1):
            if a < 1: #se é a primeira linha
               pass
            elif a == linha - 1:
                pass
            else:
                pass
            if b < 1:
                pass
            elif b == coluna-1:
                pass
            else:
                pass

def main():
    linha, coluna = input().split()
    linha = int(linha)
    coluna = int(coluna)
    m=[]
    matrizN=[]
    for l in range(int(linha)):
        lMatrizN=[]
        for char in input():
            if char == '.':
                lMatrizN.append(0)
            else:
                lMatrizN.append(-1)
        matrizN.append(lMatrizN)
    print(matrizN)
    print(linha, coluna)
    constroi(matrizN, linha, coluna)
main()
