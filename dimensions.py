#Função das dimensões
def dimensoesObjeto():
    while True:
        try:
            altura = int(input('Digite a altura (cm):'))
            comprimento = int(input('Digite o comprimento (cm):'))
            largura = int(input('Digite a largura (cm):'))

            volume = altura*comprimento*largura

            print('\n',volume)

            break

        except ValueError:
            print('Digite APENAS valores numéricos! Tente novamente')

#Função peso
def pesoObjeto():
    while True:
        try:
            peso = float(input('Informe o peso do objeto (kg):'))
            if peso <= 0.1:
                return 1

            elif peso > 0.1 or peso <= 1:
                return 1.5

            elif peso > 1 or peso <= 10:
                return 2

            elif peso > 10 or peso <= 30:
                return 3

            else:
                print('Peso não aceito! Tente novamente')
                continue

        except ValueError:
            print('Digite APENAS valores numéricos! Tente novamente')

#Função da rota
def rotaObjeto():
    rota = input('Informe a rota desejada:\n'
                 'RS - Rio de Janeiro até São Paulo\n'
                 'SR - São Paulo até Rio de Janeiro\n'
                 'BS - Brasília até São Paulo')
    if rota == 'RS':
        return 1

    elif rota == 'SR':
        return 1

    elif rota == 'BS':
        return 1.2

    else:
        print('Essa rota não existe! Digite novamente')

#Programa principal
while True:

    global volume

    print('Digite um dos seguintes números para escolher a opção desejada:\n')
    escolha = int(input('Escolha uma opção:\n'
                        '1 - Calcular o volume do objeto\n'
                        '2 - Calcular o peso do objeto\n'
                        '3 - Calcular a rota do objeto\n'
                        '4 - Sair do programa\n'))

    if escolha == 1:
        dimensoesObjeto()

    elif escolha == 2:
        pesoObjeto()

    elif escolha == 3:
        rotaObjeto()

    elif escolha == 4:
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida! Tente novamente')
