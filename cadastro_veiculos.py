<<<<<<< HEAD
import json #Biblioteca para manipular arquivos no formato Json (Armazena e le dados de forma estruturada)

#----- Classe que representa um veículo da frota e calcula sua autonomia -----

class Carro:
    #Inicialização: Atributos do carro
    def __init__(self,marca,modelo,ano,versao,codigo,kilometragem,capacidade_tanque,consumo_cidade_g,consumo_estrada_g,consumo_cidade_e,consumo_estrada_e):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.versao=versao
        self.codigo=codigo
        self.kilometragem=kilometragem
        self.capacidade_tanque=capacidade_tanque
        self.consumo_cidade_g=consumo_cidade_g
        self.consumo_estrada_g=consumo_estrada_g
        self.consumo_estrada_e=consumo_estrada_e
        self.consumo_cidade_e=consumo_cidade_e

    #Calcula autonomia na cidade e estrada (Gasolina)
    def autonomia_gasolina(self):
        return {
            'cidade': self.consumo_cidade_g*self.capacidade_tanque,
            'estrada': self.consumo_estrada_g*self.capacidade_tanque
        }

    #Calcula a autonomia na cidade/estrada (Etanol)
    def autonomia_etanol(self):
        return {
            'cidade': self.consumo_cidade_e*self.capacidade_tanque,
            'estrada': self.consumo_estrada_e*self.capacidade_tanque
        }
    #Exibe as informações de um veículo formatadas
    def exibir_dados(self):
        autonomia_g=self.autonomia_gasolina()
        autonomia_e=self.autonomia_etanol()
        return (f"\nMarca:{self.marca}\nModelo {self.modelo}\nAno:{self.ano}\nVersão:{self.versao}\nCódigo:{self.codigo}\n"
                f"Consumo cidade/estrada (gasolina):{self.consumo_cidade_g}/{self.consumo_estrada_g} km/l\n"
                f"Consumo cidade/estrada (etanol):{self.consumo_cidade_e}/{self.consumo_estrada_e} km/l\n"
                f"Capacidade do tanque:{self.capacidade_tanque} litros\n"
                f"Kilometragem:{self.kilometragem:.3f} KM\n"
                f"Autonomia cidade/estrada (Gasolina):{autonomia_g['cidade']:.2f}/{autonomia_g['estrada']:.2f}\n"
                f"Autonomia cidade/estrada (Etanol):{autonomia_e['cidade']:.2f}/{autonomia_e['estrada']:.2f}\n")


#----- Métodos estáticos de validação de dados, evita repetição de código (Função de apoio) -----

    #Impede que números sejam fornecidos, faz com que apenas letras sejam aceitas
    @staticmethod
    def validar_texto(mensagem):
        while True:
            valor=str(input(mensagem)).strip().title()
            if valor.replace(' ', "").isalpha():
                return valor
            print ("Digite apenas letras !")

    #Impede a inserção de números negativos, permite números decimais e inteiros
    @staticmethod
    def validar_numero_positivo(mensagem):
        while True:
            try:
                valor = float(input(mensagem).strip())
                if valor < 0:
                    print("⚠️ Digite um número positivo!")
                    continue
                return valor
            except ValueError:
                print("⚠️ Digite apenas números! (Use ponto para decimais)")

    #Permite apenas números inteiros, além de impedir números negativos
    @staticmethod
    def validar_numero_inteiro(mensagem):
        while True:
            try:
                valor = int(input(mensagem).strip())
                if valor < 0:
                    print('Digite apenas números inteiros positivos !')
                    continue
                return valor

            except ValueError:
                print("Digite apenas números !")

#Função que carrega os dados salvos do arquivo Json
def carregar_dados():
    try:
        with open("frota_de_veiculos.json", "r",encoding="utf-8") as arquivo:
            dados=json.load(arquivo)
            return [Carro(**carro) for carro in dados]
    except FileNotFoundError:
        return []

#Função que salva os dados atuais da lista de carros
def salvar_dados(carros):
    with open("frota_de_veiculos.json", "w", encoding="utf-8") as arquivo:
        json.dump([carro.__dict__ for carro in carros], arquivo, ensure_ascii=False, indent=4)


