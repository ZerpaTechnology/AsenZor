#!/usr/bin/python
# -*- coding: utf-8 -*-
import zdb
db=zdb.DB("prueba_db",debug=True)
db.tablas
img=db("imagenes").obtener(0,"binario")
f=open("miranda.jpg","w");
f.write(img)
f.close()

