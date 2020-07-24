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
