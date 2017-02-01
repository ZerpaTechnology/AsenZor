#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
import SocketServer
import threading
import time


#creo mi TCP Handler
class MiTcpHandler(SocketServer.BaseRequestHandler):
    
    #sobrescribo la funcion handle
    def handle(self):
        
        while self.data[0] != ".salir":
            #intento recibir informacion
            try:
                self.data.append(self.request.recv(1024))
                self.request.send("listo")
                del self.data[0]
                time.sleep(0.1) #espero 0.1 segundos antes de leer neuvamente
            #si hubo un error lo digo y termino el handle
            except:
                print "El cliente D/C o hubo un error"
                self.data[0]=".salir"

class MiTcpHandler2(SocketServer.BaseRequestHandler):#para uso en bases de datos
    
    #sobrescribo la funcion handle
    def handle(self):
        
        while self.data[0] != ".salir":
            #intento recibir informacion
            try:
                self.data.append(self.request.recv(1024))
                self.request.send("listo")
                self.data[0]=".salir"
            #si hubo un error lo digo y termino el handle
            except Exception, e:
                print "El cliente D/C o hubo un error"
                print e
                self.data[0]=".salir"

#no se assusten Creo una clase llamada ThreadServer
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def serverSock(host,port,welcome="Server corriendo..",data=[""]):
    #host & port
    #creo el server
    MiTcpHandler.data=data
    server = ThreadServer((host,port),MiTcpHandler)

    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()
    
    print welcome


def serverSock2(host,port,welcome="Server corriendo..",data=[""]):
    #host & port
    #creo el server
    MiTcpHandler2.data=data
    server = ThreadServer((host,port),MiTcpHandler2)

    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()
    
    print welcome

def setCookie(cookie):
    print "<script type='text/javascript'>"
    print "document.cookie='"+cookie+"'"
    print "</script>"
def getCookie():
    import os
    return os.environ["HTTP_COOKIE"]

   
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
			     time.sleep(0.1)
			     print sock.recv(1024)
			     break
			     enviar=False
		    # si no se puede entonces salgo
		    except Exception, e: 
		            print "no se mando el mensaje"
		            print e
		            enviar=False

		sock.close() #recuerden cerrar el socket

	
#Esta funcion solo es posible ejecutarla en una maquina y no desde el serividor con cgi(XAMPP)
#La solicion seria ejecutarla atravez de un socketServer, ya que con python directo funciona
def sendEmail(rem,dest,password,mensaje,asunto="", remAlias="",destAlias="",debug=False):
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
     
    # Enviar correo Gmail con Python
    # www.pythondiario.com
    try:
        import smtplib

        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # me == my email address
        # you == recipient's email address

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = asunto
        msg['From'] = rem
        msg['To'] = dest

        # Create the body of the message (a plain-text and an HTML version).
        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        '''
        html = """\
        <html>
          <head></head>
          <body>
            <p>Hi!<br>
               How are you?<br>
               Here is the <a href="http://www.python.org">link</a> you wanted.
            </p>
          </body>
        </html>
        """
        '''
        html = """\
        <html>
          <head>
          <meta charset="utf-8">
          </head>
          <body>
            """+mensaje+"""
            </p>
          </body>
        </html>
        """

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)
        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login(rem, password)
        mail.sendmail(rem, dest, msg.as_string())
        mail.quit()

    except Exception as e:
        print "<?php mail('"+dest+"','"+asunto+"','"+"','"+mensaje+"','"+rem+")?>"
        if debug==True:
            print e," esto puede ser culpa del servidor"
            print "Se intento hacer el envio por PHP"

    

def normalizar(v):
    try:
        exec("a="+v)
        return a
    except:
        return v

