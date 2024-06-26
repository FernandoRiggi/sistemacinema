import datetime
###### SUBMENU DE SALAS #######
def submenu_salas():
    print("\nSubmenu SALAS:")
    print("   1. Listar todas as salas")
    print("   2. Listar um elemento específico do conjunto")
    print("   3. Incluir elementos específico do conjunto")
    print("   4. Alterar elementos da sala")
    print("   5. Excluir um elemento do conjunto das salas")
    print("   6. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
####FUNÇÃO PARA LER OS DADOS DO ARQUIVO SALAS E ADD EM DICT####
def ler_salas(SALAS):
    if Existe_Arquivo('./salas.txt'):
        with open('salas.txt', 'r') as file:
            for linha in file:
                linha = linha.split(';')
                codigo = linha[0]
                SALAS[codigo]={}
                SALAS[codigo]['Codigo']=codigo
                SALAS[codigo]['Nome']=linha[1]
                capacidade = linha[2]
                SALAS[codigo]['Capacidade']=int(capacidade)
                SALAS[codigo]['Exibicao']=linha[3]
                SALAS[codigo]['Acessivel']=linha[4]
            return(SALAS)
    else:
        return False
####FUNÇÃO PARA LISTAR SALAS####
def listar_salas(SALAS):
    print("Lista de salas no sistema:")
    for codigo in SALAS:
        print('\n')
        print(SALAS[codigo]['Nome'])
####FUNÇÃO PARA LISTAR ELEMENTO ESPECIFICO SALAS####
def listar_elemento_especifico_salas(SALAS, codigo):
    Submenu = True
    while Submenu:
        print("Escolha o elemento que deseja visualizar")
        print("   1. Nome da Sala")
        print("   2. Capacidade da Sala")
        print("   3. Tipo de Exibição")
        print("   4. Acessível")
        print("   5. Sair")
        op = int(input("Escolha a opção que deseja realizar: "))
        if op == 1:
            print(f"Nome: {SALAS[codigo]['Nome']}")
        elif op == 2:
            print(f"Capacidade: {SALAS[codigo]['Capacidade']}")
        elif op == 3:
            print(f"Tipo de Exibição: {SALAS[codigo]['Exibicao']}")
        elif op == 4:
            print(f"Acessibilidade: {SALAS[codigo]['Acessivel']}")
        elif op == 5:
            print("Saindo do menu de listagem de elementos.")
            Submenu = False
        else:
            print("Operação inválida, escolha uma opção entre 1 e 5.")
####FUNÇÃO PARA ADD O CODIGO DA SALA####
def add_codigo_salas(SALAS):
    codigo = input("Digite o código da sala: ")
    codigo=codigo.upper()
    if codigo not in SALAS:
        SALAS[codigo]={}
        SALAS[codigo]['Codigo']=codigo
    else:
        print("O código já existe.")
    return codigo
####FUNÇÃO PARA INCLUIR ELEMENTO EM SALAS####
def incluir_elementos_sala(SALAS, codigo): 
    Submenu = True
    while Submenu:
        print("Escolha os elementos que deseja adicionar")
        print("1. Nome da Sala")
        print("2. Capacidade da Sala")
        print("3. Tipo de Exibição da Sala")
        print("4. Acessível")
        print("5. Sair")
        op=int(input("Escolha a opção que deseja realizar: "))
        if op ==1:
            nome = input("Digite o nome da sala: ")
            SALAS[codigo]["Nome"]=nome
        elif op ==2:
            capacidade=input("Digite a capacidade da sala: ")
            SALAS[codigo]["Capacidade"]=capacidade
        elif op==3:
            exibicao=input("Digite o tipo de exibição da sala: ")
            SALAS[codigo]["Exibicao"]=exibicao
        elif op==4:
            acessivel=input("Digite se a sala está acessível: ")
            SALAS[codigo]["Acessivel"]=acessivel
        elif op==5:
            print("Saindo do menu de inclusão de elementos.")
            Submenu = False
        else:
            print("Operação inválida, escolha uma opção entre 1 e 5.")
####FUNÇÃO PARA REMOVER SALA####
def remove_sala(SALAS, codigo):
    print("Deseja confirmar a remoção da sala?")
    confirmacao = input("Para confirmar digite o codigo do sala: ")
    confirmacao=confirmacao.upper()
    if confirmacao == codigo:
        if confirmacao in SALAS:
            del SALAS[codigo]
            return True
        else:
            print("Código do filme não encontrado, retornando ao submenu SALAS")
            return False
    else:
        print("Código de confirmação incorreto, retornando ao submenu SALAS")
        return False
####FUNÇÃO PARA GRAVAR SALAS EM ARQUIVOS####
def gravar_sala(SALAS):
    arq=open('./salas.txt', 'w')
    if Existe_Arquivo('./salas.txt'):
        for codigo in SALAS:
            frase=''
            frase = codigo +';' + SALAS[codigo]['Nome'] +';' + str(SALAS[codigo]['Capacidade'])+';'+SALAS[codigo]['Exibicao']+';' +SALAS[codigo]['Acessivel']
            frase+='\n'
            arq.write(frase)
####### SUBMENU DE FILMES #######
def submenu_filmes(): #submenu de filmes
    print("\nSubmenu FILMES:")
    print("   1. Listar todos os filmes")
    print("   2. Listar um elemento específico do conjunto")
    print("   3. Incluir elementos do filme")
    print("   4. Alterar elementos do filme")
    print("   5. Excluir um elemento do conjunto do filme")
    print("   6. Sair")
    op = int(input("Escolha a opção que deseja realizar: "))
    return op
#####FUNÇÃO PARA LER OS DADOS DO ARQUIVO FILMES E ADD EM DICT #########
def ler_filmes(FILMES):
    if Existe_Arquivo('./filmes.txt'):
        with open('filmes.txt','r') as file:
            for linha in file:
                linha = linha.split(';')
                codigo = linha[0]
                FILMES[codigo]={}
                FILMES[codigo]['Codigo'] = codigo
                FILMES[codigo]['Nome']=linha[1]
                ano=linha[2]
                FILMES[codigo]['Ano']=int(ano)
                FILMES[codigo]['Diretor']=linha[3]
                atores=linha[4].strip().split('@')[:-1]
                FILMES[codigo]['Atores']=atores
        return(FILMES)
    else:
        return False
#####FUNÇÃO PARA LISTAR OS FILMES#####
def listar_filmes(FILMES):
    print("Lista de filmes no sistema:")
    for codigo in FILMES:
        print(FILMES[codigo]['Nome'])
######## MENU PARA LISTAR ELEMENTOS EM UM FILME########
def listar_elemento_especifico_filme(FILMES, codigo):
    Submenu = True
    while Submenu:
        print("Escolha o elemento que deseja visualizar:")
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
            Submenu = False
        else:
            print("Operação inválida, escolha uma opção entre 1 e 5.")
######### FUNÇÃO PARA ADICIONAR O CODIGO DO FILME ########
def add_codigo_filmes(FILMES):
    codigo = input("Digite o código do filme: ").upper()
    if codigo not in FILMES:
        FILMES[codigo]={}
        FILMES[codigo]['Codigo']=codigo           
    else:
        print("O código já existe.")
    return codigo
######## MENU PARA ADICIONAR ELEMENTOS EM UM FILME#######
def incluir_elementos_filme(FILMES, codigo): #submenu para adicionar elementos no filme
    Submenu = True
    while Submenu:
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
            Submenu = False
        else:
            print("Operação inválida, escolha uma opção entre 1 e 5.")
######FUNÇÃO PARA REMOVER O FILME #############
def remove_filme(FILMES, codigo):
    print("Deseja confirmar a remoção do filme?")
    confirmacao = input("Para confirmar digite o codigo do filme: ").upper()
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
####FUNÇÃO PARA GRAVAR FILMES EM ARQUIVOS####
def gravar_filme(FILMES):
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
####### SUBMENU DE SESSÕES #######
def submenu_sessoes():
    print("\nSubmenu SESSÕES:")
    print("   1. Listar todas as sessões")
    print("   2. Listar um elemento específico do conjunto")
    print("   3. Incluir elementos específico do conjunto")
    print("   4. Alterar elementos da sessão")
    print("   5. Excluir um elemento do conjunto das sessões")
    print("   6. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
####ler_sessoes####
def ler_sessoes(SESSOES):
    if Existe_Arquivo('./sessoes.txt'):
        with open('sessoes.txt') as file:
            for linha in file:
                linha = linha.split(';')
                codigo_filme=linha[0]
                codigo_sala=linha[1]
                datastr=linha[2]
                horariostr=linha[3]
                tupla=(codigo_filme,codigo_sala,datastr,horariostr)
                SESSOES[tupla]={}
                SESSOES[tupla]['Preço']=float(linha[4])
            return SESSOES
    else:
        return False 
#########LISTAR SESSOES###########
def listar_sessoes(Sessões):
    print('Lista de sessões no sistema: ')
    for codigo in Sessões.keys():
        print('\n')
        print(f'{Sessões[codigo]["Preço"]}') 
#######LISTAR ELEMENTOS DO DIC DE SESSOES#########
def listar_elementos_especifico_sessões(SESSOES,tupla):
    if tupla in SESSOES:
                print('Escolha o elemento que deseja visualizar:')
                print(' 1. Valor')
                print(' 2. Sair')
                op = int(input('Escolha a opção que deseja visualizar: '))
                if op == 1:
                    print(f'Preço da Sessão: {SESSOES[tupla]["Preço"]}')
                elif op == 2:
                    print('Saindo do Menu de listagem de elementos...')
                else:
                    print('Valor inválido, escolha uma opção de 1 a 2')
                return True
    else:
        return False
####FUNÇÃO GERAR SESSÃO####
def GerarSessão(FILMES,SALAS,SESSOES):
    codigo_filme=input("Digite o código do Filme: ")
    codigo_filme=codigo_filme.upper()
    codigo_sala=input("Digite o código da Sala: ")
    codigo_sala=codigo_sala.upper()
    data = input('Entre com a data da sessão na formatação (AAAA-MM-DD): ')
    horario = input('Digite o horario da sessão na formatação (HH:MM:SS): ')
    if codigo_filme in FILMES and codigo_sala in SALAS:
        tupla=(FILMES[codigo_filme]['Codigo'], SALAS[codigo_sala]['Codigo'],data,horario)
        SESSOES[tupla]={}
        return True and tupla    
    else:
        return False
####GERAR TUPLA####
def gerar_tupla(FILMES, SALAS):
    filme=input('Digite o código do filme: ').upper()
    sala=input("Digite o código da sala: ").upper()
    data = input('Entre com a data da sessão na formatação (AAAA-MM-DD): ')
    horario = input('Digite o horario da sessão na formatação (HH:MM:SS): ')
    if filme in FILMES and sala in SALAS:
        tupla=(FILMES[filme]['Codigo'], SALAS[sala]['Codigo'],data,horario)
        return tupla    
    else: 
        return False
####ADD_PREÇO####
def add_preço(SESSOES,tupla):
    preco = float(input('Entre com o preço da sessão: '))
    if tupla in SESSOES:
        SESSOES[tupla]['Preço']=preco
        return True
    else:
        return False
######FUNÇÃO DEL SESSÃO#####
def excluir_sessão(SESSOES,codigo):
    print("Deseja confirmar a remoção da sessão?")
    confirmacao = input("Para confirmar digite o codigo da sessão: ").lower()
    if confirmacao == 'sim':
        if codigo in SESSOES:
            del SESSOES[codigo]
            return True
        else:
            print("Código do filme não encontrado, retornando ao submenu SESSÕES")
            return False
    else:
        print("Código de confirmação incorreto, retornando ao submenu SESSÕES")
        return False
####gravar_sessoes####
def gravar_sessoes(SESSOES):
    arq=open('./sessoes.txt', 'w')
    if Existe_Arquivo('./sessoes.txt'):
        for codigo in SESSOES:
            frase=''
            frase=codigo[0]+';'+codigo[1]+';'+str(codigo[2])+';'+str(codigo[3])+';'+str(SESSOES[codigo]['Preço'])
            frase+='\n'
            arq.write(frase)
    else:
        print("Não existe arquivo")
##### SUBMENU DE RELÁTORIOS ######
def submenu_relatorios():
    print("\nSubmenu RELATÓRIOS:")
    print("   1. Mostrar todos os dados de todas as salas com parâmetros")
    print("   2. Mostrar todos os filmes lançados a partir de ano de lançamento específico")
    print("   3. Mostrar os elementos, a partir de uma data inicial até uma data final")
    print("   4. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
####FUNÇÃO LISTAR DADOS DE SALA A PARTIR DE X E Y(RELATORIO 1)####
def listar_salas_cap_exib(SALAS,tipo_de_exibicao,capacidade):
    arq=open('./relatórios1.txt', 'w')
    arq.write('**************************Relatório de Salas**************************\n\n')
    arq.write(f"Salas com exibição {tipo_de_exibicao} e capacidade {capacidade}\n\n")
    for codigo in SALAS:
        if int(SALAS[codigo]['Capacidade'])==capacidade and SALAS[codigo]['Exibicao']==tipo_de_exibicao:
            arq.write((f"Código: {codigo}\n"))
            arq.write((f"Nome: {SALAS[codigo]['Nome']}\n"))
            arq.write((f"Capacidade: {SALAS[codigo]['Capacidade']}\n")) 
            arq.write((f"Tipo de Exibição: {SALAS[codigo]['Exibicao']}\n"))
            arq.write((f"Acessível: {SALAS[codigo]['Acessivel']}\n"))
######FUNÇÃO LISTAR DADOS DE FILME A PARTIR DE X(RELATORIO 2)#######
def listar_filmes_data(FILMES, data_filme):
    with open('./relatórios2.txt', 'w') as arq:
        arq.write('**************************Relatório de Filmes**************************\n\n')
        arq.write(f"Filmes lançados a partir de {data_filme}:\n\n")
        for codigo, filme in FILMES.items():
            if int(filme['Ano']) >= data_filme:
                arq.write(f"Código: {codigo}\n")
                arq.write(f"Título: {filme['Nome']}\n")
                arq.write(f"Ano de lançamento: {filme['Ano']}\n")
                arq.write(f"Diretor: {filme['Diretor']}\n")
                arq.write(f"Atores: {', '.join(filme['Atores'])}\n")
                arq.write('\n')
####RELATORIO 3####
def listar_dados_sessões_data(SESSOES, FILMES, SALAS, data_inicio, data_fim):
    with open('./relatórios3.txt', 'w') as arq:
        arq.write('**************************Relatório de Sessões**************************\n\n')
        arq.write(f"Sessões exibidas a partir de {data_inicio.strftime('%Y-%m-%d')} até {data_fim.strftime('%Y-%m-%d')}\n\n")
        # Converter data_inicio para datetime.datetime
        data_inicio_dt = datetime.datetime.combine(data_inicio, datetime.datetime.min.time())
        for codigo in SESSOES:
            data_sessao_str = codigo[2]
            data_sessao_obj = datetime.date(*map(int, data_sessao_str.split('-')))
            horario_sessao_str=codigo[3]
            horario_sessao_obj = datetime.time(*map(int, horario_sessao_str.split(':')))
            if isinstance(data_sessao_str, datetime.date):
                data_sessao_obj = data_sessao_str
            else:
                data_sessao_obj = datetime.datetime.strptime(data_sessao_str, "%Y-%m-%d").date()
            # Converter data_sessao_obj para datetime.datetime se necessário
            if isinstance(data_sessao_obj, datetime.date):
                data_sessao_obj = datetime.datetime.combine(data_sessao_obj, datetime.datetime.min.time())
            if data_inicio_dt <= data_sessao_obj <= data_fim:
                codigo_filme = codigo[0]
                codigo_sala = codigo[1]
                arq.write(f"Data da sessão: {data_sessao_obj.strftime('%Y-%m-%d')}\n")
                arq.write(f"Horário da sessão: {horario_sessao_obj.strftime('%H:%M')}\n")
                arq.write(f"Preço da sessão: {SESSOES[codigo]['Preço']}\n")
                arq.write(f"Código do filme: {FILMES[codigo_filme]['Codigo']}\n")
                arq.write(f"Nome do filme: {FILMES[codigo_filme]['Nome']}\n")
                arq.write(f"Atores do filme: {', '.join(FILMES[codigo_filme]['Atores'])}\n")
                arq.write(f"Código da sala: {SALAS[codigo_sala]['Codigo']}\n")
                arq.write(f"Nome da sala: {SALAS[codigo_sala]['Nome']}\n")
                arq.write('\n')
####obter_data_rel_3####
def obter_data():
    while True:
        data_str = input("Digite a data no formato AAAA-MM-DD: ")
        data = datetime.datetime.strptime(data_str, "%Y-%m-%d")
        return data
########FUNÇÃO PARA VER SE EXISTE ALGO NO ARQUIVO###########
def Existe_Arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
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
    Menu = True
    ler_filmes(FILMES)
    ler_salas(SALAS)
    ler_sessoes(SESSOES)
    while Menu:
        operacao = menu() #chama o menu das opções principais
        if operacao == 1: #abrirá o submenu de Salas
            print(f'Abrindo o SubMenu de Salas: ')
            Menu_salas = True
            while Menu_salas == True:
                opsalas = submenu_salas() #chama o submenu de salas
                if opsalas==1:
                    listar_salas(SALAS)
                elif opsalas==2:
                    codigo = input("Digite o código da sala para listar os detalhes: ").upper()
                    if codigo in SALAS.keys():
                        listar_elemento_especifico_salas(SALAS, codigo)
                    else:
                        print('A sala não foi encontrada.')
                elif opsalas==3:
                    codigo = add_codigo_salas(SALAS)
                    incluir_elementos_sala(SALAS, codigo)
                elif opsalas==4:
                    codigo = input('Entre com o codigo da sala que deseja alterar: ')
                    if codigo in SALAS.keys():
                        incluir_elementos_sala(SALAS, codigo)
                    else:
                        print('O codigo não foi encontrado.')
                elif opsalas==5:
                    codigo = input("Digite o código da sala que deseja remover: ").upper()
                    remover=remove_sala(SALAS, codigo)
                    if remover == True:
                        print(f"A sala {codigo} foi removida")
                elif opsalas ==6:
                    print("Encerrando submenu de salas")
                    gravar_sala(SALAS)
                    Menu_salas = False
                else:
                    print("Operação inválida, escolha uma opção entre 1 à 6.")
        elif operacao ==2: #abrirá o submenu de Filmes
            print(f'Abrindo o SubMenu de Filmes: ')
            Menu_filmes = True
            while Menu_filmes == True:
                opfilmes = submenu_filmes() #chama o submenu de filmes
                if opfilmes == 1:
                    listar_filmes(FILMES)
                elif opfilmes==2:
                    codigo = input("Digite o código do filme para listar os detalhes: ").upper()
                    listar_elemento_especifico_filme(FILMES, codigo)
                elif opfilmes==3:
                    codigo = add_codigo_filmes(FILMES).upper()
                    incluir_elementos_filme(FILMES, codigo)
                elif opfilmes==4:
                    codigo = input("Digite o código do filme que deseja alterar: ").upper()
                    if codigo in FILMES.keys():
                        incluir_elementos_filme(FILMES, codigo)
                    else:
                        print("Código não foi encontrado.")
                elif opfilmes==5:
                    codigo = input("Digite o código do filme que deseja excluir: ").upper()
                    remover = remove_filme(FILMES, codigo)
                    if remover == True:
                        print(f"O filme {codigo} foi excluido")
                elif opfilmes==6:
                    print("Encerrando submenu de filmes.")
                    gravar_filme(FILMES)
                    Menu_filmes=False
                else:
                    print("Operação inválida, escolha uma opção entre 1 à 6.")
        elif operacao ==3: #abrirá o submenu de Sessões
            print(f'Abrindo o SubMenu de Sessões: ')
            Menu_sessoes = True
            while Menu_sessoes ==True:
                opsessoes = submenu_sessoes() #chama o submenu de sessoes
                if opsessoes == 1:
                    listar_sessoes(SESSOES)
                elif opsessoes == 2:
                    tupla= gerar_tupla(FILMES, SALAS)
                    if tupla == False:
                        print('Não foi possivel criar a tupla.')
                    else:
                        bool = listar_elementos_especifico_sessões(SESSOES,tupla)
                        if bool == False:
                            print('Não foi possivel encontrar a sessão desejada.')
                elif opsessoes == 3:
                    tupla = GerarSessão(FILMES,SALAS,SESSOES)
                    if tupla:
                        print('Sessão adicionada com sucesso!')
                        preco=add_preço(SESSOES,tupla)
                        if preco:
                            print('Preço adicionado com sucesso!')
                        else:
                            print('Não foi possível adicionar o preço.')
                    else:
                        print('Não foi possivel gerar sessão!')
                elif opsessoes == 4:
                    tupla = gerar_tupla(FILMES,SALAS)
                    preco = add_preço(SESSOES,tupla)
                    if preco == True:
                        print('Preço alterado!')
                    else:
                        print('Não foi possivel alterar o preço!')
                elif opsessoes == 5:
                    codigo = gerar_tupla(FILMES, SALAS)
                    remover = excluir_sessão(SESSOES,codigo)
                    if remover == True:
                        print(f'A sessão {codigo} foi excluida!')
                elif opsessoes==6:
                    print("Encerrando submenu de sessões.")
                    Menu_sessoes=False
                    gravar_sessoes(SESSOES)
                else:
                    print('Operação inválida, escolha uma opção entre 1 à 6.')
        elif operacao == 4: #abrirá o submenu de Relátorios
            print(f'Abrindo o SubMenu de Relátorios: ')
            Menu_relatorios = True
            while Menu_relatorios:
                oprelatorios = submenu_relatorios()
                if oprelatorios==1:
                    tipo_de_exibicao=input("Digite o tipo de exibição que deseja ver as informações da sala: ")
                    capacidade=int(input("Digite a capacidade da sala que deseja ver as informações: "))
                    listar_salas_cap_exib(SALAS,tipo_de_exibicao,capacidade)
                elif oprelatorios==2:
                    data_filme=int(input("Digite a data que deseja ver as informações dos filmes lançados a partir dela: "))
                    listar_filmes_data(FILMES, data_filme)
                elif oprelatorios==3:
                    print("Informe o intervalo de datas:")
                    data_inicio=obter_data()
                    data_fim=obter_data() 
                    listar_dados_sessões_data(SESSOES, FILMES, SALAS, data_inicio, data_fim)
                else:
                    print("Encerrando submenu de relátorios")
                    Menu_relatorios=False
        elif operacao==5: #encerrará o programa
            print("Encerrando programa...")
            Menu = False
        else: #caso digitado um número que não corresponde as operações válidas
            print("Operação inválida, escolha uma opção entre 1 à 5.")
main()