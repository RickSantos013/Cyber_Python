print("******")
print("Idade")
print("******")

idade = int(input("Digite a sua idade: "))
if(idade <= 12):
    print("Você é uma criança")
elif(idade >= 13 and idade <= 18):
    print("Você tem", idade, "anos, e é adolescente!")
else:
    print("Você tem", idade, "anos, e é um adulto!")
