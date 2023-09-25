import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:5000/")


altura = float(input("Digite a sua altura : "))
peso = float(input("Digite o seu peso : "))

imc = proxy.imc(peso, altura)

print("o valor do seu IMC é :", "{:.2f}".format(imc))

print("de acordo com seu resultado")

print(
    "Você possui Magreza" if imc < 18.5 else "Você está Normal." if imc < 24.9 else "Você possui Sobrepeso." if imc < 29.9 else "Você possui obesidade."
)
