from pinterest import pinterest
from chatgpt import chatgpt
from google import google
from youtube import youtube
import os

print('Bem vindo ao Task Helper.\nTask helper agiliza as suas buscas enquanto esta fazendo suas outras tarefas.\nAo inves de abrir o google, esperar carregar e ai sim pesquisar, ele apenas pedirá onde vai ser a sua pesquisa e o que você quer pesquisar.')
print()
searched = []
while True:
    try:
        escolha = int(input('Qual deseja abrir\n'
                            '[ 1 ] Google\n'
                            '[ 2 ] Youtube\n'
                            '[ 3 ] ChatGPT\n'
                            '[ 4 ] Pinterest\n'
                            '[ 5 ] Ver Pesquisas\n'
                            '[ 0 ] Sair\n'))

        if escolha == 1:
            site = str('Google')
            pesquisa = str(input('O que deseja pesquisar?\n'))
            google(pesquisa)
            searched.append(f'Utilizou o *{site}* para pesquisar: {pesquisa}')
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print()

        elif escolha == 2:
            site = str('Youtube')
            pesquisa = str(input('O que deseja pesquisar?\n'))
            youtube(pesquisa)
            searched.append(f'Utilizou o *{site}* para pesquisar: {pesquisa}')
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print()

        elif escolha == 3:
            site = str('ChatGPT')
            pesquisa = str(input('O que deseja pesquisar?\n'))
            chatgpt(pesquisa)
            searched.append(f'Utilizou o *{site}* para pesquisar: {pesquisa}')


        elif escolha == 4:
            site = str('Pinterest')
            pinterest()
            searched.append(f'Você abriu o *{site}*')
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print()
        elif escolha == 5:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            if len(searched)<=0:
                print('Nada aqui por enquanto')
                print()
            else:
                for c in range(len(searched)):
                    print(searched[c])
                    print()

        elif escolha == 0:
            break
        else:
            print('Numero não encontrado, tente novamente')
            print()
    except ValueError as Error:
        print('Infelizmente o programa não aceita letras como opção.\nApenas digite o numero que que esta atras da opção.')