#----- Classe que representa a frota de veículos  -----
class Frota_Veiculos():
    def __init__(self):
        # Os dados salvos em JSON são carregados como dicionários, mas o programa trabalha com objetos da classe Carro.
        # Por isso, é necessário converter novamente os dicionários em objetos da classe.
        # O operador (**) desempacota cada chave/valor do dicionário e envia como argumento nomeado para o construtor da classe Carro.
        # Exemplo: Carro(**carro)
        self.carros = carregar_dados()


    #Função cadastro: Momento em que todas as informações sobre um veículos são fornecidas, cada característica do carro determinada na classe Carro possui um método de validação.
    #O que não tem método de validação aceita números e letras
    def cadastro_carros(self):
        print("Cadastro de veículo")
        marca=Carro.validar_texto("Digite a marca do veículo:")
        modelo=input("Digite o modelo do veículo:").title().strip()
        ano=Carro.validar_numero_inteiro("Digite o ano do veículo:")
        versao=input(("Digite a versão do veículo:")).title().strip()
        codigo=Carro.validar_numero_inteiro("Atribuir código para cadastro: (Distingue modelos com informações semelhantes)")
        consumo_cidade_g=Carro.validar_numero_positivo("Digite o consumo na cidade (Gasolina):")
        consumo_estrada_g=Carro.validar_numero_positivo("Digite o consumo na estrada(Gasolina):")
        consumo_cidade_e=Carro.validar_numero_positivo("Digite o consumo na cidade (Etanol):")
        consumo_estrada_e=Carro.validar_numero_positivo("Digite o consumo na estrada:")
        kilometragem=Carro.validar_numero_positivo("Informe a Kilometragem:")
        capacidade_tanque=Carro.validar_numero_positivo("Informe a capacidade total do tanque (em litros)")

        novo_carro=Carro(marca,modelo,ano,versao,codigo,kilometragem,capacidade_tanque,consumo_cidade_g,consumo_estrada_g,consumo_cidade_e,consumo_estrada_e)

        self.carros.append(novo_carro)

        #Salva os dados cadastrados no arquivo json
        salvar_dados(self.carros)

        print("\n Carro cadastrado com sucesso !")

    #Mostra os dados de todos os carros cadastrados
    def mostrar_todos(self):
        if not self.carros:
            print("Nenhum carro cadastrado !")
            return

        print("Lista de veículos cadastrados:")
        for carro in self.carros:
            print(carro.exibir_dados())

    #Função que ordena os carros com base na kilometragem (Da menor para a maior)
    def kilometragem(self):
        if not self.carros:
            print("Nenhum carro cadastrado !")
            return

        else:
            percorridos=sorted(self.carros, key=lambda carro: carro.kilometragem)
            for carro in percorridos:
                print(carro.exibir_dados())

    #Função que exclui um carro conforme o código atribuido no cadastro
    def deletar_carro(self):
        if not self.carros:
            print("Nenhum carro cadastrado !")
            return

        else:
            codigo=Carro.validar_numero_inteiro("Informe o código do cadastro:")
            modelo=input ("Informe o modelo do carro constante no cadastro:").title().strip()
            ano=Carro.validar_numero_inteiro("Informe o ano do modelo:")

            deletar=[carro for carro in self.carros if carro.codigo==codigo and carro.modelo==modelo and carro.ano==ano] #Percorre cada carro da lista self.carros até achar o carro com o código correspondente ao informado
            if deletar:
                self.carros.remove(deletar[0]) #deletar[0] pega o primeiro e único elemento com o código informado em "deletar"
                salvar_dados(self.carros)
                print(f"Carro modelo:{modelo}, ano:{ano}, código:{codigo}, removido com sucesso !")

            else:
                print("Nenhum carro cadastrado com esse código !")


    #Menu principal do sistema
    def menu(self):
        while True:
            print('-=' * 30)
            print('Frota de Veículos'.center(60))
            print('-=' * 30)
            print('Menu Interativo'.center(60))
            print('-=' * 30)
            print('1 - Cadastrar veículo')
            print('2 - Mostrar carros cadastrados')
            print('3 - Consultar dados de forma individual')
            print('4 - Filtrar por kilometragem (Km) percorrida')
            print('5 - Deletar um carro cadastrado')
            print('6 - Sair')

            escolher=int(Carro.validar_numero_inteiro ("\nEscolha uma opção:"))

            if escolher == 1:
                self.cadastro_carros()

            elif escolher == 2:
                self.mostrar_todos()

            elif escolher == 3:
                #Verifica se existe pelo menos 1 carro cadastrado para continuar
                if not self.carros:
                    print("Nenhum carro cadastrado !")
                    continue

                else:#Se houver pelo menos 1 carro cadastrado, a execução da função prossegue
                    escolha_modelo=(Carro.validar_texto("\nInforme o modelo do veículo que deseja visualizar:"))
                    ano=(Carro.validar_numero_inteiro("\nInforme o ano do veículo:"))
                    modelo=[carro for carro in self.carros if carro.modelo==escolha_modelo and carro.ano==ano]

                    for carro in modelo:
                        print(carro.exibir_dados())

            elif escolher == 4:
                self.kilometragem()

            elif escolher == 5:
                self.deletar_carro()

            elif escolher == 6:
                print("Programa encerrado.")
                exit()

            else:
                print('⚠️ Opção inválida! Escolha um número de 1 a 5.\n')
                continue


if __name__ == "__main__":
    sistema = Frota_Veiculos()  # Instancia a classe
    sistema.menu()  # Chama o menu
=======
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



>>>>>>> 1b7a7eb409555255545608dfff3c7e1c5db01fc6
