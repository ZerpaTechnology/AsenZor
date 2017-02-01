#Esto es el equibalente a los achivos .sql que se cargan en la base de datos
#  En los modelos no se crea la estructura de la base de datos solo se crean metodos de insercion de datos
db=DB(debug=True)
db("confirmacion").campo("nombres",db.str,vacio=False)
db("confirmacion").campo("appelidos",db.str,vacio=False)
db("confirmacion").campo("correo",db.email,unico=True,vacio=False)
db("confirmacion").campo("password",db.str,vacio=False)
db("confirmacion").campo("codigo",db.str,vacio=False)
#===================================================================
#TABLA USUARIOS
db("usuarios").campo("nombres",db.str,vacio=False)
db("usuarios").campo("appelidos",db.str,vacio=False)
db("usuarios").campo("correo",db.email,unico=True,vacio=False)
db("usuarios").campo("password",db.str,vacio=False)
db("usuarios").campo("foto",db.url)
db("usuarios").campo("imgs",db.list)
db("usuarios").campo("token",db.str,vacio=False)
db("usuarios").campo("login",db.bool,vacio=False)
#===================================================================
#TABLA MENSAJES - CHAT
db("msj_chat").campo("emisor",db.object)
db("msj_chat").campo("receptores",db.list)
db("msj_chat").campo("mensaje",db.str)
db("msj_chat").campo("hora",db.time)
#===================================================================
#TABLA MENSAJES - CORREO
db("msj_correo").campo("emisor",db.object)
db("msj_correo").campo("receptores",db.list)
db("msj_correo").campo("mensaje",db.str)
db("msj_correo").campo("hora",db.time)

#===================================================================
#TABLA POST
db("posts").campo("publisher",db.object)
db("posts").campo("destinatarios",db.list)
db("posts").campo("img",db.url)
db("posts").campo("lectores",db.list)
db("posts").campo("interacciones",db.list)
db("posts").campo("comentarios",db.list)
#==================================================================
#TABLA TOKENS
db("tokens").campo("usuario",db.email,True)
db("tokens").campo("valor",db.str,True)
db("tokens").campo("emisión",db.datetime)
db("tokens").campo("expiración",db.datetime)
#==================================================================
#TABLA DOCUMENTACION
db("documentos").campo("app",db.str,unicaFila=True)
db("documentos").campo("libro",db.str,unicaFila=True)
db("documentos").campo("tema",db.str,unicaFila=True)
db("documentos").campo("texto",db.str,unicaFila=True)
#==================================================================
#TABLA LIBROS
db("libros").campo("nombre",db.str,unicaFila=True)
db("libros").campo("autores",db.list,unicaFila=True)
db("libros").campo("colaboradores",db.list,unicaFila=True)
db("libros").campo("referencias",db.list,unicaFila=True)
db("libros").campo("Editorial",db.str,unicaFila=True)
db("libros").campo("fecha de publicación",db.datetime,unicaFila=True)
db("libros").campo("web",db.url,unicaFila=True)
db("libros").campo("costo",db.str,unicaFila=True)
#===================================================================
#TABLA ADMIN
db("admin").campo("nombre",db.str)
db("admin").campo("permisos",db.str)
#===================================================================
#TABLA PARTICIPACION
db("participacion").campo("usuario",db.email)
db("participacion").campo("serial",db.int)
db("participacion").campo("DI",db.int)
db("participacion").campo("img",db.file)
db("participacion").campo("curriculum",db.file)
#===================================================================
#TABLA COMITES
db("comites").campo("usuarios",db.email)
db("comites").campo("serial",db.int)
#===================================================================
#TABLA PLANCHAS
db("planchas").campo("nombre",db.str)
db("planchas").campo("usuarios",db.email)
db("planchas").campo("serial",db.int)
db("planchas").campo("miembros",db.list)
db("planchas").campo("img",db.file)
db("planchas").campo("mision",db.str)
db("planchas").campo("vision",db.str)
db("planchas").campo("propuesta",db.file)
db("planchas").campo("votos",db.int)
#====================================================================
#TABLA VOTACION
db("votacion").campo("nombre",db.str)
db("votacion").campo("institucion",db.str)
db("votacion").campo("mensajes",db.list)
db("votacion").campo("serial",db.int)
db("votacion").campo("tiempo de finalizacion",db.datatime)
db("votacion").campo("limite de planchas",db.int)
db("votacion").campo("limite del comite",db.int)
db("votacion").campo("ganador",db.int)








db.grabar(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py")
