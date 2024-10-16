import os

cadastro_geral = [ ]

def exibir_titulo():
    print("""

▒█▀▀▀ ▀█▀ ▒█▀▀█ ▒█░▒█ ░█▀▀█ 　 ▒█▀▀▄ ▒█▀▀▀ 　 ▒█▀▀▀ ▒█░▒█ ▒█▄░▒█ ▒█▀▀█ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█▀▀█ ▀█▀ ▒█▀▀▀█ ▒█▀▀▀█ 
▒█▀▀▀ ▒█░ ▒█░░░ ▒█▀▀█ ▒█▄▄█ 　 ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀▀ ▒█░▒█ ▒█▒█▒█ ▒█░░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ ▒█▄▄█ ▒█▄▄▀ ▒█░ ▒█░░▒█ ░▀▀▀▄▄ 
▒█░░░ ▄█▄ ▒█▄▄█ ▒█░▒█ ▒█░▒█ 　 ▒█▄▄▀ ▒█▄▄▄ 　 ▒█░░░ ░▀▄▄▀ ▒█░░▀█ ▒█▄▄█ ▄█▄ ▒█▄▄▄█ ▒█░░▀█ ▒█░▒█ ▒█░▒█ ▄█▄ ▒█▄▄▄█ ▒█▄▄▄█
    """)

#----------Subtitulo
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 8)
    print(linha)
    print(f'\n {texto} \n')
    print(linha)
    print()

#----------Cadastro de usuários
def cadastrar_usuario():
    exibir_subtitulo('Cadastro de novos usuários')

    nome_do_usuario = input('Digite o nome do usuário: ')
    idade = input(f'Digite a idade do usuário {nome_do_usuario}: ')
    profissao = input(f'Digite o cargo do {nome_do_usuario}: ')
    cidade = input('Digite a cidade do usuário: ')

    dados_do_usuario = {'nome':nome_do_usuario, 'idade':idade,'profissao':profissao, 'cidade':cidade, 'ativo':False}
    cadastro_geral.append(dados_do_usuario)
    print(f'O usuário {nome_do_usuario} foi cadastrado com sucesso. ')
    voltar_ao_menu_principal()

#----------Exibir Cadastro de usuários

def exibir_cadastro():
    exibir_subtitulo('Listando de cadastrados')

    print(f'{'Nome'.ljust(22)} | {'Idade'.ljust(20)} | {'Profissão'.ljust(20)} | {'Cidade'.ljust(20)} | Status')
    for user in cadastro_geral:
        nome_do_usuario = user['nome']
        idade = user['idade']
        cidade = user['cidade']
        profissao = user['profissao']
        ativo = 'ativado' if user['ativo'] else 'desativado'
        print(f'- {nome_do_usuario.ljust(20)} | {idade.ljust(20)} | {profissao.ljust(20)} | {cidade.ljust(20)} | {ativo} ')

    voltar_ao_menu_principal()

#----------Menu Usuário

def atualizar_usuario():
    exibir_subtitulo('Atualizar cadastros')

    print('1. Atualizar nome')
    print('2. Atualizar idade')
    print('3. Atualizar cidade')
    print('4. Atualizar profissão')
    print('5. Atualizar status')
    print('6. Voltar ao menu principal\n') 

    try:
        opcoes_atualizar = int(input('Escolha uma das opções: '))

        if opcoes_atualizar == 1:
            atualizar_nome()
        elif opcoes_atualizar == 2:
            atualizar_idade()
        elif opcoes_atualizar == 3:
            atualizar_cidade()
        elif opcoes_atualizar == 4:
            atualizar_profissao()
        elif opcoes_atualizar == 5:
            estado_do_usuario()
        elif opcoes_atualizar == 6:
            voltar_ao_menu_principal()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    

#----------Atualizações
def atualizar_nome():
    exibir_subtitulo('Alterando nome do usuário')
    nome_do_usuario = input('Digite o nome do usuário que deseja alterar: ')
    new_user = input('Digite o novo nome do usuário: ')  

    for user in cadastro_geral :
        if nome_do_usuario == user['nome']:
            new_user = nome_do_usuario[new_user]
            mensagem = f'O usuário {nome_do_usuario} foi modificado com sucesso para {new_user}.'
            print(mensagem)
        else:    
            print('Usuário não encontrado')

    voltar_ao_menu_principal()

def atualizar_idade():
    exibir_subtitulo('Atualizando idade do usuário')
    nome_do_usuario = input('Digite o nome do usuário que deseja atualizar a idade: ')

    for user in cadastro_geral:
        if nome_do_usuario == user['nome']:
            nova_idade = input(f'Digite a nova idade para {nome_do_usuario}: ')
            user['idade'] = nova_idade
            print(f'Idade de {nome_do_usuario} foi atualizada para {nova_idade}.')
            break
    else:
        print('Usuário não encontrado.')

    voltar_ao_menu_principal()

def atualizar_cidade():
    exibir_subtitulo('Atualizando cidade do usuário')
    nome_do_usuario = input('Digite o nome do usuário que deseja atualizar a cidade: ')

    for user in cadastro_geral:
        if nome_do_usuario == user['nome']:
            nova_cidade = input(f'Digite a nova cidade para {nome_do_usuario}: ')
            user['cidade'] = nova_cidade
            print(f'Cidade de {nome_do_usuario} foi atualizada para {nova_cidade}.')
            break
    else:
        print('Usuário não encontrado.')

    voltar_ao_menu_principal()

def estado_do_usuario():
    exibir_subtitulo('Alterando estado do usuário')
    nome_do_usuario = input('Digite o nome do usuário que deseja alterar o estado: ')
    user_encontrado = False

    for user in cadastro_geral :
        if nome_do_usuario == user['nome']:
            user_encontrado = True
            user['ativo'] = not user['ativo']
            mensagem = f'O usuário {nome_do_usuario} foi ativo com sucesso.' if user['ativo'] else f'O usuário {nome_do_usuario} foi desativado com sucesso.'
            print(mensagem)
    
    if not user_encontrado:
        print('Usuário não encontrado')
    voltar_ao_menu_principal()

def atualizar_profissao():
    exibir_subtitulo('Atualizando profissão ao usuário')
    nome_do_usuario = input('Digite o nome do usuário que deseja atualizar a profissão: ')

    for user in cadastro_geral:
        if nome_do_usuario == user['nome']:
            profissao = input(f'Digite a profissão para {nome_do_usuario}: ')
            user['profissao'] = profissao
            print(f'Profissão {profissao} adicionada para {nome_do_usuario}.')
            break
    else:
        print('Usuário não encontrado.')

    voltar_ao_menu_principal()

def remover_usuario():
    exibir_subtitulo('Removendo usuário do cadastro')
    nome_do_usuario = input('Digite o nome do usuário que deseja remover: ')

    for user in cadastro_geral:
        if nome_do_usuario == user['nome']:
            cadastro_geral.remove(user)
            print(f'Usuário {nome_do_usuario} removido com sucesso.')
            break
    else:
        print('Usuário não encontrado.')

    voltar_ao_menu_principal()

#----------Menu Principal
def exibir_opcoes():
    print('1. Cadastrar usuário')
    print('2. Atualizar usuário')
    print('3. Remover usuário')
    print('4. Exibir cadastro')
    print('5. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        if opcao_escolhida == 1:
            cadastrar_usuario()
        elif opcao_escolhida == 2:
            atualizar_usuario()
        elif opcao_escolhida == 3:
            remover_usuario()
        elif opcao_escolhida == 4:
            exibir_cadastro()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#----------Extras
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