import numpy #ainda não usei mas há possibilidade.

matriz = [ ]

linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))
area_matriz = linhas * colunas
for l in range(linhas):
        i = []
        for c in range(colunas):
            i.append('0')
        matriz.append(i)

largura = int(input("insira a altura do bloco:"))
altura = int(input("insira a largura do bloco:"))        

for x in range(altura): # inseri o x que seria relacionado ao primeiro bloco
    for y in range(largura):
        matriz[x][y] = 'x'
    
for x in(matriz):
    print(x)



                     

                    