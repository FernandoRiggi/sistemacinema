def gravar_arquivo(FILMES):
    arq= open('./filmes.txt', 'w')
    if Existe_Arquivo('./filmes.txt'):
        for codigo in FILMES:
            frase = ''
            frase = codigo +';' + FILMES[codigo]['Nome'] +';' + str(FILMES[codigo]['Ano'])+';'+FILMES[codigo]['Diretor']+';'
            for ator in FILMES[codigo]['Atores']:
                frase += ator +'@'
            frase+= "\n"
            arq.write(frase)
            
    else:
        print('Arquivo não existe')
########FUNÇÃO PARA VER SE EXISTE ALGO NO ARQUIVO###########
def Existe_Arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
#####FUNÇÃO PARA LER OS DADOS DO ARQUIVO FILMES E ADD EM DICT #########
def ler_filmes(FILMES):
    if Existe_Arquivo('./filmes.txt'):
        with open('filmes.txt','r') as file:
            for linha in file:
                linha = linha.split(';')
                codigo = linha[0]
                FILMES[codigo]={}
                FILMES[codigo]['Nome']=linha[1]
                ano=linha[2]
                FILMES[codigo]['Ano']=int(ano)
                FILMES[codigo]['Diretor']=linha[3]
                atores=linha[4].strip().split('@')[:-1]
                FILMES[codigo]['Atores']=atores
        return(FILMES)
    else:
        return False
######FUNÇÃO LISTAR DADOS DE FILME A PARTIR DE X#######
def listar_filmes_data(FILMES, data_filme):
    print(f"Filmes lançados a partir de {data_filme}:")
    for codigo in FILMES:
        if int(FILMES[codigo]['Ano'])>= data_filme:
            print("\n")
            print("Código:",codigo)
            print("Título:",FILMES[codigo]['Nome'])
            print("Ano de lançamento:",FILMES[codigo]['Ano'])
            print("Diretor:",FILMES[codigo]['Diretor'])
            print("Atores:",", ".join(FILMES[codigo]['Atores']))
