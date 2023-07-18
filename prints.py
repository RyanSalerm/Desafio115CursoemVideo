def escreva(quant=False):
    sistema = list()
    with open("sistema.txt", "rt") as arquivo:
        for linha in arquivo:
            cont, nome, idade = linha.strip().split(";")
            pessoa = {
                'Cod': cont,
                'Nome': nome,
                'Idade': idade
            }
            sistema.append(pessoa)
    if quant:
        return len(sistema)
    else:
        print(f'{"Cod":<5}{"Nome":<40}{"Idade":<10}')
        for pessoa in sistema:
            d, e, f = pessoa.values()
            print(f'{d:<5}{e:<40}{f:<10}')
        print()

