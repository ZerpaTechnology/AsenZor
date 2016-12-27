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
	

def sendEmail(rem,dest,mensaje,asunto="", remAlias="",destAlias="",debug=False):
    # -*- coding: utf-8 -*- 
    import smtplib 
     
    remitente = remAlias+" <"+rem+">" 
    destinatario = destAlias+" <"+dest+">" 
    email = """From: %s 
    To: %s 
    MIME-Version: 1.0 
    Content-type: text/html 
    Subject: %s 
     
    %s
    """ % (remitente, destinatario, asunto, mensaje) 
    try: 
        smtp = smtplib.SMTP('localhost') 
        smtp.sendmail(remitente, destinatario, email) 
        if debug==True:
            print "Correo enviado" 
    except Exception,e :
        if debug==True:
            print e 
            print """Error: el mensaje no pudo enviarse. 
            Compruebe que sendmail se encuentra instalado en su sistema"""

