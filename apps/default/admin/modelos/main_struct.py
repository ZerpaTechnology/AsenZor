#Esto es el equibalente a los achivos .sql que se cargan en la base de datos
#  En los modelos no se crea la estructura de la base de datos solo se crean metodos de insercion de datos
db=DB()
#===================================================================
#TABLA USUARIOS
db("usuarios").campo("nombres",db.str)
db("usuarios").campo("appelidos",db.str)
db("usuarios").campo("correo",db.email)
db("usuarios").campo("password",db.str)
db("usuarios").campo("foto",db.file)
db("usuarios").campo("imgs",db.list)
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
#TABLA APPS
db("apps").campo("nombre",db.str)
db("apps").campo("autores",db.list)
db("apps").campo("organizaciones",db.list)
db("apps").campo("versión",db.float)
db("apps").campo("estabilidad",db.str)
db("apps").campo("alias",db.str)
db("apps").campo("parentProjects",db.list)
db("apps").campo("technologyLevel",db.str)
db("apps").campo("icono",db.url)
db("apps").campo("web",db.url)
db("apps").campo("licencia",db.str)
#===================================================================
#TABLA POST
db("posts").campo("publisher",db.object)
db("posts").campo("destinatarios",db.list)
db("posts").campo("img",db.url)
db("posts").campo("lectores",db.list)
db("posts").campo("interacciones",db.list)
db("posts").campo("comentarios",db.list)
#==================================================================
db.grabar(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py")