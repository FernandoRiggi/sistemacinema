def add_codigo(FILMES):
    codigo = input("Digite o código do filme: ")
    if codigo not in FILMES:
        FILMES[codigo]={}
        with open("filmes.txt", "a") as file:
            file.write(f"Código: {codigo}\n")
    else:
        print("O código já existe.")
    return codigo
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
def submenu_filmes(FILMES): #submenu de filmes
    print("Escolha uma opção entre 1 à 5 ou digite 6 para sair")
    print("1. Listar todos os filmes")
    print("2. Listar um elemento específico do conjunto")
    print("3. Incluir elementos do filme")
    print("4. Alterar elementos do filme")
    print("5. Excluir um elemento do conjunto do filme")
    print("6. Sair")
    op = int(input("Escolha a opção que deseja realizar: "))
    return op
def menu(): #função para escolha das subopções
    print("Escolha uma opção entre 1 à 4 ou digite 5 para sair")
    print("1. Submenu de Salas")
    print("2. Submenu de Filmes")
    print("3. Submenu de Sessões")
    print("4. Submenu de Relatórios")
    print("5. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
def main(): #programa principal
    operacao=1
    FILMES={}
    while operacao !=5:
        operacao = menu() #chama o menu das opções principais
        if operacao == 1: #abrirá o submenu de Salas
        elif operacao ==2: #abrirá o submenu de Filmes
            opfilmes=1
            while opfilmes !=6:
                opfilmes = submenu_filmes(FILMES) #chama o submenu de filmes
                if opfilmes ==1:
                    print(f"A lista de todos os filmes são: {FILMES}")
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
                    if codigo in FILMES:
                        del FILMES[codigo]
                        print(f"Filme {codigo} excluído. \n")
                    else: 
                        print("Código do filme não encontrado")
                elif opfilmes==6:
                    print("Encerrando submenu de filmes.")
                else:
                    print("Operação inválida, escolha uma opção entre 1 à 6.")
        elif operacao ==3: #abrirá o submenu de Sessões
        elif operacao == 4: #abrirá o submenu de Relátorios
        elif operacao==5: #encerrará o programa
            print("Encerrando programa")
        else: #caso digitado um número que não corresponde as operações válidas
            print("Operação inválida, escolha uma opção entre 1 à 5.")
main()