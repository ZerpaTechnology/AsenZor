#!/usr/bin/python
# -*- coding: utf-8 -*-
def cnt(p,m):
	sys.path.append(p["base_root"]+"../admin/")
	import settings.roots as roots
	import settings.config 
	sys.path.append(p["base_root"]+"../admin/"+roots.libs_folder)
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
	