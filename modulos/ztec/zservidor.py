import SocketServer
import threading
import time
import Z

#creo mi TCP Handler
class MiTcpHandler(SocketServer.BaseRequestHandler):
    
    #sobrescribo la funcion handle
    def handle(self):
        data= ""
        self.Z=Z.Z()
        while data != "salir()":
            #intento recibir informacion
                data= self.request.recv(1024)
                print data
                time.sleep(0.1) #espero 0.1 segundos antes de leer neuvamente
                self.request.send(data+"4")
                self.Z.ejecutar(data)
                
#no se assusten Creo una clase llamada ThreadServer
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def main():
    #host & port
    host ="localhost"
    port= 9999
    #creo el server
    server = ThreadServer((host,port),MiTcpHandler)
    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()
    
    print "server corriendo.."


main()      
