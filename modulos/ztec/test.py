#!/usr/bin/python
# -*- coding: utf-8 -*-
import zdb
db=zdb.DB("prueba_db2",debug=True)
db.tablas
img=db("imagenes").obtener(0,"binario")
f=open("miranda2.jpg","w");
f.write(img)
f.close()

