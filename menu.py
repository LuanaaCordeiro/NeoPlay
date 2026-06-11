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
        0 - sair do sistema
        Escolha uma opção: '''
    return texto

def adicionarJogo(jogos, id_jogo, nome, genero, preco, idioma, plataforma, desenvolvedora):
    jogo = {'id_jogo': id_jogo, 'nome' : nome, 'genero' : genero, 'preco' : preco, 
            'idioma': idioma, 'plataforma' : plataforma, 'desenvolvedora': desenvolvedora}
    jogos.append(jogo)

def listarJogos(jogos):

    for jogo in jogos:
        print("Id: {}".format(jogo['id_jogo']))
        print("Nome: {}".format(jogo['nome']))
        print("Gênero: {}".format(jogo['genero']))
        print("Preço: {}".format(jogo['preco']))
        print("Idioma: {}".format(jogo['idioma']))
        print("Plataforma: {}".format(jogo['plataforma']))
        print("Desenvolvedora: {}".format(jogo['desenvolvedora']))
        print('')


opcao = 1
jogos = []
while opcao != 0:
    opcao = int(input(mostrarMenu()))
  

    if opcao == 1:
        print("Adicione um jogo")
        id_jogo = int(input("Digite o id do jogo: "))
        nome = input("Digite o nome do jogo: " )
        genero = input("Digite o genero do jogo: ")
        preco = float(input("Digite o preço do jogo: "))
        idioma = input("Digite o idioma do jogo: ")
        plataforma = input("Digite a plataforma do jogo: ")
        desenvolvedora = input("Digite a desenvolvedora do jogo: ")

        adicionarJogo(jogos, id_jogo,nome,genero,preco,idioma,plataforma,desenvolvedora)
        
    elif opcao == 2:
        print("Buscar pessoa")
    elif opcao == 3:
        print("Jogos listados")
        listarJogos(jogos)

    elif opcao == 4:
        print("Atualizar uma pessoa")
    elif opcao == 5:
        print("Excluir uma pessoa")
    elif opcao == 0:
        print("Sair do sistema")
    else:
        print("Opção Inválida \nDigite novamente")

