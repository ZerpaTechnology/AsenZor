#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zdb

db=zdb.zdb()
db.cargar("base.py")
db.crear_t("empresas",db.campo("nombre",str),db.campo("numero",int),db.campo("dirección",str))
db.sel_t("empresas")
db.insertar_d("123.com","1","la urbina")
db.act()
db.ver_tablas()
