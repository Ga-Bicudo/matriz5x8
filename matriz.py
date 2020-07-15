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

blocks = []  #lista criada para guardar os blocos
area_blocos = 0
for blocos in range(0,area_matriz >= area_blocos): #metodo para checar se os blocos encaixaram na matriz.
    largura = int(input("insira a altura do bloco:"))
    altura = int(input("insira a largura do bloco:"))
    bloco = largura * altura   # criando objeto bloco
    blocks.append(bloco)      #adicionalndo na lista blocks o objeto
    if altura > linhas or largura > colunas:  #validando se o objeto pode ser guardado
        print("bloco inválido")
        continue
    else:
        for x in (blocks):
            print(x)
            
for x in matriz:
    print(x)    


                     

                    