import xmlrpc.server


def palindromo(word):
    # função que remove o espaço em branco e torna os caracteres minusculos
    tratar_texto = word.replace(" ", "").lower()

    # verificando se a palavra é igual à sua inversão
    return tratar_texto == tratar_texto[::-1]


with xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000)) as server:
    server.register_function(palindromo, "palindromo")
    server.serve_forever()
