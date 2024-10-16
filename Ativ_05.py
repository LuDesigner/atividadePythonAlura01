import os

def exibir_titulo():
    print("""
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─█─▄▄─█▄─▀█▄─▄█─▄─▄─██▀▄─██▄─▄▄▀█─▄▄─█▄─▄▄▀███▄─▄▄▀█▄─▄▄─███▄─▄▄─██▀▄─██▄─▄████▀▄─██▄─█─▄█▄─▄▄▀██▀▄─██─▄▄▄▄█
█─███▀█─██─██─█▄▀─████─████─▀─███─██─█─██─██─▄─▄████─██─██─▄█▀████─▄▄▄██─▀─███─██▀██─▀─███▄▀▄███─▄─▄██─▀─██▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
""")

def funcao():
    frase = input('\nDigite uma frase: ')
    contagem_palavras = {}
    palavras = frase.split()
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(f'\n{contagem_palavras}')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite Enter para reiniciar.')
    main()

def main():
    os.system('cls')
    exibir_titulo()
    funcao()

if __name__ == '__main__':
    main()