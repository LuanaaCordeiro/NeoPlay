#Menu inicial de NeoPlay
def mostrarMenu():
    texto = '''
        **************************************************
        *********NeoPlay - Loja de Jogos Digitais*********
        **************************************************
        1 - adicionar um jogo
        2 - buscar um jogo
        3 - listar os jogos
        4 - atualizar um jogo
        5 - excluir um jogo
        6 - filtrar jogos
        0 - sair do sistema
        Escolha uma opção: '''
    return texto

#Função chamada ao escolher a opção 1, com a finalidade de adicionar um jogo
def adicionarJogo(jogos, id_jogo, nome, genero, preco, idioma, plataforma, desenvolvedora):
    jogo = {
        'id_jogo': id_jogo,
        'nome': nome,
        'genero': genero,
        'preco': preco,
        'idioma': idioma,
        'plataforma': plataforma,
        'desenvolvedora': desenvolvedora
    }

    jogos.append(jogo)

#Função chamada ao escolher a opção 2, com a finalidade de buscar um jogo específico por ID
def buscarJogo(jogos, busca):
    if len(jogos) == 0:
        print("Nenhum jogo cadastrado")
        return

    for jogo in jogos:
        if busca == jogo['id_jogo']:
            print("Id: {}".format(jogo['id_jogo']))
            print("Nome: {}".format(jogo['nome']))
            print("Gênero: {}".format(jogo['genero']))
            print("Preço: {}".format(jogo['preco']))
            print("Idioma: {}".format(jogo['idioma']))
            print("Plataforma: {}".format(jogo['plataforma']))
            print("Desenvolvedora: {}".format(jogo['desenvolvedora']))
            return

    print("Jogo não encontrado")

#Função chamada ao escolher a opção 3, com a finalidade de listar todos os jogos cadastrados e seus respectivos campos
def listarJogos(jogos):
    if len(jogos) == 0:
        print("Nenhum jogo cadastrado")
        return

    for jogo in jogos:
        print("Id: {}".format(jogo['id_jogo']))
        print("Nome: {}".format(jogo['nome']))
        print("Gênero: {}".format(jogo['genero']))
        print("Preço: {}".format(jogo['preco']))
        print("Idioma: {}".format(jogo['idioma']))
        print("Plataforma: {}".format(jogo['plataforma']))
        print("Desenvolvedora: {}".format(jogo['desenvolvedora']))
        print("")

#Função chamada ao escolher a opção 4, com a finalidade de receber um ID e atualizar os campos relacionados ao ID escolhido
def atualizarJogo(jogos, busca, nome, genero, preco, idioma, plataforma, desenvolvedora):
    if len(jogos) == 0:
        print("Nenhum jogo cadastrado")
        return

    for jogo in jogos:
        if busca == jogo['id_jogo']:
            jogo['nome'] = nome
            jogo['genero'] = genero
            jogo['preco'] = preco
            jogo['idioma'] = idioma
            jogo['plataforma'] = plataforma
            jogo['desenvolvedora'] = desenvolvedora
            return

    print("Jogo não encontrado")

#Função chamada ao escolher a opção 5, com a finalidade de receber um ID e excluir o jogo relacionado a esse ID
def excluirJogo(jogos, busca):
    if len(jogos) == 0:
        print("Nenhum jogo cadastrado")
        return

    for jogo in jogos:
        if busca == jogo['id_jogo']:
            jogos.remove(jogo)
            return

    print("Jogo não encontrado")

#Função chamada ao escolher a opção 6, com a finalidade de buscar o jogo relacionado ao filtro escolhido pelo usuário, seja
#ele de gênero, plataforma ou desenvolvedora
def filtrarJogos(jogos, opcaoFiltro, valor):
    if len(jogos) == 0:
        print("Nenhum jogo cadastrado")
        return

    encontrou = False

    for jogo in jogos:

        if opcaoFiltro == 1 and jogo['genero'].lower() == valor.lower():
            encontrou = True

        elif opcaoFiltro == 2 and jogo['desenvolvedora'].lower() == valor.lower():
            encontrou = True

        elif opcaoFiltro == 3 and jogo['plataforma'].lower() == valor.lower():
            encontrou = True

        elif opcaoFiltro == 4 and jogo['idioma'].lower() == valor.lower():
            encontrou = True

        elif opcaoFiltro == 5 and jogo['nome'].lower() == valor.lower():
            encontrou = True

        else:
            continue

        print("Id: {}".format(jogo['id_jogo']))
        print("Nome: {}".format(jogo['nome']))
        print("Gênero: {}".format(jogo['genero']))
        print("Preço: {}".format(jogo['preco']))
        print("Idioma: {}".format(jogo['idioma']))
        print("Plataforma: {}".format(jogo['plataforma']))
        print("Desenvolvedora: {}".format(jogo['desenvolvedora']))
        print("")

    if encontrou == False:
        print("Nenhum jogo encontrado")

