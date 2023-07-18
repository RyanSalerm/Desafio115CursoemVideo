def linhas(*txt, sit=0):
    mai = [txt]
    for c, v in enumerate(txt):
        if sit==1:
            print(f'{"-"*40}')
            print(f'{v.center(40)}  ')
        else:
            print(f'{v}  ')
    print(f'{"-"*40}')
def opcoes(op=0):
    linhas('MENU', sit=1)
    linhas('\033[0;32;1m1-\033[m \033[0;34;1mCadrastrar uma nova pessoa\033[m',
           '\033[0;32;1m2-\033[m \033[0;34;1mListar as pessoas cadastradas\033[m',
           '\033[0;32;1m3-\033[m \033[0;34;1mSair do programa\033[m')
    op = str(input('\033[0;32;1mSua opção: \033[m'))
    while op not in '123':
        print('\033[0;31;1mERRO. Digite um valor válido!\033[m')
        linhas('\033[0;32;1m1-\033[m \033[0;34;1mCadrastrar uma nova pessoa\033[m',
        '\033[0;32;1m2-\033[m \033[0;34;1mListas as pessoas cadastradas\033[m',
        '\033[0;32;1m3-\033[m \033[0;34;1mSair do programa\033[m')
        op = str(input('\033[0;32;1mSua opção: \033[m'))
    return op