def zAPI(linea,vars):
        for elem in vars:
            exec(elem+"=vars['"+elem+"']")
        if len(linea)<=200:     
            c=0
            mark=0
            mark2=0#para los bucles y condicionales
            codigo=""
            nivel=0
            condicion=[]
            funciones=0
            enlace=False
            lineas=0
            __r=None

            while c<len(linea):
                #si hay condiciones
                if len(condicion)>1:
                    if condicion[-1]=="==" or condicion[-1]=="!=" or condicion[-1]==">=" or condicion[-1]=="<=" or condicion[-1]=="<" or condicion[-1]==">" or condicion[-1]=="in" or condicion[-1]=="for " or condicion[-1]=="while ":

                        if c>0 and c<=3:
                            if  linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                                if  linea[c-2]=="=" and linea[c-1]=="=":
                                    #if len()
                                    pass
                                elif linea[c-2]=="!" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]!="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]!="=":
                                    pass
                                #es una asignacion
                                elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                    pass
                                pass
                            pass

                        #------------------------------
                        if c>=3 and c<=5:
                            if  linea[c-1]!=" " and linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                                if  linea[c-2]=="=" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="!" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]!="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]!="=":
                                    pass
                                #es una asignacion
                                elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                    pass
                                pass


                            elif linea[c-1]==" " and linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                                if  linea[c-3]=="=" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]=="!" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]==">" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]=="<" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]=="<" and linea[c-2]!="=":
                                    pass
                                elif linea[c-3]==">" and linea[c-2]!="=":
                                    pass
                                pass

                        #para lo anterior y bucle while
                        if c>=5 and c<=9:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                pass
                            pass
                        #para bucle for
                        elif c>=9:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                pass
                            pass
                            
                        #para bucle while y for
                        elif c>=11 and c<13:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                        
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                if "for " in linea[:c-3]:
                                    pass
                                else:
                                    pass
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                if "while " in linea[:c-3]:
                                    pass
                                else:
                                    pass
                            
                        #para el bucle while con in
                        elif c>=13:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                
                                if "for " in linea[:c-3]:
                                    pass
                                else:
                                    pass
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                
                                if "while " in linea[:c-3]:
                                    pass

                                else:
                                    pass
                            else:

                                if linea[c]==";":
                                    if nivel==0:
                                        codigo.append(linea[mark:c])
                                        mark=c
                                        lineas+=1
                                    else:
                                        tab=" "*condicion
                                        codigo.append(tab+linea[mark:c])
                                        lineas+=1



                                elif linea[c]=="]":
                                    pass
                                elif linea[c]=="}":
                                    pass
                                elif linea[c]=="]]":
                                    pass
                                elif linea[c]=="}}":
                                    pass

                        else:
                            if linea[c]==";":
                                pass
                            elif linea[c]=="]":
                                pass
                            elif linea[c]=="}":
                                pass
                            elif linea[c]=="]]":
                                pass
                            elif linea[c]=="}}":
                                pass


                else:
                    #para una pregunta boolean
                    if c>0 and c<=3:
                        if  linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":

                            if  linea[c-2]=="=" and linea[c-1]=="=":
                                        
                                    if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])


                            elif linea[c-2]=="!" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]!="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]!="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            #es una asignacion
                            elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            pass
                        pass

                    #------------------------------
                    if c>=3 and c<=7:
                        if  linea[c-1]!=" " and linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                            if  linea[c-2]=="=" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="!" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]!="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]!="=":
                                exec("__r="+linea[mark:c+1])
                            #es una asignacion
                            elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            pass


                    #para lo anterior y bucle while
                    if c>7 and c<=10:

                        if linea[c-1]=="=" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="!" and linea[c]=="=":
                            pass
                        elif linea[c-1]==">" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]!="=":
                            pass
                        elif linea[c-1]==">" and linea[c]!="=":
                            pass
                        #usa in
                        elif " in " in linea[mark:c-2] and linea[c-2]==" " and linea[c]!=" ":
                            nivel+=1
                            
                            if condicion==[]:
                                codigo+="if "+linea[mark:c-2]+":\n"
                                mark=c
                            else:
                                if condicion[-1]=="if":
                                    pass
                                elif condicion[-1]=="elif":
                                    pass

                            mark=c
                            condicion.append("for")


                        #es una asignacion
                        elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                            pass
                        else:
                            if nivel>0:
                                tab=" "*nivel
                                if linea[c]==":":
                                    
                                    codigo+=tab+linea[mark-1:c]+"("
                                    c+=1
                                    mark=c

                                    funciones+=1
                                if linea[c]==";":
                                    if funciones>0:
                                        codigo+=tab+linea[mark:c]+")"
                                    else:
                                        codigo+="\n"
                                else:
                                    pass
                        
                    #para bucle for
                    elif c>10 and c<=13:
                        if linea[c-1]=="=" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="!" and linea[c]=="=":
                            pass
                        elif linea[c-1]==">" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]!="=":
                            pass
                        elif linea[c-1]==">" and linea[c]!="=":
                            pass
                        #usa in
                        elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                            pass
                        #es una asignacion
                        elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                            pass
                        else:
                            if nivel>0:
                                pass
                            
                        
                    #para bucle while y for
                    elif c>13:
                        if linea[c-1]=="=" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="!" and linea[c]=="=":
                            pass
                        elif linea[c-1]==">" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]!="=":
                            pass
                        elif linea[c-1]==">" and linea[c]!="=":
                            pass
                    
                        #usa in
                        elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                            if "for " in linea[:c-3]:
                                pass
                            else:
                                pass
                            pass
                        #es una asignacion
                        elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                            if "while " in linea[:c-3]:
                                pass
                            else:
                                pass
                        else:
                            if nivel>0:
                                pass

                        
                    #para el bucle while con in
                    
                c+=1
            if funciones>0:
                codigo+=linea[mark:c]+")"
        try:
            print "-----------"
            print codigo
            print "-----------"
            exec(codigo)
            return __r
        except Exception,e:
            print e

