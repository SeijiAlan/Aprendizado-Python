carros=[]
def menu(): #O programa é controlado com base nessa função 
    print('-='*30)
    print('Frota de Veiculos'.center(60))
    print('-='*30)
    print('-='*30)
    print('Menu Interativo'.center(60))
    print('-='*30)

    while True: #O loop contém um mecanismo de validação de dados garantindo que o usuário realmente escolha uma função real
        try:
            consultar=int(input('1-Cadastrar veículo\n2-Consultar os veículos disponíveis\n3-Visualizar veículos econômicos\n4-Consultar lista de veículos por kilometragem (Km)'))

        except ValueError:
            print('Digite somente números inteiros!')   #O Try/except ValueError garante que apenas números inteiros serão digitados 
            continue

        if consultar == 1:
            cadastro()

        elif consultar == 2:
            mostrar_todos()

def cadastro():
    # A função cadastro() é responsável por coletar e validar todas as informações sobre o veículo
    # Cada campo possui seu próprio loop de validação garantindo a integridade dos dados inseridos

    while True:
        marca = str(input('Digite a marca do veículo: '))
        if not marca.replace(' ', "").isalpha():
            print('Digite apenas letras !')
            continue
        else:
            break

    while True:
        modelo = str(input('Digite o modelo do veículo:'))
        if not modelo.replace(' ', "").isalpha():           
            print('Digite apenas letras !')
            continue
        else:
            break

    # Validação do ano do modelo - impede valores negativos e entradas não numéricas
    while True:
        try:
            ano = int(input('Digite o ano do modelo: '))
            if ano < 0:
                print('Digite apenas números inteiros positivos!')
                continue
            break
        except ValueError:
            print('Digite apenas números inteiros!')
            continue

    # Validação da kilometragem - impede valores negativos e caracteres inválidos
    while True:
        try:
            kilometragem = float(input('Digite quantos Km rodados: '))
            if kilometragem < 0:
                print('Digite apenas números positivos!')
                continue
            break
        except ValueError:
            print('Digite apenas números!')

    # Validação da capacidade do tanque - impede valores negativos e letras
    while True:
        try:
            capacidade_tanque = int(input('Qual a capacidade total do tanque de combustível? (litros) '))
            if capacidade_tanque < 0:
                print('Digite apenas números inteiros positivos!')
                continue
            break
        except ValueError:
            print('Digite apenas números!')
            continue

    # Essa função criada contém um método de validação de dados que impede a inserção de números negativos
    # e evita repetição de código em múltiplos inputs (método que será utilizado na próxima versão do script)
    
    def validar_numero_positivo(mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                if valor < 0:
                    print("Digite apenas números positivos!")
                    continue
                return valor
            except ValueError:
                print("Digite apenas números válidos!")

    # Entradas com validação reutilizando a função acima
    consumo_cidadeg = validar_numero_positivo('Consumo Gasolina na cidade: ')
    consumo_estradag = validar_numero_positivo('Consumo Gasolina na estrada: ')
    consumo_cidadeet = validar_numero_positivo('Consumo Etanol na cidade: ')
    consumo_estradaet = validar_numero_positivo('Consumo Etanol na estrada: ')

    # Cálculo automático das autonomias (cidade e estrada para Gasolina e Etanol)
    autonomia_cidadeg = consumo_cidadeg * capacidade_tanque
    autonomia_estradag = consumo_estradag * capacidade_tanque
    autonomia_cidadeet = consumo_cidadeet * capacidade_tanque
    autonomia_estradaet = consumo_estradaet * capacidade_tanque

    # Armazena os dados do veículo em um dicionário e adiciona à lista principal "carros"
    carros.append({
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'kilometragem': kilometragem,
        'capacidade_tanque': capacidade_tanque,
        'consumo gasolina cidade': consumo_cidadeg,
        'consumo gasolina estrada': consumo_estradag,
        'consumo et cidade': consumo_cidadeet,
        'consumo et estrada': consumo_estradaet,
        'autonomia gasolina cidade': autonomia_cidadeg,
        'autonomia gasolina estrada': autonomia_estradag,
        'autonomia etanol estrada': autonomia_estradaet,
        'autonomia etanol cidade': autonomia_cidadeet
    })

    print('Cadastro concluído com sucesso!')

    # Mecanismo de controle para cadastrar novos veículos ou encerrar a operação
    while True:
        continuar = str(input('Deseja cadastrar outro carro? [S/N] ')).lower().strip()
        if continuar in ['s', 'sim']:
            return cadastro()  # Reinicia o cadastro
        elif continuar in ['n', 'nao', 'não']:
            break
        else:
            print('Resposta incorreta!')
            continue

def mostrar_todos():
    if not carros:    #Se não houver carro cadastrado o programa exibe a mensagem do print e sai dessa função, retornando ao menu(), função que se encontrao no final do arquivo.
        print('Nenhum carro cadastrado!')
        return

    for carro in carros:
        print(f"Marca: {carro['marca']}\n"
              f"Modelo: {carro['modelo']}\n"
              f"Ano: {carro['ano']}\n"
              f"Kilometragem: {carro['kilometragem']}\n"
              f"Capacidade total do tanque de combustível: {carro['capacidade_tanque']} litros\n"
              f"Consumo de combustível na cidade (Gasolina):{carro['consumo gasolina cidade']} Km/l\n"
              f"Consumo de combustível na estrada (Gasolina): {carro['consumo gasolina estrada']} Km/l\n"
              f"Autonomia (Cidade-Gasolina): {carro['autonomia gasolina cidade']} Km\n"
              f"Autonomia (Estrada-Gasolina): {carro['autonomia gasolina estrada']} Km\n"
              f"Autonomia (Cidade-Etanol): {carro['autonomia etanol cidade']} Km\n"
              f"Autonomia (Estrada-Etanol): {carro['autonomia etanol estrada']} Km\n")

menu() #Função no final do arquivo faz com que o programa se inicie a partir dela mesma



