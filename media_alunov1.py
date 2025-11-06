alunos=[]
def cadastro_alunos():
    while True:
        nome_aluno=str (input('Digite o nome do aluno: '))
        if not nome_aluno.replace(' ',"").isalpha():
            print('Digite apenas letras')
            continue
        else:
            break

    notas=[]
    for c in range(2):
        nota=float(input(f'Digite a nota {c+1}'))
        notas.append(nota)


    media=sum(notas)/len(notas)
    alunos.append({'nome':nome_aluno,'notas':notas,'media':media})
    continuar()

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

def notas_individuais():
    while True:
        nome_individual=str(input('Digite o nome do aluno para visualizar suas notas: '))
        if not nome_individual.replace(' ',"").isalpha():
            print('Digite apenas Letras !')
            continue

        alunos_existentes=[p['nome'].lower() for p in alunos]
        if nome_individual not in alunos_existentes:
            print('Aluno não encontrado!')
            return

        for aluno in alunos:
            if aluno['nome'].lower() == nome_individual:
                print(f"Nome do aluno:{aluno['nome']}, Notas: {aluno['notas']}")
                return


def media_todos():
    if not alunos:
        print('Nenhum aluno cadastrado!')
        return
    else:
        for aluno in alunos:
            print(f'Aluno:{aluno["nome"]}, Média:{aluno["media"]:.2f}')




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