def urlParamDecod(param):
    return param.replace("+"," ").replace("%40","@").replace("®","reg")
def redirect(url,tiempo=0):
    print "<META HTTP-EQUIV='Refresh' CONTENT='"+str(tiempo)+"; URL="+url+"'>";
def charset(cha="utf-8"):
    print "<meta charset='"+cha+"'>"


def zform(db,action,controller="post.py",placeholder="",submit="Enviar",i=None,style="",display="block",_class="ff pad-1",ignorar=[],confirmar=[],valores={},clases={}):
    try:
        form=style+"<form name='_FORM"+action+"' id='_FORM"+action+"' action='"+controller+"'"+(" class='text-center "+_class+"'" if display=="block-center" or display=="inline-block-center" else "")+(" class='text-right "+_class+"'" if display=="block-right" or display=="inline-block-right" else "")+(" class='text-justify "+_class+"'" if display=="block-justify" or display=="inline-block-justify" else "")+" method='post'>"
        c=0
        id_elem=1
        d=""
        d2=""

        script=""

        
        for elem in db.campos[db.seleccion]: 

                value=""

                if i!=None:
                            value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                else:

                        
                        if elem[0] in valores:

                            value="value='"+str(valores[elem[0]])+"'"
                        else:
                            value=""

                        if elem[0] in clases:

                            if elem[0] in ignorar:
                                
                                _class=" class='"+clases[elem[0]]+" hidden'"
                            else:
                                
                                _class=" class='"+clases[elem[0]]+"'"
                        else:
                            if elem[0] in ignorar:
                                
                                _class=" class='hidden'"

                            else:
                                
                                _class=""
                if display=="block" or display=="block-center" or display=="block-rigth" or display=="block-justify":
                    d="<br "+_class+">"
                    d2="<br "+_class+">"
                elif display=="inline-block" or display=="inline-block-center" or display=="inline-block-rigth" or display=="inline-block-justify":
                    d2="<br "+_class+">"

                if elem[1]==db.str:
                    if elem[0] in confirmar:

                  
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" id='_CONF"+action+elem[0]+"'><span id='_CONFSPAN"+action+elem[0]+" class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+" class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+" class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+" class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='Confirmar "+placeholder+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+" class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+" class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                        script+="""
                        $('#_CONF"""+action+elem[0]+"""').keyup(function(){
                        
                        if (document.getElementById('"""+action+elem[0]+"""').value== document.getElementById('_CONF"""+action+elem[0]+"""').value){$('#_CONFSPAN"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN2"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(true) }
                        else{
                        $('#_CONFSPAN2"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(flase) }
                        })
                        """
                    else:
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" name='"+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2

                elif elem[1]==db.password:
                    if elem[0] in confirmar:

                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='password' "+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='password' "+value+_class+" id='_CONF"+action+elem[0]+"'><span id='_CONFSPAN"+action+elem[0]+"'' class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+"'' class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+"' class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+"' class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='Confirmar "+placeholder+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+"' class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+"' class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                        script+="""
                        $('#_CONF"""+action+elem[0]+"""').keyup(function(){
                        
                        if (document.getElementById('"""+action+elem[0]+"""').value== document.getElementById('_CONF"""+action+elem[0]+"""').value){$('#_CONFSPAN"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN2"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(true) }
                        else{
                        $('#_CONFSPAN2"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(false) }
                        })
                        """
                    else:
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" name='"+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2

                elif elem[1]==db.doc:
                    if placeholder!="":
                        if i!=None:
                            value=str(db.obtenerCampo(i,elem[0]))
                        else:
                            value=""
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<textarea name='"+elem[0]+"'"+_class+">"+value+"</textarea>"+d2
                        id_elem+=2
                    else:
                        if i!=None:
                            value=str(db.obtenerCampo(i,elem[0]))
                        else:
                            value=""
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<textarea placeholder='"+placeholder[c]+elem[0]+"' name='"+elem[0]+"' id='"+action+elem[0]+"'"+_class+">"+value+"</textarea>"+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<textarea placeholder='"+placeholder+elem[0]+"' name='"+elem[0]+"' id='"+action+elem[0]+"'"+_class+">"+value+"</textarea>"+d2
                            id_elem+=2
                elif elem[1]==db.email:
                    if elem[7]!=-1:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+action+str(id_elem+1)+'"><input  type="email" '+mini+maxi+step+value+_class+'name="'+elem[0]+'"></div>'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+action+str(id_elem+1)+'"><input  type="email" placeholder="'+placeholder[c]+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'"></div>'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+action+str(id_elem+1)+'"><input type="email" placeholder="'+placeholder+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'"></div>'+d2
                            id_elem+=2
                elif elem[1]==db.int or elem[1]==db.float or elem[1]==db.long:
                    if elem[7]!=-1:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'" type="number" '+mini+maxi+step+value+_class+'name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'" type="number" placeholder="'+placeholder[c]+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'" type="number" placeholder="'+placeholder+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'">'+d2
                            id_elem+=2

                elif elem[1]==db.datetime:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="datetime" onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true)" '''+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="datetime" onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true)" placeholder="'''+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="datetime" onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true)" placeholder="'''+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2

                elif elem[1]==db.time:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="time" onclick="mostrarCalendar(this,'hh:ii')" '''+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="time" onclick="mostrarCalendar(this,'hh:ii')" placeholder="'''+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="time" onclick="mostrarCalendar(this,'hh:ii')" placeholder="'''+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2

                elif elem[1]==db.date:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="date" class="date" onclick="mostrarCalendar(this,'yyyy/mm/dd')" '''+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="date" class="date" onclick="mostrarCalendar(this,'yyyy/mm/dd')" placeholder="'''+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="date" class="date" onclick="mostrarCalendar(this,'yyyy/mm/dd')" placeholder="'''+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                elif elem[1]==db.file:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+str(id_elem+1)+'"><input type="file" '+mini+maxi+step+value+_class+'></div>'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+str(id_elem+1)+'"><input type="file" placeholder="'+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'"><div>'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+str(id_elem+1)+'"><input type="file" placeholder="'+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'"></div>'+d2
                            id_elem+=2
                

                c+=1

        return form+"<input type='text' class='hidden' name='action' value='"+action+"'><input type='submit' id='"+str(id_elem+1)+"' class='btn white b-r5' value='"+submit+"'></form><script>"+script+"</script>"
    except Exception, e:
        print "Error en el zform"
        print e

def INPUT(_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_value=""):
    if _type=="time":
        _onclick="mostrarCalendar(this,'hh:ii');"+_onclick
    elif _type=="date":
        _onclick="mostrarCalendar(this,'yyyy/mm/dd');"+_onclick
    elif _type=="datetime":
        _onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true);"+_onclick
    return "<input "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' value="'''+_value+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"

def DIV(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<div "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</div>"

def FORM(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_action=None,_method="post",_zaction=None):
    
    return "<form "+''' method="'''+_method+'''"'''+''' onclick="'''+_onclick+'''"'''+(''' action="'''+_action+'''"''' if _action!=None else '')+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+(INPUT(_name="action",_class="hidden",_value=_zaction) if _zaction!=None else '')+"</form>"
def P(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<p "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</p>"

def B(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<B "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</B>"
def H1(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h1 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h1>"

def H2(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h2 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h2>"

def H3(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h3 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h3>"

def H4(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h4 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h4>"

def H5(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h5 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h5>"

def H6(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h6 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h6>"
def H7(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h7 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h7>"
def SPAN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<span "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</span>"
def ARTICLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<article "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</article>"
def SECTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<section "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</section>"
def BODY(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<body "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</body>"
def HEAD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<head "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</head>"
def HEADER(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<header "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</header>"
def FOOTER(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<footer "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</footer>"
def ASIDE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<aside "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</aside>"
def STYLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<style "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</style>"
def CANVAS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<canvas "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</canvas>"
def AUDIO(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):
    
    return "<audio "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</audio>"
def VIDEO(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):
    
    return "<video "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</video>"
def SCRIPT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):    
    return "<script "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</script>"
def NOSCRIPT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):    
    return "<noscript "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</noscript>"


def NAV(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<aside "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</nav>"
def TABLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<table "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</table>"
def TR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<tr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</tr>"
def TD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<td "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</td>"
def CAPTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<caption "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</caption>"
def COL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<col "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</col>"
def COLGROUP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<colgroup "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</colgroup>"
def MAIN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<main "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</main>"
def LI(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):  
    return "<li "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</li>"
def UL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):  
    return "<ul "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ul>"
def DL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<dl"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dl>"    
def DT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<dt"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dt>"
def DD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<dd"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dd>"        
def FIGURE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<figure"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</figure>"    
def FIGCAPTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<figcaption"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</figcaption>"    
def STRONG(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<strong"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</strong>"    
def EM(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<em"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</em>"    
def S(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<S"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</S>"    
def CITE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<cite"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</cite>"    
def MENU(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<menu"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</menu>"    
def COMMAND(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<command"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</command>"    
def DETALIST(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<detalist"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</detalist>"    
def METER(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<meter"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</meter>"    
def PROGRESS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<progress"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</progress>"    
def OUTPUT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<output"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</output>"    
def KEYGEN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<keygen"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</keygen>"    
def TEXTAREA(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<textarea"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</textarea>"    
def OPTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<option"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</option>"    
def DATALIST(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<datalist"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</datalist>"    
def SELECT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<select"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</select>"    
def BUTTON(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<button"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</button>"    
def LABEL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<label"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</label>"    
def legend(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<legend"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</legend>"    
def FIELDSET(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<fieldset"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</fieldset>"    
def MAP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<map "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</map>"
def AREA(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<area "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</area>"

def A(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_href=""):
    
    return "<a "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' href="'''+_href+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</a>"
def IMG(_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_src=""):
    
    return "<img "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' src="'''+_src+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"
def BR(_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_src=""):
    
    return "<br"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' src="'''+_src+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"
def SOURCE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<source "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</source>"
def PARAM(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<param "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</param>"
def EMBED(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<embebed "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</embebed>"
def IFRAME(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<iframe "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</iframe>"
def DEL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<del "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</del>"
def INS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<ins "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ins>"
def WBR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<wbr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</wbr>"
def BDO(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<bdo "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</bdo>"
def BDI(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<bdi "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</bdi>"
def MARK(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<mark "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</mark>"
def U(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<u "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</u>"
def I(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<i "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</i>"
def SUB(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<sub "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</sub>"
def SUP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<sup "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</sup>"
def KBD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<kbd "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</kbd>"
def SAMP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<samp "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</samp>"
def VAR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<var "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</var>"
def CODE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<code "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</code>"   
def TIME(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<time "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</time>"
def DATA(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<data "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</data>"
def ABBR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<abbr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</abbr>"
def DFN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<dfn "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dfn>"
def Q(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<q "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</q>"
def SMALL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<small "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</small>"
def PRE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<pre "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</pre>"
def HR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<hr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</hr>"
def OL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<ol "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ol>"
def BLOCKQUOTE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<blockquote "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</blockquote>"
def ADDRESS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<address "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</address>"
def LINK(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<link "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</link>"
def BASE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<base "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</base>"
def META(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<meta "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</meta>"
def TITLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<title "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</title>"
def TRACK(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<track "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</track>"
def MATH(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<math "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</math>"
def OBJECT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<object "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</object>"
def RP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<rp "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</rp>"
def RT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<rt "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</rt>"
def RUBY(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<ruby "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ruby>"
def SUMMARY(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<summary "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</summary>"
def LEGEND(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<legend "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</legend>"

def redirecter(base,app,vista):
    redirecter.base=base
    redirecter.app=app
    redirecter.vista=vista

    def redireccionador(vista=redirecter.vista,**args):
        if "app" not in args:
            app="app="+redirecter.app
        else:
             app="app="+args["app"]
        c=""
        for elem in args:
            if elem != "app" and elem != "vista":
                c+="&"+elem+"="+args[elem]

        vista="vista="+vista
        redirect(redirecter.base+app+"&"+vista+c)
    return redireccionador
