alunos=[]
#Função que cadastra os dados inseridos
def cadastro_alunos():
    while True:
        nome_aluno=str (input('Digite o nome do aluno: ')).strip().lower()
        #Metodo de validação, permite apenas letras
        if not nome_aluno.replace(' ',"").isalpha():
            print('Digite apenas letras')
            continue
        else:
            break

    #Toda vez que um novo cadastro for iniciado a lista notas será zerada.
<<<<<<< HEAD
    notas = []
    for c in range(2):
        while True:
            try:
                nota = float(input(f'Digite a nota {c + 1}: '))
                if nota < 0 or nota > 10:
                    print('Digite uma nota entre 0 e 10!')
                    continue
                notas.append(nota)
                break
            except ValueError:
                print('Digite apenas números!')
=======
    notas=[]
    for c in range(2):
        nota=float(input(f'Digite a nota {c+1}'))
        notas.append(nota)
>>>>>>> c25e52a7f9b72e3e8dd8dc92b04f5f3e24d85820

    #sum e len são comandos utilizados para realizar operações de dados/valores que se encontram em uma lista
    media=sum(notas)/len(notas)

    #A lista "alunos" é a principal sendo que a lista "notas" foi englobada
    alunos.append({'nome':nome_aluno,'notas':notas,'media':media})
    continuar()

#Função que contém loop while,independentemente da resposta o programa volta ao menu (via return), dessa forma é possível escolher o que fazer
def continuar():
    while True:
        cont=str(input('Deseja cadastrar outro aluno (a)?')).lower().strip()
        if cont in ['n','nao','não']:
            return

        elif cont in ['s','sim']:
            return

        else:
            print('Resposta inválida !')
            continue

#Função criada para permitir a consulta das notas de um aluno em especifico
def notas_individuais():
    while True:
        nome_individual=str(input('Digite o nome do aluno para visualizar suas notas: ')).lower().strip()
        if not nome_individual.replace(' ',"").isalpha():
            print('Digite apenas Letras !')
            continue

        #Variavel que guarda o acesso ao nome de cada aluno na lista alunos
        alunos_existentes=[p['nome'].lower().strip() for p in alunos]

        #Se o nome fornecido não estiver no cadastro o programa retorna ao menu depois de apresentar a mensagem do print
        if nome_individual not in alunos_existentes:
            print('Aluno não encontrado!')
            return

        #Percorre aluno por aluno na lista alunos até achar o nome fornecio em "nome_individual"), quando acha printa as informações e sai da função
        for aluno in alunos:
            if aluno['nome'].lower().strip() == nome_individual:
                print(f"Nome do aluno:{aluno['nome']}, Notas: {aluno['notas']}")
                return

#Função que mostra a lista com nome e média de todos os alunos
def media_todos():
    if not alunos:
        print('Nenhum aluno cadastrado!')
        return
    else:
        for aluno in alunos:
            print(f'Aluno:{aluno["nome"]}, Média:{aluno["media"]:.2f}')



#Função menu interativo
def menu():
    while True:
        try:
            escolher=int(input('\n1-Cadastrar aluno\n2-Visualizar as notas de cada aluno\n3-Visualizar as médias dos aluno cadastrados\n4-Encerrar programa'))

            if escolher<0:
                print('Digite números inteiros positivos !')
                continue

            elif escolher==1:
                cadastro_alunos()

            elif escolher==2:
                notas_individuais()

            elif escolher==3:
                media_todos()

            elif escolher==4:
                print('Programa encerrado!')
                exit()

        except ValueError:
            print('Digite apenas números inteiros positivos !')





















menu()