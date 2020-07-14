import numpy 

matriz = [ ]
mataux = [ ]

linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))
for l in range(linhas):
        i = []
        for c in range(colunas):
            i.append('0')
        matriz.append(i)    


largura = int(input("insira a altura do bloco:"))
altura = int(input("insira a largura do bloco:"))
 
if altura > linhas or largura > colunas:
    print("bloco inválido")
else:
    for altura in(linhas):
        for largura in(colunas):    
            matriz[altura][largura] = 'x'
    for x in matriz:
        print(x)    
                     

                    