#Função responsável por salvar os dados no arquivo .txt, garantindo que os jogos fiquem salvos localmente
def salvarDados(jogos):
    dados = open("jogos.txt", 'w')

    for jogo in jogos:
        dados.write("{};".format(jogo['id_jogo']))
        dados.write("{};".format(jogo['nome']))
        dados.write("{};".format(jogo['genero']))
        dados.write("{};".format(jogo['preco']))
        dados.write("{};".format(jogo['idioma']))
        dados.write("{};".format(jogo['plataforma']))
        dados.write("{}\n".format(jogo['desenvolvedora']))

    dados.close()

#Função responsável por ler os dados que estão salvos no arquivo .txt
def lerDados(jogos):
    id_jogo = 1
    dados = open("jogos.txt", 'r')
    linhas = dados.readlines()

    for linha in linhas:
        if linha.strip() == "":
            continue

        palavras = linha.split(';')

        jogo = {}
        jogo['id_jogo'] = int(palavras[0])
        id_jogo = int(palavras[0])
        jogo['nome'] = palavras[1]
        jogo['genero'] = palavras[2]
        jogo['preco'] = float(palavras[3])
        jogo['idioma'] = palavras[4]
        jogo['plataforma'] = palavras[5]
        jogo['desenvolvedora'] = palavras[6].strip()

        jogos.append(jogo)

    return id_jogo + 1


opcao = 1
jogos = []

cont = lerDados(jogos)

while opcao != 0:

    opcao = int(input(mostrarMenu()))

    if opcao == 1:

        print("Adicionar jogo")

        nome = input("Digite o nome do jogo: ")
        genero = input("Digite o gênero do jogo: ")
        preco = float(input("Digite o preço do jogo: "))
        idioma = input("Digite o idioma do jogo: ")
        plataforma = input("Digite a plataforma do jogo: ")
        desenvolvedora = input("Digite a desenvolvedora do jogo: ")

        if nome == "":
            print("Nome inválido")

        elif preco < 0:
            print("Preço inválido")

        else:
            adicionarJogo(
                jogos,
                cont,
                nome,
                genero,
                preco,
                idioma,
                plataforma,
                desenvolvedora
            )

            cont = cont + 1

    elif opcao == 2:
        print("Buscar jogo")
        busca = int(input("Digite o id do jogo: "))
        buscarJogo(jogos, busca)

    elif opcao == 3:
        listarJogos(jogos)

    elif opcao == 4:
        print("Atualizar um jogo")

        busca = int(input("Digite o id do jogo para ser atualizado: "))

        nome = input("Digite o nome do jogo: ")
        genero = input("Digite o gênero do jogo: ")
        preco = float(input("Digite o preço do jogo: "))
        idioma = input("Digite o idioma do jogo: ")
        plataforma = input("Digite a plataforma do jogo: ")
        desenvolvedora = input("Digite a desenvolvedora do jogo: ")

        if nome == "":
            print("Nome inválido")

        elif preco < 0:
            print("Preço inválido")

        else:
            atualizarJogo(
                jogos,
                busca,
                nome,
                genero,
                preco,
                idioma,
                plataforma,
                desenvolvedora
            )

    elif opcao == 5:

        print("Excluir um jogo")

        busca = int(input("Digite o id do jogo para ser excluído: "))
        excluirJogo(jogos, busca)

    elif opcao == 6:

        print("1 - Filtrar por gênero")
        print("2 - Filtrar por desenvolvedora")
        print("3 - Filtrar por plataforma")
        print("4 - Filtrar por idioma")
        print("5 - Filtrar por nome")

        opcaoFiltro = int(input("Escolha uma opção: "))
        valor = input("Digite o valor da busca: ")

        filtrarJogos(jogos, opcaoFiltro, valor)

    elif opcao == 0:

        salvarDados(jogos)
        print("Saindo do Sistema")

    else:
         print("Opção Inválida \nDigite novamente")

