try:
	from modelos.main_model2 import model

	if p["vista"]=="pagNoticias":
		modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["token"],debug=False)
		data["zform"]=zform(modelo.db("noticias"),"pagNoticias",display="block-justify")
		pass
	elif p["vista"]=="registro":
		modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["token"],debug=False)
		data["zform"]=zform(modelo.db("users"),"sing_up",display="block-justify",ignorar=["ip","token","login"],confirmar=["password"],valores={"token":None,"ip":None})
	elif p["vista"]=="index2":

		cookie=""
		if "HTTP_COOKIE" in os.environ:
			cookie=os.environ["HTTP_COOKIE"]

		ip=""
		if "REMOTE_ADDR" in os.environ:
			ip=os.environ["REMOTE_ADDR"]
		cookies=cookie.split(" ")
		token=""
		for elem in cookies:
			if "token=" in elem:
				token=elem.replace("token=","")
		modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["token"],debug=False)

		respuesta=modelo.consultarLogin(token,os.environ["REMOTE_ADDR"])
		if respuesta==True:
			#print "El usuario esta logueado"
			pass
		elif respuesta==False:
			#print "El usuario no esta logueado"
			pass
		else:
			#print "El token no es valido porfavor vuelvase a loguear"
			pass
			
	elif p["vista"]=="index":
		pass





except Exception, e:
	print "error en el subcontrolador vistas:<br>"
	print e