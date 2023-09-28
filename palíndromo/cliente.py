import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")


def main():
    texto = input("digite uma palavra: ")

    resultado = cliente.palindromo(texto)

    if resultado:
        print(f"'{texto}' é um palíndromo.")
    else:
        print(f"'{texto}' não é um palíndromo.")


if __name__ == "__main__":
    main()
