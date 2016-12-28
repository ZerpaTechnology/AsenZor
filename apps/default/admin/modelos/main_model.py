#====================================================================
#Cabecera del modelo
import sys
import os
#sys.path.append("../config")
import random
import settings.roots as roots
import settings.config 
from ztec.zdb import DB
from ztec import zu
from ztec import zred
name_db=settings.config.dbs[0] #main_db
p=settings.config.p
root_db=p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py"
import time
tiempo=time.time()
if os.path.exists(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py"):
	db=DB(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py")
	

else:
	f=open(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_struct.py","r")
	struct=f.read()
	f.close()
	exec(struct)
#===================================================================
#Cuerpo del modelo
def registrarUsuario(nombres,apellidos,correo,password,foto,imgs,db=db):
	
	token=zu.randomString()
	while token in db.obtenerColumna("valor","tokens"):
		token=zu.randomString()

	db("usuarios").insertar(nombres,apellidos,correo,password,foto,[],token)
	db("tokens").insertar(correo,token,str(zu.DateTime()),str(zu.DateTime(w=4)))
	i=len(db.obtenerColumna("token","usuarios"))-1
	db("tokens").relacionar(i,"usuario",tabla="usuarios",campo="correo",id=i)
	db("usuarios").relacionar(i,"token",tabla="tokens",campo="valor",id=i)
	db.grabar(root_db)

def crearLibro(nombre,autores,colaboradores=[],referencias=[],editorial=None,fechaP=None,url=None,costo=None):

	db("libros").insertar(nombre,autores,colaboradores,referencias,editorial,fechaP,url,costo)
	db.grabar(root_db)

def guardarTema(app,libro,tema,text):
	db("documentos").insertar(app,libro,tema,text)
	db.grabar(root_db)
	
