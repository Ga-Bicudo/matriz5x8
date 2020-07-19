import random

matriz = [ ]

linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))                 
area_matriz = linhas * colunas
for l in range(linhas):
    i = []
    for c in range(colunas):
        i.append(0)
    matriz.append(i)

def print_matriz(matriz_desejada):
    for z in(matriz_desejada):
        print(z)    

r = 0  #chave para o loop principal
am = 1 #chave para o loop principal, se for validado, ficara com valor de r, acabará a inserção de blocos e finaliza o programa
num_ran = 1 #numero que servirá de imagem na amtriz para os quadrados iseridos
num_bloco = 0 #identificação do bloco inserido que ssempre será igual o num_ram
blocos = [] #lista para armazenar os blocos
cord_x = [] #lista para armezenar os indices utilizados para a largura 
cord_y = [] #lista para armezenar os indices utilizados para a altura 
indices_usados_x = []
indices_usados_y = []

while(r != am ): #enquanto tiver espaço sem bloco na matriz r() sera diferente de am(0) 
    for h in matriz: #loop de validação a cada bloco que será criado
        teste = 0 not in h  #verifica se ainda tem algum espaço na matriz sem bloco
        if teste == False: #significa que ainda tem 0  
             #começa a criação de blocos 
            altura = int(input("insira a largura do bloco:"))
            largura = int(input("insira a altura do bloco:")) 
            #bloco foi criado
            blocos.append({'nº bloco': (num_bloco + 1), 'altura bloco': altura, 'largura bloco': largura})#entender este erro
            print('blocos usados: \n {}'.format(blocos))
            bloco = blocos[num_bloco]  
            print("bloco numero: {} ".format(bloco['nº bloco']))
            #lista blocos criadas, e os objetos blocos sendo instanciados, a cada loop por meio de um dicionario, em cada indice da lista adcionado
            if bloco['nº bloco'] == 1:# se for o primeiro bloco, a posição será aleatória
                l_p = linhas - altura
                c_p = colunas - largura
                l_i = random.randrange(0,(l_p + 1))
                c_i = random.randrange(0,(c_p + 1))
                for d in range(altura): #inserindo bloco na matriz
                    indices_usados_y.append(l_i)
                    y = l_i  
                    for f in range(largura):
                        indices_usados_x.append(c_i)
                        matriz[l_i][c_i] = num_ran
                        c_i += 1
                        x = c_i
                    l_i += 1
                    c_i = c_i - largura #fazendo com o que o c_i retorne ao local que ele iniciou no loop
                cord_y.append(y) #armazenando o local y que o leitor da matriz parou depois de inserir este bloco
                cord_x.append(x) #armazenando o local x que o leitor da matriz parou depois de inserir este bloco
                print_matriz(matriz) 
                print(x,y, "\n",c_i,l_i)       
            else:        
                diferença = linhas - l_i
                diferença_coluna = colunas - c_i
                if altura <= diferença or colunas <= diferença_coluna: #caso o cubo inserido possa ser encaixado na matriz de acordo com a posicão do x e y:
                    for d in range(altura):
                        indices_usados_y.append(y)
                        y = l_i 
                        for f in range(largura):
                            indices_usados_x.append(x)
                            matriz[l_i][c_i] = num_ran
                            c_i += 1
                            x = c_i
                        l_i += 1
                        c_i = c_i - largura #fazendo com o que o c_i retorne ao local que ele iniciou no loop
                    cord_y.append(y) #armazenando o local y que o leitor da matriz parou depois de inserir este bloco
                    cord_x.append(x) #armazenando o local x que o leitor da matriz parou depois de inserir este bloco
                    print_matriz(matriz)    
                else:#caso o cubo inserido não possa ser encaixado na matriz de acordo com a posicão do x e y:    
                    if altura > diferença or if colunas > diferença_coluna : 
                        c_i = 0   #recomeçando a leitura da matriz para achar um lugar onde possa por o cubo sem sobrepor os outros
                        l_i = 0
            num_ran += 1
            num_bloco += 1  
                           
        else:
            am = 0 #significa que não há mais espaço na matriz