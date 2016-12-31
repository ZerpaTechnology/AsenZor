import sys
sys.path.append("../")
import ztec.zdb as zdb

db=zdb.DB("prueba.db",debug=True)

db("tabla1").delFila(2)
db.grabar("prueba.db")
