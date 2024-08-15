# # ex 1
# def verifica_numero_par():
#     numero_escolhido = int(input(f'Digite um número: '))
#     if numero_escolhido % 2 == 0:
#         print(f'O número {numero_escolhido} é par!')
#     else:
#         print(f'O número {numero_escolhido} é impar!')
# verifica_numero_par()

# ex 2

# def classificar_idade():
#     idade = int(input(f'Digite sua idade: '))
#     if 0<= idade < 13:
#         print('Você é criança')
#     elif 13 <= idade <18:
#         print('Você é adolescente')
#     elif 18 <= idade < 60:
#         print('Você é adulto(a)')
#     else:
#         print('Você é idoso(a)')

# classificar_idade()


# ex 3

# def login():
#     nome_usuario = input('Digite seu nome de usuário: ')
#     senha = input('Digite sua senha: ')
#     if nome_usuario == 'joao' and senha == '123':
#         print(f'Seja bem-vindo {nome_usuario}')
#     else:
#         print('Usuário e/ou senha inválidos')

# login()


# ex 4

def determinar_coordenadas():
    x = int(input('Insira a coordenada x:'))
    y = int(input('Insira a coordenada y:'))
    if x > 0 and y > 0:
        print('Você está no primeiro quadrante')
    elif x < 0 and y > 0:
        print('Você está no segundo quadrante')
    elif x < 0 and y < 0:
        print('Você está no terceiro quadrante')
    elif x > 0 and y < 0:
        print('Você está no quarto quadrante')
    else:
        print('o ponto está localizado no eixo ou origem')
        
determinar_coordenadas()
