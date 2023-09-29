import xmlrpc.client

def main():
    cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")
    
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    raizes = cliente.equacao(a, b, c)
    
    # Exibir
    print("Raízes da equação de segundo grau:")
    for raiz in raizes:
        print(raiz)

if __name__ == "__main__":
    main()
