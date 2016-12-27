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
	#print db.tablas

	if token not in db.obtenerColumna("valor","tokens"):
		
		db("usuarios").insertar(nombres,apellidos,correo,password,foto,[],token)
		db("tokens").insertar(correo,token,str(zu.DateTime()),str(zu.DateTime(w=4)))

		i=len(db.obtenerColumna("token","usuarios"))-1

		db("tokens").relacionar(i,"usuario",tabla="usuarios",campo="nombres",id=i)
		
		db("usuarios").relacionar(i,"token",tabla="tokens",campo="valor",id=i)
		
		pass
	db.grabar(root_db)
	

def obtenerColumna(campo,seleccion,db=db):
	return db(seleccion).obtenerColumna(campo,seleccion)

def obtenerFila(campo,seleccion,db=db):
	return db(seleccion).obtenerFila(campo,seleccion)