#ex 1:
numeros = [1, 2, 3 ,4 ,5 ,6 ,7 ,8, 9 ,10]
nomes = ['João', 'Maria', 'José', 'Mayara']
anos = [2002, 2024]

# ex2:
# for numero in numeros:
#     print(f'{numero}')


# ex3:
# soma_numero = 0
# for numero in numeros:
#     if numero %2 > 0:
#         soma_numero = soma_numero + numero
#         print(f'- {soma_numero}')

# ex4:
# for numero in range(len(numeros), 0, -1):
#     print(numero)

# ex5:
# def multiplicar_numero(numero):
#     for i in range(1, 11, 1):
#         print(f'{i} - {numero} x {i} = {i*numero}')
        
# multiplicar_numero(10)

# ex6:
# soma_numeros = 0
# try:
#     for numero in numeros:
#         soma_numeros += numero
#         print(f'{soma_numeros}')
# except Exception as e:
#     print(f'{e}')

# ex7:
# notas = [8, 10]
# soma_notas = 0
# try:
#     for nota in notas:
#         soma_notas += nota
#     media = soma_notas / len(notas)
#     print(media)
# except:
#     print('Lista vazia')