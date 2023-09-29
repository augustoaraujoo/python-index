import xmlrpc.server

def equacao(a, b, c):
    d = b**2 - 4*a*c
    
    if d > 0:
        valX1 = (-b + d**0.5) / (2*a)
        valX2 = (-b - d**0.5) / (2*a)
        r = [valX1, valX2]
    elif d == 0:
        valX1 = -b / (2*a)
        r = [valX1]
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = (-d)**0.5 / (2*a)
        r = [f"{parte_real} + {parte_imaginaria}i", f"{parte_real} - {parte_imaginaria}i"]

    return r

def main():
    with xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000)) as server:
        server.register_function(equacao, "equacao")
        server.serve_forever()
if __name__ == "__main__":
    main()
