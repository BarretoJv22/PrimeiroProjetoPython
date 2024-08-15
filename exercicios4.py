# ex1:
dicionario_pessoa = {
    'nome': 'João Victor',
    'idade': 22,
    'cidade': 'São Paulo'
}
# ex2:
# 2 a)dicionario_pessoa['idade'] = 23
# 2 b)dicionario_pessoa['profissão'] = 'Estudante'
# 2 c)dicionario_pessoa.pop('cidade')

# ex3:
numeros_e_seus_quadrados = {x: x**2 for x in range(1,6)}
print(numeros_e_seus_quadrados)

# ex 4:
if 'nome' in dicionario_pessoa:
    print("A chave 'nome' existe no dicionário")
else:
    print("Essa chave não existe")
    
# ex 5:

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(contagem_palavras)