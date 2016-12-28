import SocketServer
import threading
import time


#creo mi TCP Handler
class MiTcpHandler(SocketServer.BaseRequestHandler):
    
    #sobrescribo la funcion handle
    def handle(self):
        data= ""
        while data != ".salir":
            #intento recibir informacion
            try:
                data= self.request.recv(1024)
                if data!="":
                    print data
                time.sleep(0.1) #espero 0.1 segundos antes de leer neuvamente
            #si hubo un error lo digo y termino el handle
            except:
                print "El cliente D/C o hubo un error"
                data=".salir"

#no se assusten Creo una clase llamada ThreadServer
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def serverSock(host,port,welcome="Server corriendo.."):
    #host & port
    #creo el server
    server = ThreadServer((host,port),MiTcpHandler)
    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()
    
    print welcome


   
def clienteSock(host,port,msj="",welcome="Ingrese un mensaje o salir para terminar"):
		import socket
		#creo un socket y me conecto
		sock= socket.socket()
		sock.connect((host,port))
		enviar=True
		print welcome
		while enviar==True:
		    #intento mandar msj
		    try:
		        sock.send(msj)
		        enviar=False
		    # si no se puede entonces salgo
		    except:
		        print "no se mando el mensaje"
		        enviar=False
		    
		sock.close() #recuerden cerrar el socket
	
#Esta funcion solo es posible ejecutarla en una maquina y no desde el serividor con cgi(XAMPP)
#La solicion seria ejecutarla atravez de un socketServer, ya que con python directo funciona
def sendEmail(rem,dest,password,mensaje,asunto="", remAlias="",destAlias="",debug=False):
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
     
    # Enviar correo Gmail con Python
    # www.pythondiario.com
     
    import smtplib
    fromaddr = rem
    toaddrs  = rem
    msg = mensaje
     
     
    # Datos
    username = rem
    
     
    # Enviando el correo
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def normalizar(v):
    try:
        exec("a="+v)
        return a
    except:
        return v
