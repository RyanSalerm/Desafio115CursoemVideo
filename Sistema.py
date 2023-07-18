from Menu import opcoes
from ArquivosTXT import cadrastrar
from prints import escreva
sistema = list()
pessoa = {}

while True:
    op = opcoes()
    if op in '3':
        break
    elif op in '1': # cadastrar uma pessoa
        pessoa = {}
        nome = str(input('Nome: ')).strip()
        idade = str(input('Idade: ')).strip()
        while not idade.isnumeric():
            print(f'\033[0;32;1mERRO. Digite um número válido!\033[m')
            idade = str(input('Idade: '))
        cont = escreva(True) + 1
        cadrastrar(cont, nome, idade)
        pessoa = {'Cod': cont, 'Nome': nome, 'Idade': int(idade)}
        sistema.append(pessoa)
    elif op in '2': # exibir a lista
        escreva(False)
