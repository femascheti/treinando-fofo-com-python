import os

treinos = [
    {'nome':'Tríceps pulley', 'categoria':'braço', 'ativo': False},
    {'nome':'Supino inclinad','categoria':'peito', 'ativo': True}, 
    {'nome':'Legpress', 'categoria':'perna','ativo': False},
]

def exibir_nome_programa():
    '''Link para gerador de fontes: https://fsymbols.com/pt/geradores/'''
    print("""
        ████████╗██████╗░███████╗██╗███╗░░██╗░█████╗░  ███████╗░█████╗░███████╗░█████╗░
        ╚══██╔══╝██╔══██╗██╔════╝██║████╗░██║██╔══██╗  ██╔════╝██╔══██╗██╔════╝██╔══██╗
        ░░░██║░░░██████╔╝█████╗░░██║██╔██╗██║██║░░██║  █████╗░░██║░░██║█████╗░░██║░░██║
        ░░░██║░░░██╔══██╗██╔══╝░░██║██║╚████║██║░░██║  ██╔══╝░░██║░░██║██╔══╝░░██║░░██║
        ░░░██║░░░██║░░██║███████╗██║██║░╚███║╚█████╔╝  ██║░░░░░╚█████╔╝██║░░░░░╚█████╔╝
        ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝░╚════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░░░░░╚════╝░
        """)

def exibir_opcoes():
    exibir_subtitulo('Escolha uma opção: \n')
    print('1. Cadastrar treino')
    print('2. Listar treinos')
    print('3. Ativar ou desativar treino')
    print('4. Sair do aplicativo \n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu():
    input('\nClique qualquer tecla para voltar para o menu principal ')
    main()

def cadastrar_treino():
    '''Essa função é responsável por cadastrar novos treinos
    
        Inputs:
        - Nome do treino (nome_do_treino)
        - Categoria do novo treino (categoria_treino)

        Outputs: 
        - Adiciona o treino criado na lista de treinos (treinos) 
    
    '''
    exibir_subtitulo('Cadastro de novos treinos')
    nome_do_treino = input('Digite o nome do treino que deseja cadastrar: ')
    categoria_treino = input(f'Digite o nome da categoria do treino {nome_do_treino}: ')
    dados_do_treino = {'nome':nome_do_treino, 'categoria':categoria_treino, 'ativo':False}
    treinos.append(dados_do_treino)
    print(f'O treino {nome_do_treino} foi cadastrado com sucesso!')
    voltar_menu()

def listar_treinos():
    '''Essa função é responsável por listar todos os treinos cadastrados

        Output: 
        - Lista treinos cadastrados no programa

    '''
    exibir_subtitulo('Listando treinos \n')
    
    print(f'{"Nome do treino".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for treino in treinos:
        nome_treino = treino['nome']
        categoria_treino = treino['categoria']
        ativo_treino = 'ativado' if treino['ativo'] else 'desativado'
        print(f'- {nome_treino.ljust(20)} | {categoria_treino.ljust(20)} | {ativo_treino}')
    
    voltar_menu()

def ativar_treino():
    '''Essa função é responsável por alternar os treinos cadastrados entre ativado e desativado

        Input:
        - Nome do treino cadastrado

        Output: 
        - Alternança entre ativado e desativado

    '''
    exibir_subtitulo('Ativar treino')

    nome_treino = input('Digite o nome do treino que deseja ativar ou desativar: ')
    treino_encontrado = False

    for treino in treinos:
        if nome_treino == treino['nome']:
            treino_encontrado = True
            treino['ativo'] = not treino['ativo']
            mensagem = f'O treino {nome_treino} foi ativado com sucesso' if treino['ativo'] else f'O treino {nome_treino} foi desativado com sucesso'
            print(mensagem)
    if not treino_encontrado:
        print('O treino não foi encontrado')

    voltar_menu()


def finalizar_app():
    exibir_subtitulo('Encerrando')

def opcao_invalida():
    exibir_subtitulo('Essa opção não é válida!')
    voltar_menu()

def escolher_opcao():
    '''Esta função verifica a opção selecionada pelo usuário e direciona para a função correspondente
    
        Inputs:
        - Opcão escolhida em formato numérico 

        Outputs:
        - Função cadastrar treino, se selecionado a opção 1
        - Função listar treinos cadastrados, se selecionado a opção 2
        - Função ativar treinos cadastrados, se selecionado a opção 3
        - Função finalizar aplicação, se selecionado a opção 4
        - Função opção inválida, se for selecionado qualquer outra opção que não listada anteriormente

    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_treino()
            case 2:
                listar_treinos()
            case 3:
                ativar_treino()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except: 
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()