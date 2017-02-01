#Esto es el equibalente a los achivos .sql que se cargan en la base de datos
#  En los modelos no se crea la estructura de la base de datos solo se crean metodos de insercion de datos
db=DB(debug=True)

#====================================
#USERS
db("users").campo("username",db.str,unico=True)
db("users").campo("email",db.email)
db("users").campo("password",db.password)
db("users").campo("token",db.str,unico=True)#para las operaciones,se usa en las cookies
db("users").campo("expediente",db.str,unico=True)
db("users").campo("ip´s",db.list)#para saber que las operaciones son desde esa ip
db("users").campo("login",db.bool)#para saber si el usuario esta logueado
#====================================
#NOTICIAS
db("noticias").campo("autor",db.str)
db("noticias").campo("titulo",db.str)
db("noticias").campo("img",db.file)
db("noticias").campo("noticia",db.doc)
db("noticias").campo("fecha",db.datetime,formato="%d/%m/%Y %H:%M")
db("noticias").campo("fechaModificación",db.datetime,formato="%d/%m/%Y %H:%M")
#==========================================
#TOKENS
db("tokens").campo("user",db.str)
db("tokens").campo("value",db.str)
db("tokens").campo("nace",db.datetime,formato="%d/%m/%Y %H:%M")
db("tokens").campo("muere",db.datetime,formato='%d/%m/%Y %H:%M')



db.grabar(self.dbfile+"_db.py")
