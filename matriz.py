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
    for d in range(altura):
        for z in range(largura):    
            matriz[d][z] = 'x'


for x in matriz:
    print(x)    
                     

                    