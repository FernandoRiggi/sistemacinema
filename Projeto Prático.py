def incluir_elementos_filme(FILMES): #submenu para adicionar elementos no filme
    print("Escolha os elementos que deseja adicionar")
    print("1. Código do Filme")
    print("2. Nome do Filme")
    print("3. Ano de lançamento do Filme")
    print("4. Diretor do Filme")
    print("5. Atores do Filme")
    print("6. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
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
                elif opfilmes==3:
                    incluir_elementos_filme = incluir_elementos_filme(FILMES)
                elif opfilmes==4:
                elif opfilmes==5:
                elif opfilmes==6:
                    print("Encerrando programa")
                else:
                    print("Operação inválida, escolha uma opção entre 1 à 6.")
        elif operacao ==3: #abrirá o submenu de Sessões
        elif operacao == 4: #abrirá o submenu de Relátorios
        elif operacao==5: #encerrará o programa
            print("Encerrando programa")
        else: #caso digitado um número que não corresponde as operações válidas
            print("Operação inválida, escolha uma opção entre 1 à 5.")
main()