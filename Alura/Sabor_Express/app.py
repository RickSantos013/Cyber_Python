import os           #importa biblioteca para poder limpar a tela

restaurantes = [{'nome':'Ricks Bar', 'categoria': 'Churrasco', 'ativo': False },{'nome': 'Torre', 'categoria': 'Italiana', 'ativo': True}]      

def nome_programa():    
    print("---------------")
    print(" 𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼")
    print("---------------\n")

def opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Status do restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")            #limpa a tela
    print("Finalizando o app...")

def voltar_menu():
    input("\nDigite uma tecla para voltar ao menu principal: ")  
    main()  

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu()

def novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f'Digite o nome da categoria do {nome}:')
    dados_do_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome} foi cadastrado com sucesso')
    voltar_menu()

def listar_restaurantes():
    os.system("cls")
    print('**********************************')
    print("Lista dos restaurantes cadastrados")
    print('**********************************\n')
    print(f'{'Nome do restaurante'.ljust(15)} | {'Categoria'.ljust(15)} | {'Status'}')
    print('----------------------------------------------')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']         
        categoria = restaurante['categoria']
        ativo = 'ativado' if ['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(17)} | {categoria.ljust(15)} | {ativo}')
    voltar_menu()

def alternar_estado():
    os.system("cls")
    print("Alternando o estado do restaurante...\n")
    nome = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome} foi ativado com sucesso' if['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)      
            
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")        
    voltar_menu()

def escolhe_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        if(opcao == 1):
            novo_restaurante()
        elif(opcao == 2):
            listar_restaurantes()
        elif(opcao == 3):
            alternar_estado()
        elif(opcao == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    nome_programa()
    opcoes()
    escolhe_opcao()    

if __name__ == "__main__":
    main()