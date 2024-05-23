
##### SUBMENU DE RELÁTORIOS ######
def submenu_relatorios(RELATORIOS):
    print("Submenu RELATÓRIOS:")
    print("   1. Mostrar todos os dados de todas as salas com parâmetros")
    print("   2. Mostrar todos os filmes lançados a partir de ano de lançamento específico")
    print("   3. Mostrar os elementos, a partir de uma data inicial até uma data final")
    print("   4. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
####### SUBMENU DE SESSÕES #######
def submenu_sessoes(SESSOES):
    print("Submenu SESSÕES:")
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
    print("Submenu SALAS:")
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
    if codigo in FILMES:  
        print("Deseja confirmar a remoção do filme?")
        confirmacao = input("Para confirmar digite o codigo do filme: ")
        if confirmacao == codigo:
            del FILMES[codigo]
            return True
        else:
            print("Código de confirmação incorreto, retornando ao submenu FILMES")
    else:
        print("Código do filme não encontrado, retornando ao submenu FILMES")
######### FUNÇÃO PARA ADICIONAR O CODIGO DO FILME ########
def add_codigo(FILMES):
    codigo = input("Digite o código do filme: ")
    if codigo not in FILMES:
        FILMES[codigo]={}
        with open("filmes.txt", "a") as file:
            file.write(f"Código: {codigo}\n")
    else:
        print("O código já existe.")
    return codigo
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
        with open("filmes.txt", "a") as file:
            file.write(f"Nome: {nome}\n")
    elif op ==2:
        ano=input("Digite o ano de lançamento do filme: ")
        FILMES[codigo]["Ano"]=ano
        with open("filmes.txt", "a") as file:
            file.write(f"Ano: {ano}\n")
    elif op==3:
        diretor=input("Digite o nome do diretor: ")
        FILMES[codigo]["Diretor"]=diretor
        with open("filmes.txt", "a") as file:
            file.write(f"Diretor: {diretor}\n")
    elif op==4:
        atores=input("Digite os atores, (para separar utilize vírgula): ")
        FILMES[codigo]["Atores"]=atores.split(",")
        with open("filmes.txt", "a") as file:
            file.write(f"Atores: {",".join(atores.split(","))}\n")
    elif op==5:
        print("Saindo do menu de inclusão de elementos.")
    else:
        print("Operação inválida, escolha uma opção entre 1 e 5.")
    return op
######## MENU PARA LISTAR ELEMENTOS EM UM FILME########
def listar_elemento_especifico(FILMES, codigo):
    print("Escolha o elemento que deseja visualizar")
    print("1. Nome do Filme")
    print("2. Ano de lançamento do Filme")
    print("3. Diretor do Filme")
    print("4. Atores do Filme")
    print("5. Sair")
    op = int(input("Escolha a opção que deseja realizar: "))

    if codigo in FILMES:
        if op == 1:
            print(f"Nome: {FILMES[codigo].get('Nome', 'Não disponível')}")
        elif op == 2:
            print(f"Ano: {FILMES[codigo].get('Ano', 'Não disponível')}")
        elif op == 3:
            print(f"Diretor: {FILMES[codigo].get('Diretor', 'Não disponível')}")
        elif op == 4:
            print(f"Atores: {', '.join(FILMES[codigo].get('Atores', ['Não disponível']))}")
        elif op == 5:
            print("Saindo do menu de listagem de elementos.")
        else:
            print("Operação inválida, escolha uma opção entre 1 e 5.")
    else:
        print("Código do filme não encontrado.")
####### SUBMENU DE FILMES #######
def submenu_filmes(FILMES): #submenu de filmes
    print("Submenu FILMES:")
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
                    print(f"A lista de filmes são: {FILMES}")
                elif opfilmes==2:
                    codigo = input("Digite o código do filme para listar os detalhes: ")
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
                else:
                    print("Encerrando submenu de relátorios")
                    Menu_relatorios=False
        elif operacao==5: #encerrará o programa
            print("Encerrando programa")
            Menu = False
        else: #caso digitado um número que não corresponde as operações válidas
            print("Operação inválida, escolha uma opção entre 1 à 5.")
main()
