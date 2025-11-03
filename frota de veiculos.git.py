def menu():
    print('-='*30)
    print('Frota de Veiculos'.center(60))
    print('-='*30)
    print('-='*30)
    print('Menu Interativo'.center(60))
    print('-='*30)

    while True:
        try:
            consultar=int(input('1-Cadastrar veículo\n2-Consultar os veículos disponíveis\n3-Visualizar veículos econômicos\n4-Consultar lista de veículos por kilometragem (Km)'))

        except ValueError:
            print('Digite somente números inteiros!')
            continue

        if consultar == 1:
            cadastro()

        elif consultar == 2:
            mostrar_todos()



carros=[]
def cadastro():
    while True:
        marca=str(input('Digite a marca do veículo: '))
        if not marca.replace(' ',"").isalpha():
            print('Digite apenas letras !')
            continue
        else:
            break

    while True:
        modelo = str(input('Digite o modelo do veículo:'))
        if not modelo.replace(' ',"").isalpha():
            print('Digite apenas letras !')
            continue

        else:
                break
    ano=0
    while True:
        try:
            ano=int(input('Digite o ano do moedelo:'))

        except ValueError:
            print('Digite apenas números inteiros! !')
            continue

        else:
            break

    while True:
        try:
            kilometragem=float(input('Digite quantos Km rodados:'))

        except ValueError:
            print('Digite apenas números !')

        else:
            break

    capacidade_tanque=0
    while True:
        try:
            capacidade_tanque= int(input('Qual a capacidade total do tanque de combustível? (litros)'))

        except ValueError:
            print('Digite apenas números !')
            continue

        else:
            break

    consumo_cidadeg=0
    consumo_estradag=0
    consumo_cidadeet=0
    consumo_estradaet=0
    while True:
        try:
            consumo_cidadeg = float(input('Qual o consumo de combustível (Gasolina) na cidade? '))
            consumo_estradag = float(input('Qual o consumo de combustível (Gasolina na estrada? '))
            consumo_cidadeet=float(input('Qual o consumo de combustível(Etanol) na cidade? '))
            consumo_estradaet=float(input('Qual o consumo de combustível (Etanol) na estrada?'))


        except ValueError:
            print('Digite apenas números !')
            continue

        else:
            break

    autonomia_cidadeg=consumo_cidadeg*capacidade_tanque
    autonomia_estradag=consumo_estradag*capacidade_tanque
    autonomia_cidadeet=consumo_cidadeet*capacidade_tanque
    autonomia_estradaet=consumo_estradaet*capacidade_tanque

    carros.append({'marca': marca,
                   'modelo': modelo,
                   'ano': ano,
                   'kilometragem': kilometragem,
                   'capacidade_tanque': capacidade_tanque,
                   'consumo gasolina cidade':consumo_cidadeg,
                   'consumo gasolina estrada':consumo_estradag,
                   'consumo et cidade':consumo_cidadeet,
                   'consumo et estrada':consumo_estradaet,
                   'autonomia gasolina cidade':autonomia_cidadeg,
                   'autonomia gasolina estrada':autonomia_estradag,
                   'autonomia etanol estrada':autonomia_estradaet,
                   'autonomia etanol cidade':autonomia_cidadeet,})

    print('Cadastro concluído com sucesso!')


    while True:
        continuar=str(input('Deseja cadastrar outro carro?')).lower().strip()
        if continuar in ['s','sim']:
            return

        elif continuar in ['n','nao','não']:
            break

        else:
            print('Resposta incorreta!')
            continue

def mostrar_todos():
    if not carros:
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

menu()


def km_rodado():
    km_rodado=


#Impede números negativos:
while True:
    try:
        numero = float(input("Digite um número positivo: "))
        if numero < 0:
            print("⚠️ Digite apenas números positivos!")
            continue
        break
    except ValueError:
        print("⚠️ Entrada inválida! Digite apenas números.")
