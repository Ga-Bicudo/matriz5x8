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
   



"""from matriz import cord_x, cord_y
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

def cria_matriz(x,y,nome_matriz):
   for l in range(x):
        for c in range(y):
            cord = [x,y]
            nome_matriz.append(cord)
            return(nome_matriz)


cord_x = []
cord_y = []
r = 0
am = 1 
num_ran = 1
num_bloco = 0
cord_usadas = [] # vai ser amezenado x, y 

while(r != am ): #enquanto tiver espaço sem bloco na matriz r() sera diferente de am(0) 
    for h in matriz: #loop de validação a cada bloco que será criado
        teste = 0 not in h  #verifica se ainda tem algum espaço na matriz sem bloco
        if teste == False: #significa que ainda tem 0  
             #começa a criação de blocos 
            altura = int(input("insira a largura do bloco:"))
            largura = int(input("insira a altura do bloco:")) 
            #bloco foi criado
            blocos = []
            blocos.append({'nº bloco': (num_bloco + 1), 'altura bloco': altura, 'largura bloco': largura, 'cord_usadas':cord_usadas })#entender este erro
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
                    x = l_i
                    cord_x.append(x)
                    for f in range(largura):
                        matriz[l_i][c_i] = num_ran
                        y = c_i
                        cord_y.append(y)
                        c_i += 1
                    l_i += 1
                    c_i = c_i - largura
                if l_i == linhas: #caso o bloco fique no fundo da matriz vamos resetar para o começo
                    l_i = 0 
                    c_i = 0
                #c_i = c_i + largura
                print_matriz(matriz)
                #print(l_i,c_i,y)
                num_ran += 1        
            else:        
                diferença = linhas - l_i
                diferença_coluna = colunas - c_i
                if altura > diferença or colunas > diferença_coluna:
                    for p in range(diferença):
                        for k in range(diferença_coluna):
                            c_i += 1
                        l_i += 1 
                        c_i = c_i - diferença_coluna
                    while l_i >linhas:
                        if altura > diferença: 
                            l_i = y + 1
                            c_i = l_i
                        if colunas > diferença_coluna:
                            l_i = x + 1
                            c_i = l_i
                        #if altura > diferença and colunas > diferença_coluna:

                        try:
                            for m in range(altura):                 
                                for n in range(largura): 
                                    matriz[l_i][c_i] = num_ran
                                    cord_usadas = l_i,c_i
                                    y = c_i 
                                    c_i += 1
                                l_i += 1
                                c_i = c_i - largura          
                            num_ran = num_ran + 1
                            print_matriz(matriz) 
                        except:
                            print("bloco não cabe em nenhum lugar da matriz")          
                else:
                    for d in range(altura):
                        x = l_i
                        cord_x.append(x)
                        for f in range(largura):
                            y = c_i
                            cord_y.append(y)
                            while matriz[l_i][c_i] > 0:

                                break               
                            matriz[l_i][c_i] = num_ran
                            c_i += 1
                        l_i += 1
                        c_i = c_i - largura 
        else:
            am = 0 #significa que não há mais espaço na matriz"""
            



"""matriz = [ ]

linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))                  #tentativa de fazer uma matriz secundaria para calcular quantos blocos precisa para fechar o principal
area_matriz = linhas * colunas #não vou fazer matriz so pega os tamanhos
for l in range(linhas):
        i = []
        for c in range(colunas):
            i.append(0)
        matriz.append(i)

num_ran = 1
area_matriz_sobrando = len
matriz_aux = []
while(area_matriz_sobrando == 0):
    altura = int(input("insira a largura do bloco:"))
    largura = int(input("insira a altura do bloco:"))      
    for x in range(altura): # inseri o x que seria relacionado ao primeiro bloco
        i = []
        for y in range(largura):
            i.append('x')
            matriz[x][y] = num_ran           
    num_ran = num_ran + 1    
    for x in(matriz):
        print(x)"""

   
"""num_ran = 1
resposta = "sim"
while(resposta == 'sim'):
    matriz = []
    altura = int(input("insira a largura do bloco:"))
    largura = int(input("insira a altura do bloco:"))      
    for x in range(altura): # inseri o x que seria relacionado ao primeiro bloco
        i = []
        for y in range(largura):
            i.append(num_ran)
    num_ran = num_ran + 1    
    for x in(matriz):
        print(x)"""








"""matriz = [ ]

linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))
area_matriz = linhas * colunas
for l in range(linhas):
        i = []
        for c in range(colunas):
            i.append('0')
        matriz.append(i)


area_blocos = 0
blocks = []  #lista criada para guardar os blocos
for blocos in range(0,area_matriz): #repetição feita para o possivel maximo de blocos com tamanho minimo(1x1) poderem ser criados.
    largura = int(input("insira a altura do bloco:"))
    altura = int(input("insira a largura do bloco:"))
    bloco = largura * altura   # criando objeto bloco
    if altura > linhas or largura > colunas:  #validando se o objeto pode ser guardado
        print("bloco inválido")
    elif(area_matriz > area_blocos):
        blocks.append(bloco)      #adicionalndo na lista blocks o objeto
        area_blocos = sum(blocks) #cria um objeto com a soma dos blocos criados na lista 
        for x in (blocks):
            print(x)
            for x in range(altura):
                for y in range(largura):
                    matriz[x][y] = 'x'
    else:  
          print('tamanho do bloco inválido')
"""




"""matriz = [ ]
area_blocos = 0
area_matriz = 25
linhas = 5 
colunas = 5
blocks= []

for blocos in range(0,area_matriz):
    largura = int(input("insira a altura do bloco:"))
    altura = int(input("insira a largura do bloco:"))
    bloco = largura * altura  #cria um bloco
    if altura > linhas or largura > colunas:
        print("bloco inválido")
    elif(area_matriz > bloco):  # 25 > 6
        linhas = (linhas - altura) # 5 - 3 = 2
        colunas = (colunas - largura)# 5 - 2 = 3
        blocks.append(bloco)
        area_blocos = sum(blocks) #cria um objeto com a soma dos blocos criados na lista 
        for x in (blocks):
            print(x)
    else:
        print('não ha espaço na matriz para o ultimo bloco desejado \n espaço sobrando = {}x{}'.format()) """



'''matriz = [ ]
area_blocos = 0
area_matriz = 25
linhas = 5 
colunas = 5
blocks= []

for blocos in range(0,area_matriz):
    largura = int(input("insira a altura do bloco:"))
    altura = int(input("insira a largura do bloco:"))
    bloco = largura * altura
    if altura > linhas or largura > colunas:
        print("bloco inválido")
    else:
        blocks.append(bloco)
        area_blocos = sum(blocks)
        for x in (blocks):
            print(x)'''





        
'''def teste():        
    z = 20
    x = (385 - z)
    while x <= 0:
        y = x - z
        x = y 
        return(x)

print(teste())        
sys.path()'''