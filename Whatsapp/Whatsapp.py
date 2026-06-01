import pywhatkit
phone_number = '+551332512666'
message = "Teste python"
hours = 1
minutes = 53
pywhatkit.sendwhatmsg(phone_number,message,hours,minutes)
print("Mensagem enviada")
