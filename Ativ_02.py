import os

numeros_quadrados = {i: i ** 2 for i in range(1, 6)}

def exibir_titulo():
    print("""

░█████╗░░█████╗░  ░██████╗░██╗░░░██╗░█████╗░██████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗  ██╔═══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██║░░██║  ██║██╗██║██║░░░██║███████║██║░░██║██████╔╝███████║██║░░██║██║░░██║
██╔══██║██║░░██║  ╚██████╔╝██║░░░██║██╔══██║██║░░██║██╔══██╗██╔══██║██║░░██║██║░░██║
██║░░██║╚█████╔╝  ░╚═██╔═╝░╚██████╔╝██║░░██║██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝
╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░
""")

#----------
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 8)
    print(linha)
    print(f'\n {texto} \n')
    print(linha)
    print()

#----------

def cadastrar_numeros():
    exibir_subtitulo('Cadastro de novos números')
    numero_inicial = int(input('Digite o número para elevar ao quadrado: '))

    dados_quadrados = {'numero':numero_inicial, 'quadrado':numero_inicial**2 }
    numeros_quadrados.append(dados_quadrados)

    print(f'O número {numero_inicial} elevado ao quadrado foi cadastrado!. ')
    voltar_ao_menu_principal()

def exibir_numeros():
    exibir_subtitulo('Lista de números')

    for number in numeros_quadrados:
        numero_inicial = number['numero']
        quadrado = number['quadrado']
        print(f'- O número {numero_inicial} elevado ao quadrado fica em {quadrado}')
    
    voltar_ao_menu_principal()

#----------
def exibir_opcoes():
    print('1. Cadastrar números')
    print('2. Listar números cadastrados')
    print('3. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        if opcao_escolhida == 1:
            cadastrar_numeros()
        elif opcao_escolhida == 2:
            exibir_numeros()
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#----------
def finalizar_app():
    os.system('cls')
    print('\nFinalizando o app')

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite Enter para reiniciar.')
    main()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()