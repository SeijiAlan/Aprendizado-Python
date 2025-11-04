from random import choice
#Classe que representa o jogador humano
class jogador:
    def __init__(self, nome,escolha):
        self.nome = nome
        self.escolha=escolha
    #Solicita que o jogador faça uma escolha dentre as 3 opções
    def fazer_escolha(self):
        self.escolha=str(input('Pedra,Papel ou Tesoura?')).title().strip()

    # Método estático para validar textos (aceita apenas letras)
    @staticmethod
    def validar_textos(mensagem):
        while True:
            valor=str(input(mensagem)).lower().strip()
            if not valor.replace(' ','').isalpha():
                print('Digite apenas letras')
                continue
            return valor

    # Método estático para validar números (aceita apenas valores positivos)
    @staticmethod
    def validar_numeros(mensagem):
        while True:
            try:
                valor=float(input(mensagem))
                if valor <0:
                    print('Digite apenas números positivos ! Use "."(Ponto final) para números decimais.')
                    continue
                return valor
            except ValueError:
                print('Digite apenas números !')

# Classe que representa o computador (adversário)
class computador:
    def __init__(self, aleatorio):
        self.aleatorio=aleatorio

    def escolha_aleatorioa(self):
        opcoes=["Pedra","Papel", "Tesoura"]
        self.aleatorio=choice(opcoes)


# Classe principal que controla o jogo Jokenpô
class jokenpô:
    #Mostra informações e regras do jogo
    def informacao(self):
        print("Jokenpô, também conhecido como pedra, papel e tesoura," 
              "é um jogo de mãos popular, originário do Japão, para duas ou mais pessoas, que usa três gestos para determinar o vencedor.\n"
              "É frequentemente usado para resolver conflitos e tomar decisões de forma justa, como escolher quem começa uma brincadeira.\n"
              "O jogo pode ser jogado de maneira casual, mas também há estratégias, baseadas na análise de padrões de comportamento dos oponentes.\n"
              "\nObjetivo: Derrotar o adversário com um dos três gestos: pedra (mão fechada), papel (mão aberta) ou tesoura (mão com os dedos indicador e médio esticados).\n"
              "Combinações: Pedra vence tesoura (a pedra quebra a tesoura).\n"
              "Tesoura vence papel (a tesoura corta o papel).\n"
              "Papel vence pedra (o papel cobre a pedra).\n"
              "O que fazer em caso de empate: Se houver empate, a disputa é repetida até que um vencedor seja determinado.(Gerado por Google IA")

    #Lógica principal do jogo
    def jogar(self):
        while True:
            player = jogador("Você", None)
            pc = computador(None)

            player.fazer_escolha()
            pc.escolha_aleatorioa()

            fazer_escolha = player.escolha.lower()
            escolha_aleatoria = pc.aleatorio.lower()

            print(f"Você escolheu:{fazer_escolha} e o computador escolheu:{escolha_aleatoria}")

            # Verifica as combinações vencedoras e perdedoras
            if fazer_escolha=='pedra' and escolha_aleatoria=='tesoura':
                print("Você ganhou ! Pedra quebra tesoura Tesoura")
                return

            elif fazer_escolha=="tesoura" and escolha_aleatoria=='pedra':
                print("Você perdeu ! Pedra quebra Tesoura !")
                return

            elif fazer_escolha=="papel" and escolha_aleatoria=='pedra':
                print("Você ganhou ! Papel embrulha pedra !")
                return

            elif fazer_escolha=="pedra" and escolha_aleatoria=='papel':
                print("Você perdeu ! Papel embrulha pedra !")
                return

            elif fazer_escolha==escolha_aleatoria:
                print("Empate ! ninguém ganhou!")
                return

            else:
                print("Resposta Inválida !")
                continue


    # Menu principal do programa
    def menu(self):
        print("*****Jokenpô*****")
        while True:
            try:
                jogar=int(jogador.validar_numeros ('\n1-Iniciar jogo\n2-Informações sobre o jogo\n3-Sair'))
                if jogar == 1:
                    self.jogar()

                elif jogar == 2:
                    self.informacao()

                elif jogar == 3:
                    print("Programa encerrado !")
                    exit()


            except ValueError:
                print("Digite apenas números !")
                continue


# Execução principal do programa
if __name__ == "__main__":
    sistema=jokenpô()
    sistema.menu()