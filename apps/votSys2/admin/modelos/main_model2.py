from zmodel import Model
class model(Model):
	"""docstring for model"""
	def __init__(self, arg):
		super(Model, self).__init__()
	
	#===================================================================
	#Cuerpo del modelo
	def confirmarUsuario(self,nombres,apellidos,correo,password,codigo):
		self.update()
		if self.request():
			self.db("confirmacion").insertar(nombres,apellidos,correo,password,codigo)
			self.db.grabar(self.root_db)

	def registrarUsuario(self,cod,foto=None,imgs=None):
		self.update()
		if self.request():
			filas=self.db("confirmacion").obtenerFilasValores(cod)
			print filas
			for elem in self.db("confirmacion").obtenerFilasId(cod):
				self.db("confirmacion").delFila(elem)
			token=zu.randomString()
			while token in db.obtenerColumna("valor","tokens"):
				token=zu.randomString()

			if cod==filas[4]:
				self.db("usuarios").insertar(filas[0],filas[1],filas[2],filas[3],foto,imgs,token)
				self.db("tokens").insertar(filas[2],token,str(zu.DateTime()),str(zu.DateTime(w=4)))
				i=len(self.db.obtenerColumna("token","usuarios"))-1
				self.db("tokens").relacionar(i,"usuario",tabla="usuarios",campo="correo",id=i)
				self.db("usuarios").relacionar(i,"token",tabla="tokens",campo="valor",id=i)
				self.db.grabar(self.root_db)
			else:
				print filas," - ",cod
				print "el codigo de confirmacion no coincide"

	def crearLibro(self,nombre,autores,colaboradores=[],referencias=[],editorial=None,fechaP=None,url=None,costo=None,db=db):
		self.update()
		if self.request():
			self.db("libros").insertar(nombre,autores,colaboradores,referencias,editorial,fechaP,url,costo)
			self.db.grabar(self.root_db)

	def guardarTema(self,app,libro,tema,text,db=db):
		self.update()
		if self.request:
			self.db("documentos").insertar(app,libro,tema,text)
			self.db.grabar(self.root_db)
			
	def login(self,usuario,password):
		self.update()
		if self.request():

			if self.db("usuarios").obtenerFilasValores(usuario)[-1]==False:
				filas=self.db("usuarios").obtenerFilasValores(usuario)

				if filas[3]==password:

					self.db("usuarios").modificarCampo(self.db("usuarios").obtenerFilasId(usuario)[0],"login",True)
					
					self.db.grabar(self.root_db)
					return True
				else:
					print "la contraseña es incorrecta"
					return False
			else:
				print "Este usuario ya esta logueado"
				return True
			

	def closeSession(self,token):
		self.update()
		if self.request():
			filas=self.db("usuarios").obtenerFilasValores(token)
			if filas[6]==token:
				self.db("usuarios").modificarCampo(self.db("usuarios").obtenerFilasId(token)[0],"login",False)
				newToken=zu.randomString()
				while newToken in self.db.obtenerColumna("valor","tokens"):
					newToken=zu.randomString()
				self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(token)[0],"valor",newToken)
				self.db.grabar(root_db)
				return True
			else:
				return False

	def consultarLogin(self,token):
		self.update()
		if self.request():
			return self.db("usuarios").obtenerFilasValores(token)[-1]
