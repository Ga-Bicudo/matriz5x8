atriz = [ ]

linhas = int(input("escolha quantas linhas tera a matriz:"))
colunas = int(input("escolha quantas colunas tera a matriz:"))
area_matriz = linhas * colunas
for l in range(linhas):
        i = []
        for c in range(colunas):
            i.append(0)
        matriz.append(i)

num_ran = 1
for encaixes in range(area_matriz):
    largura = int(input("insira a altura do bloco:"))
    altura = int(input("insira a largura do bloco:"))     
    for x in range(altura): # inseri o x que seria relacionado ao primeiro bloco
        for y in range(largura):
            matriz[x][y] = num_ran
    num_ran = num_ran + 1    
    for x in(matriz):
        print(x)

   









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