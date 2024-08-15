import os

restaurantes = [
    {'nome': 'Sushi da Mooca', 'categoria': 'Japonesa', 'ativo': False}, 
    {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True}, 
    {'nome': 'Feijoada do seu zé', 'categoria': 'Brasileira', 'ativo': False}
]

def exibir_nome_do_programa():
    '''Exibe o nome estilizado do programa na tela'''
    print('Bᴇᴍ ᴠɪɴᴅᴏ ᴀᴏ Radar Restaurante \n')

def exibir_opcoes():
    '''Exibe todas as opções do menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def finalizar_app():
    '''Limpa a tela e exibe a mensagem de finalização do aplicativo'''
    os.system('cls')
    exibir_subtitulo('Finalizando o app')
    
def voltar_ao_menu_principal():
    ''' Ao Apertar em qualquer tecla, volta ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main() 

def opcao_invalida():
    ''' É exibida uma mensagem de opção inválida e retorna ao menu principal
    
    Outputs: 
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    main()

def exibir_subtitulo(texto):
    ''' ao redor de asteriscos, é exibido a mensagem de texto de cada tela'''
    os.system('cls')
    linha = '*' * (len(texto) + 2)
    print(linha)
    print(f'{texto}')
    print(f'{linha}\n')

def cadastrar_novo_restaurante():
    ''' Função responsável pelo cadastro de novos restaurantes
    
    Inputs:
    -Nome do restaurante
    -Categoria do restaurante
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    main()

def alternar_estado_restaurante():
    ''' Função responsável por alterar o status do restaurante
    
    Inputs:
    -Nome do restaurante
    
    Outputs:
    Nome do Restaurante e a condição alterada
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input(f'Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Função para listar restaurantes
    
    Outputs:
    -Nome do restaurante
    -Categoria
    -Status
    '''
    exibir_subtitulo('Lista de restaurantes cadastrados até o momento: ')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'} \n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'. {nome_restaurante.ljust(20)} | categoria: {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()
    main()
    
def escolher_opcao():
    '''Solicita e executa a opção escolhida pelo usuário
    
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        print(f'Você escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''Função que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
