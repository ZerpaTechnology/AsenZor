#Esto es el equibalente a los achivos .sql que se cargan en la base de datos
#  En los modelos no se crea la estructura de la base de datos solo se crean metodos de insercion de datos
db=DB(debug=True)
#====================================
#USERS
db("users").campo("username",db.str,)
db("users").campo("password",db.str)
db("users").campo("email",db.email,unico=True)
db("users").campo("name",db.str)
db("users").campo("lastname",db.str)
db("users").campo("register_date",db.datetime)
db("users").campo("rank",db.int)
db("users").campo("avatar",db.url)
db("users").campo("departament_id",db.int)
db("users").campo("position_id",db.int)
db("users").campo("total_hours",db.str)
#======================================
#POSITIONS
db("positions").campo("name",db.str)
db("users").campo("id_department",db.int)
#======================================
#DEPARTMENT
db("department").campo("name",db.str)
#=======================================
#CHRONOMETERS
db("chronometers").campo("start_date",db.datetime)
db("chronometers").campo("end_date",db.datetime)
db("chronometers").campo("total_hours",db.datetime)
db("chronometers").campo("text",db.str)
db("chronometers").campo("id_user",db.int)
db("chronometers").campo("status",db.bool)
db("chronometers").campo("type",db.int)
#========================================
#USER_PROJECTS
db("user_projects").campo("user_id",db.int)
db("user_projects").campo("project_id",db.int)
#========================================
#PROJECTS
db("projects").campo("name",db.str)
db("projects").campo("description",db.str)
db("projects").campo("start_date",db.datetime)
db("projects").campo("end_date",db.datetime)
db("projects").campo("status",db.bool)



db.grabar(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py")
