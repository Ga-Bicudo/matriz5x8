import random
                                                                 
matriz = [ ]
print("Eu pensava que sim, mas não consegui finalizar a tempo, a lógica esta sendo mais complexa que eu imaginava. \n\nO código ainda esta incompleto, porem o programa roda , mas com alguns bugs, o outro arquivo contem todos os testes e tudo que fiz nele \n Alem disso falta adicionar alguns comentários")
linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))                 
area_matriz = linhas * colunas
for l in range(linhas):
    i = []
    for c in range(colunas):                                
        i.append(0)
    matriz.append(i)
#Criação da matriz 


def print_matriz(matriz_desejada):                    
    for z in(matriz_desejada):
        print(z)    
#método criado para imprimir a Matriz bonitinha


r = 0                                              
am = 1
espaco = []
#chaves para o loop principal não parar enquanto tiver espaço na matriz
                                                                                     
num_bloco = 1 
#contadores de repetições

blocos = []
#lista criada para armazenar os blocos que serão inseridos no loop                                       

while(r != am ):
#loop responsável pela criação dos blocos, inserção deles na matriz e validações                                  
    
    for h in matriz:
        for j in h:                                                   
            espaco.append(j)
    teste = 0 not in espaco      
    #verificando se ha espaço na matriz

    if teste == False:                                   
        #significa que ainda tem espaço na matriz  

            altura = int(input("insira a largura do bloco:"))
            largura = int(input("insira a altura do bloco:")) 
            #bloco foi criado

            blocos.append({'nº bloco': (num_bloco), 'altura bloco': altura, 'largura bloco': largura})  
            #bloco instanciado na lista blocos 
            
            l_a = linhas - altura
            c_l = colunas - largura
                   
                   
            if l_a >= 0 and c_l >= 0:
            #verifica se o bloco criado entra na matriz 
    
                def verifica_espaço(indicex,indicey,altura,largura):#precisa consertar esta função
                    validação = []
                    for d in range(altura):
                        print('y:',y)
                        for f in range(largura):          
                            if matriz[indicey][indicex] == 0:
                                indicex += 1 
                                print('x:',x)       
                            else:
                                validação.append(1)
                                break
                        indicey += 1
                        indicex = indicex - largura
                         #verifica se tem espaço sobrando na matriz        
                    if 1 in validação:
                        return(False)
                    else:
                        return(True)

                def marca_espaço(x,y,altura,largura):
                        for d in range(altura):
                            for f in range(largura):
                                matriz[y][x] = num_bloco
                                x += 1
                            y += 1
                            x = x - largura 
                #encaixa o bloco na matriz


                y = random.randrange(0,(l_a + 1))
                x = random.randrange(0,(c_l + 1))
                #randomizar o ponto de partida do marca_matriz

                
                if y + altura > linhas or x + largura > colunas:  
                # verifica se ao fazer o verifica espaço n da erro.

                    while y + altura > linhas or x + largura > colunas:
                        y = random.randrange(0,(l_a + 1))
                        x = random.randrange(0,(c_l + 1))
                        #fica em loop ate o x e y caberem na matriz
                

                
                
    
                if verifica_espaço(x,y,altura,largura) == True:
                    marca_espaço(x,y,altura,largura)
                #encaixa o quadrado na matriz se tudo estiver certo
                


                
                else:
                # caso a varificação veja q n da para encaixar

                    area_verificada = 0
                    while verifica_espaço(x,y,altura,largura) == False:
                        area_verificada += 1 
                        y += 1
                        if area_verificada == area_matriz + 1:
                            print("não ha espaço sufieciente para o bloco desejado, crie outro por favor")
                            break
                        #se ele verificar     

                        if y + altura > linhas :  
                            x += 1   
                            y = 0
                            if  x + largura > colunas:
                                x = 0
                                y = 0
                            else:
                                continue
                        else:
                            continue
                        #verifica todos os indices da matriz se em algum é possivel encaixar o cubo        

                            
                    marca_espaço(x,y,altura,largura)        

                num_bloco += 1        
                print_matriz(matriz)
                espaco = []

            else:
                print('Bloco maior que á matriz, por favor crie outro')  

    else:
            am = 0 
        #significa que não há mais espaço na matriz



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