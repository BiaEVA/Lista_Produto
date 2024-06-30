import locale

# Define a localidade para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

listaProduto = []

#---------- COMEÇO CADASTRAR PRODUTO ----------
def cadastrarProduto(cp):
    print('Você Selecionou a Opção de Cadastrar Produto!')
    print('O código do produto é: {}'.format(cp))
    nome = input('Por favor, entre com o nome do produto: ')
    fabricante = input('Por favor, entre com o fabricante do produto: ')
    try:
        valor = float(input('Por favor, entre com o valor do produto: '))
    except ValueError:
        print('Valor inválido. O valor deve ser um número.')
        return
    
    dicionarioProduto = {
        'Código': cp,
        'Nome': nome,
        'Fabricante': fabricante,
        'Valor': valor
    }
    listaProduto.append(dicionarioProduto.copy())
    print('Produto cadastrado com sucesso!')
#------------- FIM CADASTRAR PRODUTO-----------

#---------- COMEÇO CONSULTAR PRODUTO ----------
def consultarProduto():
    while True:
        try:
            print('Você Selecionou a Opção de Consultar Produtos!')
            opcaoC = int(input('Escolha a opção desejada:\n1 - CONSULTAR TODOS OS PRODUTOS\n'
                               '2 - CONSULTAR PRODUTO POR CÓDIGO\n'
                               '3 - CONSULTAR PRODUTO POR FABRICANTE\n'
                               '4 - RETORNAR\n'))
            if opcaoC == 1:
                print('---------------')
                for produto in listaProduto:
                    for key, value in produto.items():
                        if key == 'Valor':
                            value = locale.currency(value, grouping=True)
                        print('{}: {}'.format(key, value))
                    print('---------------')
            elif opcaoC == 2:
                print('---------------')
                entrada = int(input('Entre com o código do produto:\n'))
                produto_encontrado = False
                for produto in listaProduto:
                    if produto['Código'] == entrada:
                        for key, value in produto.items():
                            if key == 'Valor':
                                value = locale.currency(value, grouping=True)
                            print('{}: {}'.format(key, value))
                        produto_encontrado = True
                        print('---------------')
                if not produto_encontrado:
                    print('Produto não encontrado.')
            elif opcaoC == 3:
                print('---------------')
                entrada = input('Entre com o fabricante do produto:\n')
                fabricante_encontrado = False
                for produto in listaProduto:
                    if produto['Fabricante'] == entrada:
                        for key, value in produto.items():
                            if key == 'Valor':
                                value = locale.currency(value, grouping=True)
                            print('{}: {}'.format(key, value))
                        fabricante_encontrado = True
                        print('---------------')
                if not fabricante_encontrado:
                    print('Fabricante não encontrado.')
            elif opcaoC == 4:
                break
            else:
                print('Você escolheu uma opção que não existe. Tente novamente!')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
#------------ FIM CONSULTAR PRODUTO -----------

#------------ COMEÇO REMOVER PRODUTO ----------
def removerProduto():
    print('Você Selecionou a Opção de Remover Produto!')
    try:
        entrada = int(input('Entre com o código do produto:\n'))
    except ValueError:
        print('Código inválido. Deve ser um número.')
        return
    
    produto_removido = False
    for produto in listaProduto:
        if produto['Código'] == entrada:
            listaProduto.remove(produto)
            produto_removido = True
            print('Produto removido com sucesso!')
            break
    
    if not produto_removido:
        print('Produto não encontrado.')
#--------------- FIM REMOVER PRODUTO ----------

#------------ COMEÇO MAIN -------------------
print('Bem Vindo ao Controle de Estoque de produtos da Beatriz')
registroProduto = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n1 - CADASTRAR PRODUTO\n'
                          '2 - CONSULTAR PRODUTO\n'
                          '3 - REMOVER PRODUTO\n'
                          '4 - SAIR\n'))
        if opcao == 1:
            registroProduto += 1
            cadastrarProduto(registroProduto)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Programa Finalizado')
            break
        else:
            print('Você escolheu uma opção que não existe. Tente novamente!')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')
#------------ FIM MAIN -------------------
