import random

matriz = [ ]

linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))                  #tentativa de fazer uma matriz secundaria para calcular quantos blocos precisa para fechar o principal
area_matriz = linhas * colunas #não vou fazer matriz so pega os tamanhos
for l in range(linhas):
    i = []
    for c in range(colunas):
        i.append(0)
    matriz.append(i)

def print_matriz(matriz_desejada):
    for z in(matriz_desejada):
        print(z)    

r = 0
am = 1 
num_ran = 1
num_bloco = 0

while(r != am ): #enquanto tiver espaço sem bloco na matriz r() sera diferente de am(0) 
    for h in matriz: #loop de validação a cada bloco que será criado
        teste = 0 not in h  #verifica se ainda tem algum espaço na matriz sem bloco
        if teste == False: #significa que ainda tem 0  
             #começa a criação de blocos 
            altura = int(input("insira a largura do bloco:"))
            largura = int(input("insira a altura do bloco:")) 
            #bloco foi criado
            blocos = []
            blocos.append({'nº bloco': (num_bloco + 1), 'altura bloco': altura, 'largura bloco': largura})#entender este erro
            bloco = blocos[num_bloco]
            num_bloco += 1    
            print("bloco numero: {} ".format(bloco['nº bloco']))
            #lista blocos criadas, e os objetos blocos sendo instanciados, a cada loop por meio de um dicionario, em cada indice da lista adcionado
            if bloco['nº bloco'] == 1:# se for o primeiro bloco, a posição será aleatória
                l_p = linhas - altura
                c_p = colunas - largura
                l_i = random.randrange(0,(l_p + 1))
                c_i = random.randrange(0,(c_p + 1))
                for d in range(altura):

                    for f in range(largura):
                        f = c_i
                        matriz[l_i][c_i] = num_ran
                        c_i += 1
                    l_i += 1
                    c_i = c_i - largura
                print_matriz(matriz)
                num_ran += 1        
            else:        
                for x in range(altura): # inseri o x que seria relacionado ao primeiro bloco                 
                    for y in range(largura): 
                        matriz[x][y] = num_ran           
                num_ran = num_ran + 1
                print_matriz(matriz)                
        else:
            am = 0 #significa que não há mais espaço na matriz
            
