def arquivoExiste(nome_arquivo):
    try:
        with open(nome_arquivo, 'rt') as arquivo:
            return True
    except FileNotFoundError:
        return False

def criarArquivo(nome_arquivo):
    if not arquivoExiste(nome_arquivo):
        with open(nome_arquivo, 'wt+') as arquivo:
            arquivo.write("Inicializando o arquivo\n")

arquivo = "sistema.txt"
criarArquivo(arquivo)

def cadrastrar(cont, nome, idade):
    with open("sistema.txt", "a") as arquivo:
        arquivo.write(f'{cont};{nome};{idade}\n')
