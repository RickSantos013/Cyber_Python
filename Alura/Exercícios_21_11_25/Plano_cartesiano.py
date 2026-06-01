print("****************")
print("Plano Cartesiano")
print("****************")

x = int(input("Qual a coordenada do ponto x: "))
y = int(input("Qual a coordenada do ponto y: "))

if(x > 0 and y > 0):
    print("O ponto está no 1o quadrante")
elif(x < 0 and y > 0):
    print("O ponto está no 2o quadrante")
elif(x < 0 and y < 0):
    print("O ponto está no 3o quadrante")
elif(x > 0 and y < 0):
    print("O ponto está no 4o quadrante")
else:
    print("O ponto está na origem do gráfico")

