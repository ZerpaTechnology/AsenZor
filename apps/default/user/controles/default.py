#!/usr/bin/python
# -*- coding: utf-8 -*-
def cnt(p,m):
	#============================================================
	#Cabecera del controlador
	sys.path.append(p["base_root"]+"../admin/")
	import settings.roots as roots
	import settings.config
	settings.config.p=p
	sys.path.append(p["base_root"]+"../admin/"+roots.libs_folder)
	sys.path.append(p["base_root"]+"../admin/"+roots.models_folder)
	import modelos.main_model as main_model
	#============================================================
	#Cuerpo del controlador
	main_model.registrarUsuario("jesus","zerpa","jesus26abraham1996@gmaill.com","123456",p["base_url"]+"static/imgs/icono_perfil.jpg",[])

	
	for elem in settings.config.libs_python:
		exec("import "+elem)
	if "vista" in p:
		m["servir"](p["base_root"]+roots.vistas_folder+p["vista"]+".html",p["base_root"]+roots.templates_url+p["vista"]+".py")
	
	if "action" in p:

		if p["action"]=="phpload":
			
			if "script" in p:

				if os.path.exists(p["base_root"]+"../admin/"+roots.libs_folder+p["script"]):
					
					functions.ajax(p["base_root"]+"../admin/"+roots.models_folder+roots.ajax_file,{})
					functions.phpload(p["base_url"]+"../admin/"+roots.libs_folder,p["script"],True)
				else:
					print "El script no existe"

			else:
				print "Debes pasar el parametro 'script' con el nombre del script de php a cargar"
	