##### SUBMENU DE RELÁTORIOS ######
def submenu_relatorios(RELATORIOS):
    print("\nSubmenu RELATÓRIOS:")
    print("   1. Mostrar todos os dados de todas as salas com parâmetros")
    print("   2. Mostrar todos os filmes lançados a partir de ano de lançamento específico")
    print("   3. Mostrar os elementos, a partir de uma data inicial até uma data final")
    print("   4. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
####### SUBMENU DE SESSÕES #######
def submenu_sessoes(SESSOES):
    print("\nSubmenu SESSÕES:")
    print("   1. Listar todas as salas")
    print("   2. Listar um elemento específico do conjunto")
    print("   3. Incluir elementos específico do conjunto")
    print("   4. Alterar elementos da sessão")
    print("   5. Excluir um elemento do conjunto das sessões")
    print("   6. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
###### SUBMENU DE SALAS #######
def submenu_salas(SALAS):
    print("\nSubmenu SALAS:")
    print("   1. Listar todas as salas")
    print("   2. Listar um elemento específico do conjunto")
    print("   3. Incluir elementos específico do conjunto")
    print("   4. Alterar elementos da sala")
    print("   5. Excluir um elemento do conjunto das salas")
    print("   6. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
######FUNÇÃO PARA REMOVER O FILME #############
def remove_filme(FILMES, codigo):
    print("Deseja confirmar a remoção do filme?")
    confirmacao = input("Para confirmar digite o codigo do filme: ")
    if confirmacao == codigo:
        if confirmacao in FILMES:
            del FILMES[codigo]
            return True
        else:
            print("Código do filme não encontrado, retornando ao submenu FILMES")
            return False
    else:
        print("Código de confirmação incorreto, retornando ao submenu FILMES")
        return False
######### FUNÇÃO PARA ADICIONAR O CODIGO DO FILME ########
def add_codigo(FILMES):
    codigo = input("Digite o código do filme: ")
    if codigo not in FILMES:
        FILMES[codigo]={}           
    else:
        print("O código já existe.")
    return codigo
#####FUNÇÃO PARA LISTAR OS FILMES#####
def listar_filmes(FILMES):
    print("Lista de filmes no sistema:")
    for codigo in FILMES:
        print(FILMES[codigo]['Nome'])
######## MENU PARA ADICIONAR ELEMENTOS EM UM FILME#######
def incluir_elementos_filme(FILMES, codigo): #submenu para adicionar elementos no filme
    print("Escolha os elementos que deseja adicionar")
    print("1. Nome do Filme")
    print("2. Ano de lançamento do Filme")
    print("3. Diretor do Filme")
    print("4. Atores do Filme")
    print("5. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    if op ==1:
        nome = input("Digite o nome do filme: ")
        FILMES[codigo]["Nome"]=nome
    elif op ==2:
        ano=input("Digite o ano de lançamento do filme: ")
        FILMES[codigo]["Ano"]=ano
    elif op==3:
        diretor=input("Digite o nome do diretor: ")
        FILMES[codigo]["Diretor"]=diretor
    elif op==4:
        atores=input("Digite os atores, (para separar utilize vírgula): ")
        FILMES[codigo]["Atores"]=atores.split(",")
    elif op==5:
        print("Saindo do menu de inclusão de elementos.")
    else:
        print("Operação inválida, escolha uma opção entre 1 e 5.")
    return op
######## MENU PARA LISTAR ELEMENTOS EM UM FILME########
def listar_elemento_especifico(FILMES, codigo):
    print("Escolha o elemento que deseja visualizar")
    print("   1. Nome do Filme")
    print("   2. Ano de lançamento do Filme")
    print("   3. Diretor do Filme")
    print("   4. Atores do Filme")
    print("   5. Sair")
    op = int(input("Escolha a opção que deseja realizar: "))
    if op == 1:
        print(f"Nome: {FILMES[codigo]['Nome']}")
    elif op == 2:
        print(f"Ano: {FILMES[codigo]['Ano']}")
    elif op == 3:
        print(f"Diretor: {FILMES[codigo]['Diretor']}")
    elif op == 4:
        print(f"Atores: {', '.join(FILMES[codigo]['Atores'])}")
    elif op == 5:
        print("Saindo do menu de listagem de elementos.")
    else:
        print("Operação inválida, escolha uma opção entre 1 e 5.")
####### SUBMENU DE FILMES #######
def submenu_filmes(FILMES): #submenu de filmes
    print("\nSubmenu FILMES:")
    print("   1. Listar todos os filmes")
    print("   2. Listar um elemento específico do conjunto")
    print("   3. Incluir elementos do filme")
    print("   4. Alterar elementos do filme")
    print("   5. Excluir um elemento do conjunto do filme")
    print("   6. Sair")
    op = int(input("Escolha a opção que deseja realizar: "))
    return op
#########MENU DE SUBOPÇÕES######
def menu(): 
    print("Menu de Opções:")
    print("  1. Submenu de Salas")
    print("  2. Submenu de Filmes")
    print("  3. Submenu de Sessões")
    print("  4. Submenu de Relatórios")
    print("  5. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
def main(): #programa principal
    FILMES={}
    SALAS={}
    SESSOES={}
    RELATORIOS={}
    Menu = True
    ler_filmes(FILMES)
    while Menu:
        operacao = menu() #chama o menu das opções principais
        if operacao == 1: #abrirá o submenu de Salas
            opsalas = 1
            Menu_salas = True
            while Menu_salas == True:
                opsalas = submenu_salas(SALAS) #chama o submenu de salas
                if opsalas==1:
                    print(f"A lista de salas são: {SALAS}")
                elif opsalas ==6:
                    print("Encerrando submenu de salas")
                    Menu_salas = False
        elif operacao ==2: #abrirá o submenu de Filmes
            opfilmes=1
            Menu_filmes = True
            while Menu_filmes == True:
                opfilmes = submenu_filmes(FILMES) #chama o submenu de filmes
                if opfilmes == 1:
                    listar_filmes(FILMES)
                elif opfilmes==2:
                    codigo = input("Digite o código do filme para listar os detalhes: ")
                    ler_filmes(FILMES)
                    listar_elemento_especifico(FILMES, codigo)
                elif opfilmes==3:
                    codigo = add_codigo(FILMES)
                    incluir_elementos_filme_op=1
                    while incluir_elementos_filme_op !=5:
                        incluir_elementos_filme_op = incluir_elementos_filme(FILMES, codigo)
                elif opfilmes==4:
                    codigo = input("Digite o código do filme que deseja alterar: ")
                    if codigo in FILMES:
                        incluir_elementos_filme_op=1
                        while incluir_elementos_filme_op!=5:
                            incluir_elementos_filme_op=incluir_elementos_filme(FILMES, codigo)
                    else:
                        print("Código não encontrado.")
                elif opfilmes==5:
                    codigo = input("Digite o código do filme que deseja excluir: ")
                    remover = remove_filme(FILMES, codigo)
                    if remover == True:
                        print(f"O filme {codigo} foi excluido")
                elif opfilmes==6:
                    print("Encerrando submenu de filmes.")
                    gravar_arquivo(FILMES)
                    Menu_filmes=False
                else:
                    print("Operação inválida, escolha uma opção entre 1 à 6.")
        elif operacao ==3: #abrirá o submenu de Sessões
            opsessoes = 1
            Menu_sessoes = True
            while Menu_sessoes ==True:
                opsessoes = submenu_sessoes(SESSOES) #chama o submenu de sessoes
                if opsessoes == 1:
                    print(f"A lista de todas as Sessões são: {SESSOES}")
                elif opsessoes==6:
                    print("Encerrando submenu de sessões.")
                    Menu_sessoes=False
        elif operacao == 4: #abrirá o submenu de Relátorios
            oprelatorios = 1
            Menu_relatorios = True
            while Menu_relatorios==True:
                oprelatorios = submenu_relatorios(RELATORIOS)
                if oprelatorios==1:
                    print("Mostrar todos as salas cujo tipo de exibição seja X e capacidade para mais de Y pessoas, onde X e Y são fornecidos pelo usuário;")
                elif oprelatorios==2:
                    data_filme=int(input("Digite a data que deseja ver as informações dos filmes lançados a partir dela: "))
                    listar_filmes_data(FILMES, data_filme)
                else:
                    print("Encerrando submenu de relátorios")
                    Menu_relatorios=False
        elif operacao==5: #encerrará o programa
            print("Encerrando programa")
            Menu = False
        else: #caso digitado um número que não corresponde as operações válidas
            print("Operação inválida, escolha uma opção entre 1 à 5.")
main()