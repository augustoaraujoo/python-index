import xmlrpc.client

def main():
    # Crie um cliente RPC
    cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")
    
    # Solicite ao usuário para inserir os coeficientes da equação de segundo grau
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    # Faça uma chamada remota para calcular as raízes da equação
    raizes = cliente.calcular_raizes_equacao_segundo_grau(a, b, c)
    
    # Exiba o resultado
    print("Raízes da equação de segundo grau:")
    for raiz in raizes:
        print(raiz)

if __name__ == "__main__":
    main()
