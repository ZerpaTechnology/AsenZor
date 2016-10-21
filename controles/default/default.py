#!/usr/bin/python
print "Content-type: text/html\n\n"
print "Controlador Principal: default<br>"
try:
	#------------------------------------------------
	#HEAD
	import controlador as cnt

	orden=cnt.request.value
	app=cnt.darTipo(orden[0].value)
	version=cnt.darTipo(orden[1].value)
	control=cnt.darTipo(orden[2].value)
	vista=cnt.darTipo(orden[3].value)





	#--------------------------------------------------
	if control!="default":
		if version == "produccion":
			print '<meta http-equiv="Refresh" content="0;url='+config.base_root+config.apps_url+app+"controles/"+control+'/'+vista+'/">'
	
	else:
		print version
		if version=="produccion":
			if vista!="index":
				print "diferente"
		elif version=="error":
				print "error"
		else:
			if vista!="index":
				print cnt.config.base_root+cnt.config.projects_url+"/"+version+cnt.config.vistas_url+cnt.config.templates_url+vista+".py"
			else:
				f=open(cnt.config.base_root+cnt.config.projects_url+app+"/"+version+"/"+"default/"+cnt.config.vistas_url+"index.html","r")
				html=f.read()
				f.close()
				print html
				#f=open(config.base_root+config.apps_url+app+"/"+config.vistas_url+config.templates_url+vista+".html","r")
						

	#vista html
	#(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = cnt.os.stat(ruta_html)
	#vista python
	#(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = cnt.os.stat(ruta_python)

	#fm_html=time.ctime(mtime).split(" ")
	#fm_python=time.ctime(mtime2).split(" ")
	


except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(ex)+"</p>"