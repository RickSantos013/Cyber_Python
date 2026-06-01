

def licao():    
    titulo_licao("Lista de 1 a 10")
    print("---------------")

def licao2():
    print("***************")
    titulo_licao("Lista de Nomes")
    print("----------------")

def licao3():
    print("**************")
    titulo_licao("Lista dos Anos")
    print("-----------------")

def imprime_licao1():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(lista)
    print()

def imprime_licao2():
    lista = ['Henrique', 'SANTOS', 'UFC', 'Vencedor']
    print(lista)
    print()

def imprime_licao3():
    lista = [1996,2025]
    print(lista)
    print()

def titulo_licao(texto):
    print(texto)

def main():
    licao()
    imprime_licao1()
    licao2()
    imprime_licao2()
    licao3()
    imprime_licao3()

if __name__ == "__main__":
    main()