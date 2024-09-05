msg = """
    -----------------------
    --Super Simulator------
    -----------------------
    Menu
    1-Novo jogo
    2-Carregar jogo
    3-Opções
    4-Sair
"""
menu = int(input(msg))

match menu:
    # case 1:
    #     print('Bem vindo....')
    # case 2:
    #     print('Continuando jogo')
    case 1 | 2:
        print('jogando do mesmo jeito')
    case 3:
        print('Opções do jogo')
    case 4:
        print('Sair')
    case _:
        print('Valor invalido')
