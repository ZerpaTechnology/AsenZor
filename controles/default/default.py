#!/usr/bin/python
print "Content-type: text/html\n\n"
print "el controlador:<br>"
try:
	#------------------------------------------------
	#HEAD
	import controlador as cnt
	orden=cnt.request.value
	app=orden[2]
	version=orden[3]
	#control=orden[4]
	#vista=orden[5]


	#--------------------------------------------------
	"""
	if control!="default":
		if version == "produccion":
			print '<meta http-equiv="Refresh" content="0;url='+config.host+config.apps_url+app+"controles/"+control+'/'+vista+'/">'
	"""
	#vista html
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = cnt.os.stat(ruta_html)
	#vista python
	(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = cnt.os.stat(ruta_python)

	fm_html=time.ctime(mtime).split(" ")
	fm_python=time.ctime(mtime2).split(" ")
	


except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(ex)+"</p>"