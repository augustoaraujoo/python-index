from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

def imc(peso,altura):
    imc = peso/(altura**2)
    return imc

server = SimpleXMLRPCServer(("localhost", 5000), requestHandler=SimpleXMLRPCRequestHandler)
#chamada da func
server.register_function(imc,"imc")
server.serve_forever()