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


	#functions.ajax(p["base_root"]+"../admin/"+roots.models_folder+roots.ajax_file,{})
	#functions.phpload(p["base_url"]+"../admin/"+roots.libs_folder,"test.php",True)
	