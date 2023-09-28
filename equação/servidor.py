import xmlrpc.server

def calcular_raizes_equacao_segundo_grau(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        raizes = [x1, x2]
    elif discriminante == 0:
        x1 = -b / (2*a)
        raizes = [x1]
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = (-discriminante)**0.5 / (2*a)
        raizes = [f"{parte_real} + {parte_imaginaria}i", f"{parte_real} - {parte_imaginaria}i"]

    return raizes

def main():
    # Crie um servidor RPC
    with xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000)) as server:
        server.register_function(calcular_raizes_equacao_segundo_grau, "calcular_raizes_equacao_segundo_grau")
        
        print("Servidor RPC pronto para receber chamadas...")
        server.serve_forever()

if __name__ == "__main__":
    main()
