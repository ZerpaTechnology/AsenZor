#====================================================================
#Cabecera del modelo
import sys
import os
sys.path.append("../config")

import settings.roots as roots
import settings.config 
from ztec.zdb import DB
name_db=settings.config.dbs[0] #main_db
p=settings.config.p
root_db=p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py"
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
	db("usuarios").insertar(nombres,apellidos,correo,password,foto,imgs)
	db.grabar(root_db)
	
