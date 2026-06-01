print("********")
print("Tabuada")
print("********")

numero = int(input("Quero a tabuada do número: "))
for i in range(1,11):
    multiplicacao = (numero * i)
    print("{} x {} = {}".format(numero, i, multiplicacao))